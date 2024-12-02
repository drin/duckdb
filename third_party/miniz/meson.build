# >> Dependencies


# >> Conditional build args

# hide global symbols
cppargs_miniz = ['-fvisibility=hidden']

# disable warnings
if cmp_name == 'msvc'
  cppargs_miniz += '/W0'

elif cmp_name == 'clang' or cmp_name == 'gcc'
  cppargs_miniz += '-w'

endif


# >> Build targets

# Include targets
libminiz_inc = include_directories('.')

# Library targets
libminiz = static_library('duckdb_miniz'
  ,'miniz.cpp'
  ,include_directories: [ libminiz_inc ]
  ,cpp_args           : cppargs_miniz
  ,install            : true
)


# >> Final artifacts
# Accumulate into list of includes for third-party libs (external projects)
ep_inc += [libminiz_inc]
