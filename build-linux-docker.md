# Building BitBi for Linux Using Docker

This document describes how to build BitBi daemon for Linux using Docker. This method ensures a consistent build environment and makes it easy to collect all necessary binaries and dependencies.

## Prerequisites

- Docker installed and running on a Linux system
- Git repository cloned
- Basic familiarity with command line operations

## Building Process

1. Build the Docker image:

```bash
docker build -t bitbi-build .
```


2. Extract the artifacts:
```bash
# Create a temporary container
docker create --name temp bitbi-build:latest
# Create local artifacts directory
mkdir -p ./artifacts
# Copy artifacts from container to host
docker cp temp:/artifacts/. ./artifacts/
# Clean up
docker rm temp
```


## Build Outputs

After successful build, the `./artifacts` directory will contain:

- `bitbid-ubuntu-x86_64` - The BitBi daemon binary
- `lib/` - Directory containing:
  - Required system shared libraries
  - POW module libraries
- `dependencies.txt` - List of all shared library dependencies

## Build Configuration

The binary is built with the following configuration:
- Base system: Ubuntu 22.04
- POW version: 0.2.2
- Build options:
  - Wallet functionality disabled (`--without-wallet`)
  - GUI disabled (`--with-gui=no`)
  - Tests disabled (`--disable-tests`)
  - Benchmarks disabled (`--disable-bench`)
  - Optimization level: -O2

## Dependencies

The build process automatically installs and configures:
- Essential build tools (build-essential, autotools, etc.)
- Required libraries:
  - libsqlite3-dev
  - libminiupnpc-dev
  - libnatpmp-dev
  - libevent-dev
  - libboost-dev
- POW module (downloaded during build)

## Proxy Configuration (Optional)

If you're behind a proxy, configure the build with:

```bash
docker build -t bitbi-build --build-arg HTTP_PROXY=${HTTP_PROXY} --build-arg HTTPS_PROXY=${HTTPS_PROXY} --build-arg NO_PROXY=${NO_PROXY} .
```
