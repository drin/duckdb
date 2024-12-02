
# ------------------------------
# Headers and Sources

# Sources
duckdb_csv_scanner_sources = [
   'base_scanner.cpp'
  ,'column_count_scanner.cpp'
  ,'csv_schema.cpp'
  ,'scanner_boundary.cpp'
  ,'skip_scanner.cpp'
  ,'string_value_scanner.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_csv_scanner = static_library('duckdb_csv_scanner'
  ,duckdb_csv_scanner_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_csv_scanner.extract_all_objects()

