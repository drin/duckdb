# >> Dependencies

dependency('threads')


# >> Conditional build args

# hide global symbols
cppargs_fsst = ['-fvisibility=hidden']

# disable warnings
if cmp_name == 'msvc'
  cppargs_fsst += '/W0'

elif cmp_name == 'clang' or cmp_name == 'gcc'
  cppargs_fsst += '-w'

endif


# >> Build targets

# Include targets
libfsst_inc = include_directories('.')

# Library targets
libfsst = static_library('duckdb_fsst'
  ,'libfsst.cpp'
  ,include_directories: [ libfsst_inc ]
  ,cpp_args           : cppargs_fsst
  ,install            : true
)


# >> Final artifacts
# Accumulate into list of includes for third-party libs (external projects)
ep_inc += [libfsst_inc]
