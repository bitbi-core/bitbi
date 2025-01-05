FROM ubuntu:22.04

# Avoid interactive prompts during package installation
# ENV DEBIAN_FRONTEND=noninteractive

# Setup proxy if provided
ARG HTTP_PROXY
ARG HTTPS_PROXY
# ENV http_proxy=${HTTP_PROXY}
# ENV https_proxy=${HTTPS_PROXY}

# Print proxy settings
# RUN set -x && \
#     echo "HTTP_PROXY=${HTTP_PROXY}" && \
#     echo "HTTPS_PROXY=${HTTPS_PROXY}" && \
#     if [ ! -z "$HTTP_PROXY" ]; then \
#         echo "Acquire::http::Proxy \"$HTTP_PROXY\";" > /etc/apt/apt.conf.d/proxy.conf; \
#     fi && \
#     if [ ! -z "$HTTPS_PROXY" ]; then \
#         echo "Acquire::https::Proxy \"$HTTPS_PROXY\";" >> /etc/apt/apt.conf.d/proxy.conf; \
#     fi

# Install dependencies matching the GitHub Actions workflow
RUN apt-get update && apt-get install -y \
    libsqlite3-dev \
    libminiupnpc-dev \
    libnatpmp-dev \
    build-essential \
    libtool \
    autotools-dev \
    automake \
    pkg-config \
    bsdmainutils \
    python3 \
    libevent-dev \
    libboost-dev

RUN apt-get install -y curl

# Set working directory
WORKDIR /bitbi

# Copy source files
COPY . .

# Download and setup POW dependency
RUN POW_VERSION=0.2.2 && \
    POW_URL="https://github.com/bitbi-core/pow/releases/download/v${POW_VERSION}/ubuntu-ubuntu-22.04.tar.gz" && \
    POW_HOME="/root/pow" && \
    mkdir -p $POW_HOME && \
    echo "Downloading POW from: $POW_URL" && \
    if ! curl -L -f "$POW_URL" -o /tmp/pow.tar.gz; then \
        echo "Failed to download POW from $POW_URL" && \
        echo "Please verify the URL and version are correct" && \
        exit 1; \
    fi && \
    tar xzf /tmp/pow.tar.gz -C $POW_HOME && \
    rm /tmp/pow.tar.gz && \
    ls -l $POW_HOME

# Build script matching CI workflow
RUN chmod +x ./autogen.sh && \
    ./autogen.sh && \
    POW_HOME="/root/pow" && \
    ./configure \
        --without-wallet \
        --with-gui=no \
        --disable-tests \
        --disable-bench \
        CPPFLAGS="-I$POW_HOME/include" \
        LDFLAGS="-L$POW_HOME/lib -lrandomx" \
        CXXFLAGS="-O2" && \
    mkdir -p depends/x86_64-pc-linux-gnu/lib && \
    make -j$(nproc) src/bitbid && \
    mv ./src/bitbid ./bitbid-ubuntu-x86_64 

# Create artifacts directory and collect binary + dependencies
RUN mkdir -p /artifacts && \
    mv ./bitbid-ubuntu-x86_64 /artifacts/ && \
    echo "Collecting shared library dependencies..." && \
    mkdir -p /artifacts/lib && \
    ldd /artifacts/bitbid-ubuntu-x86_64 | grep "=> /" | awk '{print $3}' | \
    xargs -I '{}' cp -v '{}' /artifacts/lib/ && \
    echo "Creating dependency list..." && \
    ldd /artifacts/bitbid-ubuntu-x86_64 > /artifacts/dependencies.txt && \
    cp -r $POW_HOME/lib/* /artifacts/lib/ && \
    echo "Contents of artifacts directory:" && \
    ls -la /artifacts/

# Create a new stage to package artifacts
FROM busybox:latest as export-stage
# Add a dummy command so container can be created
CMD ["/bin/true"]
COPY --from=0 /artifacts /artifacts 