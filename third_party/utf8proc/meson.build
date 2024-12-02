# >> Conditional build args

# hide global symbols
cppargs_utf8proc = ['-fvisibility=hidden']


# >> Build targets

# Include targets
libutf8proc_inc = include_directories('include')

# Library targets
libutf8proc = static_library('duckdb_utf8proc'
  ,[ 'utf8proc.cpp', 'utf8proc_wrapper.cpp' ]
  ,include_directories: [ libutf8proc_inc ]
  ,cpp_args           : cppargs_utf8proc
  ,install            : true
)


# >> Final artifacts
# Accumulate into list of includes for third-party libs (external projects)
ep_inc += [libutf8proc_inc]
