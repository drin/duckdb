
# ------------------------------
# Headers and Sources

# Sources
duckdb_common_exception_sources = [
   'binder_exception.cpp'
  ,'catalog_exception.cpp'
  ,'conversion_exception.cpp'
  ,'parser_exception.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_common_exception = static_library('duckdb_common_exception'
  ,duckdb_common_exception_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_common_exception.extract_all_objects()

