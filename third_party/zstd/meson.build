# >> Dependencies


# >> Conditional build args

# hide global symbols
cppargs_zstd = ['-fvisibility=hidden']

# disable warnings
if cmp_name == 'msvc'
  cppargs_zstd += '/W0'

elif cmp_name == 'clang' or cmp_name == 'gcc'
  cppargs_zstd += '-w'

endif


# >> Headers and sources

zstd_sources = [
	 'compress'   / 'zstd_compress_superblock.cpp'
	,'compress'   / 'zstdmt_compress.cpp'
	,'compress'   / 'zstd_double_fast.cpp'
	,'compress'   / 'zstd_fast.cpp'
	,'compress'   / 'zstd_compress_sequences.cpp'
	,'compress'   / 'zstd_ldm.cpp'
	,'compress'   / 'hist.cpp'
	,'compress'   / 'zstd_compress.cpp'
	,'compress'   / 'zstd_lazy.cpp'
	,'compress'   / 'zstd_compress_literals.cpp'
	,'compress'   / 'huf_compress.cpp'
	,'compress'   / 'zstd_opt.cpp'
	,'compress'   / 'fse_compress.cpp'
	,'decompress' / 'zstd_ddict.cpp'
	,'decompress' / 'huf_decompress.cpp'
	,'decompress' / 'zstd_decompress.cpp'
	,'decompress' / 'zstd_decompress_block.cpp'
	,'common'     / 'entropy_common.cpp'
	,'common'     / 'fse_decompress.cpp'
	,'common'     / 'debug.cpp'
	,'common'     / 'xxhash.cpp'
	,'common'     / 'pool.cpp'
	,'common'     / 'threading.cpp'
	,'common'     / 'zstd_common.cpp'
	,'common'     / 'error_private.cpp'
	,'dict'       / 'cover.cpp'
	,'dict'       / 'divsufsort.cpp'
	,'dict'       / 'fastcover.cpp'
	,'dict'       / 'zdict.cpp'
	,'deprecated' / 'zbuff_common.cpp'
	,'deprecated' / 'zbuff_decompress.cpp'
	,'deprecated' / 'zbuff_compress.cpp'
]


# >> Build targets

# Include targets
libzstd_inc = include_directories('include')

# Library targets
libzstd = static_library('duckdb_zstd'
  ,zstd_sources
  ,include_directories: [ libzstd_inc ]
  ,cpp_args           : cppargs_zstd
  ,install            : true
)


# >> Final artifacts
# Accumulate into list of includes for third-party libs (external projects)
ep_inc += [libzstd_inc]
