# >> Conditional build args

# hide global symbols
cppargs_fmt = ['-fvisibility=hidden']

# disable warnings
if cmp_name == 'msvc'
  cppargs_fmt += '/W0'

elif cmp_name == 'clang' or cmp_name == 'gcc'
  cppargs_fmt += '-w'

endif


# >> Build targets

# Include targets
libfmt_inc = include_directories('include')

# Library targets
libfmt = static_library('duckdb_fmt'
  ,'format.cc'
  ,include_directories: [ libfmt_inc ]
  ,cpp_args           : cppargs_fmt
  ,install            : true
)


# >> Final artifacts
# Accumulate into list of includes for third-party libs (external projects)
ep_inc += [libfmt_inc]
