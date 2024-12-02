# >> Dependencies


# >> Conditional build args

# hide global symbols
cppargs_yyjson = ['-fvisibility=hidden']

# disable warnings
if cmp_name == 'msvc'
  cppargs_yyjson += '/W0'

elif cmp_name == 'clang' or cmp_name == 'gcc'
  cppargs_yyjson += '-w'

endif


# >> Build targets

# Include targets
libyyjson_inc = include_directories('include')

# Library targets
libyyjson = static_library('duckdb_yyjson'
  ,'yyjson.cpp'
  ,include_directories: [ libyyjson_inc ]
  ,cpp_args           : cppargs_yyjson
  ,install            : true
)


# >> Final artifacts
# Accumulate into list of includes for third-party libs (external projects)
ep_inc += [libyyjson_inc]
