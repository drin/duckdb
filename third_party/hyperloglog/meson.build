# >> Dependencies


# >> Conditional build args

# hide global symbols
cppargs_hyperloglog = ['-fvisibility=hidden']

# disable warnings
if cmp_name == 'msvc'
  cppargs_hyperloglog += '/W0'

elif cmp_name == 'clang' or cmp_name == 'gcc'
  cppargs_hyperloglog += '-w'

endif


# >> Build targets

# Include targets
libhyperloglog_inc = include_directories('.')

# Library targets
libhyperloglog = static_library('duckdb_hyperloglog'
  ,[ 'hyperloglog.cpp', 'sds.cpp' ]
  ,include_directories: [ libhyperloglog_inc ]
  ,cpp_args           : cppargs_hyperloglog
  ,install            : true
)


# >> Final artifacts
# Accumulate into list of includes for third-party libs (external projects)
ep_inc += [libhyperloglog_inc]
