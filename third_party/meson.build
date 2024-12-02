# ------------------------------
# Build targets

# >> Include targets
# Header only (no further build definitions)
ep_inc += [
   include_directories('pcg')
  ,include_directories('tdigest')
  ,include_directories('fast_float')
  ,include_directories('jaro_winkler')
  ,include_directories('concurrentqueue')
]

# >> Targets from subdirectories

# NOTE: these will accumulate include targets into `ep_inc`
subdir('hyperloglog')
subdir('fastpforlib')
subdir('fmt')
subdir('fsst')
subdir('mbedtls')
subdir('miniz')
subdir('skiplist')
subdir('utf8proc')
subdir('yyjson')
subdir('zstd')

# This is a subproject in cmake, but a meson subproject seems unnecessary
subdir('re2')

