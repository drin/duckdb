# >> Dependencies


# >> Conditional build args

# hide global symbols
cppargs_re2 = ['-fvisibility=hidden', '-DRE2_ON_VALGRIND']

# disable warnings
if cmp_name == 'msvc'
  cppargs_re2 += '/W0'

elif cmp_name == 'clang' or cmp_name == 'gcc'
  cppargs_re2 += '-w'

endif

# Check the compiler toolchain
if cmp_name == 'msvc'
  cppargs_re2 += ['/wd4100', '/wd4201', '/wd4456', '/wd4457', '/wd4702', '/wd4815', '/utf-8']

elif cmp_name == 'gcc' or cmp_name == 'clang'
  cppargs_re2 += 'std=c++11'

endif

# Check if we're on cygwin which calls c++11 gnu++11
if sys_name == 'cygwin'
  cppargs_re2 += 'std=gnu++11'
endif

# Check if we're on a windows system, then set other flags
if sys_name == 'windows'
  cppargs_re2 += [
     '-DUNICODE'
    ,'-D_UNICODE'
    ,'-DSTRICT'
    ,'-DNOMINMAX'
    ,'-D_CRT_SECURE_NO_WARNINGS'
    ,'-D_SCL_SECURE_NO_WARNINGS'
  ]
endif


# >> Headers and sources

re2_sources = [
   're2/bitmap256.cc'
  ,'re2/compile.cc'
  ,'re2/bitstate.cc'
  ,'re2/dfa.cc'
  ,'re2/filtered_re2.cc'
  ,'re2/mimics_pcre.cc'
  ,'re2/nfa.cc'
  ,'re2/onepass.cc'
  ,'re2/parse.cc'
  ,'re2/perl_groups.cc'
  ,'re2/prefilter.cc'
  ,'re2/prefilter_tree.cc'
  ,'re2/prog.cc'
  ,'re2/re2.cc'
  ,'re2/regexp.cc'
  ,'re2/set.cc'
  ,'re2/simplify.cc'
  ,'re2/stringpiece.cc'
  ,'re2/tostring.cc'
  ,'re2/unicode_casefold.cc'
  ,'re2/unicode_groups.cc'
  ,'util/rune.cc'
  ,'util/strutil.cc'
]


# >> Build targets

# Include targets
libre2_inc = include_directories('.')

# Library targets
libre2 = static_library('duckdb_re2'
  ,re2_sources
  ,include_directories: [ libre2_inc ]
  ,cpp_args           : cppargs_re2
  ,install            : true
)


# >> Final artifacts
# Accumulate into list of includes for third-party libs (external projects)
ep_inc += [libre2_inc]
