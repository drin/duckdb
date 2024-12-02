
# ------------------------------
# Headers and Sources

# Sources
duckdb_common_arrow_appender_sources = [
   'bool_data.cpp'
  ,'struct_data.cpp'
  ,'union_data.cpp'
  ,'fixed_size_list_data.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_common_arrow_appender = static_library('duckdb_common_arrow_appender'
  ,duckdb_common_arrow_appender_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_common_arrow_appender.extract_all_objects()

