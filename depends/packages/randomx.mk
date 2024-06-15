package=randomx
$(package)_version=0.2.1
$(package)_download_path=https://codeload.github.com/bitbi-core/pow/tar.gz/refs/tags
$(package)_file_name=v$($(package)_version).tar.gz
$(package)_download_file=v$($(package)_version)
$(package)_sha256_hash=f3e0c7165af9fd0474f985537a8f25a3ba0daeb9bed538890fbcba35acb1a370


define $(package)_preprocess_cmds
	cp -f $(BASEDIR)/config.guess $(BASEDIR)/config.sub . 
endef

define $(package)_set_vars
	$(package)_config_opts = -DARCH=native
	$(package)_config_opts_linux = -DARCH=x86_64
	$(package)_config_opts_android = -DCMAKE_TOOLCHAIN_FILE=$(ANDROID_NDK)/build/cmake/android.toolchain.cmake  -DANDROID_ABI=arm64-v8a -DANDROID_PLATFORM=android-$(ANDROID_API_LEVEL) 
endef

define $(package)_config_cmds
	cmake $($(package)_config_opts) ..
	
endef

define $(package)_build_cmds
	cd build
	$(MAKE)
endef

define $(package)_stage_cmds
	mkdir -p $($(package)_staging_prefix_dir)/include $($(package)_staging_prefix_dir)/lib &&\
	install ./src/*.h $($(package)_staging_prefix_dir)/include &&\
	install librandomx.a $($(package)_staging_prefix_dir)/lib
endef

# define $(package)_postprocess_cmds
#   rm lib/*.la
# endef
