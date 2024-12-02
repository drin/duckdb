# >> Dependencies


# >> Conditional build args

# hide global symbols
cppargs_skiplist = ['-fvisibility=hidden']

# disable warnings
if cmp_name == 'msvc'
  cppargs_skiplist += '/W0'

elif cmp_name == 'clang' or cmp_name == 'gcc'
  cppargs_skiplist += '-w'

endif


# >> Build targets

# Include targets
libskiplist_inc = include_directories('.')

# Library targets
libskiplist = static_library('duckdb_skiplist'
  ,'SkipList.cpp'
  ,include_directories: [ libskiplist_inc ]
  ,cpp_args           : cppargs_skiplist
  ,install            : true
)


# >> Final artifacts
# Accumulate into list of includes for third-party libs (external projects)
ep_inc += [libskiplist_inc]
