# ------------------------------
# Conditional build args

# NOTE: kept for direct comparability to CMakeLists.txt; seems unnecessary for meson
if get_option('GENERATE_EXTENSION_ENTRIES')
  add_project_argument('-DGENERATE_EXTENSION_ENTRIES', language: 'cpp')
endif


# ------------------------------
# Headers and Sources

# Sources
function_sources = [
  aggregate_function.cpp
  built_in_functions.cpp
  cast_rules.cpp
  compression_config.cpp
  copy_function.cpp
  encoding_function.cpp
  function.cpp
  function_binder.cpp
  function_list.cpp
  function_set.cpp
  pragma_function.cpp
  macro_function.cpp
  register_function_list.cpp
  scalar_macro_function.cpp
  table_macro_function.cpp
  scalar_function.cpp
  table_function.cpp
  udf_function.cpp
]


# ------------------------------
# Build artifacts (libraries)

# >> Artifacts from subdirectories
subdir('aggregate')
subdir('cast')
subdir('pragma')
subdir('scalar')
subdir('table')

# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_function = static_library('duckdb_function'
  ,function_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_function.extract_all_objects()

