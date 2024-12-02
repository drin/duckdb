
# ------------------------------
# Headers and Sources

# Sources
duckdb_csv_util_sources = [
   'csv_error.cpp'
  ,'csv_reader_options.cpp'
  ,'csv_validator.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_csv_util = static_library('duckdb_csv_util'
  ,duckdb_csv_util_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_csv_util.extract_all_objects()

