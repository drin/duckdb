# >> Dependencies


# >> Conditional build args

# hide global symbols
cppargs_fastpforlib = ['-fvisibility=hidden']

# disable warnings
if cmp_name == 'msvc'
  cppargs_fastpforlib += '/W0'

elif cmp_name == 'clang' or cmp_name == 'gcc'
  cppargs_fastpforlib += '-w'

endif


# >> Build targets

# Include targets
libfastpforlib_inc = include_directories('.')

# Library targets
libfastpforlib = static_library('duckdb_fastpforlib'
  ,'bitpacking.cpp'
  ,include_directories: [ libfastpforlib_inc ]
  ,cpp_args           : cppargs_fastpforlib
  ,install            : true
)


# >> Final artifacts
# Accumulate into list of includes for third-party libs (external projects)
ep_inc += [libfastpforlib_inc]
