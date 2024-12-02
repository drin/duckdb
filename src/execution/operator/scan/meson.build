
# ------------------------------
# Headers and Sources

# Sources
duckdb_operator_scan_sources = [
   'physical_column_data_scan.cpp'
  ,'physical_dummy_scan.cpp'
  ,'physical_empty_result.cpp'
  ,'physical_expression_scan.cpp'
  ,'physical_positional_scan.cpp'
  ,'physical_table_scan.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_operator_scan = static_library('duckdb_operator_scan'
  ,duckdb_operator_scan_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_operator_scan.extract_all_objects()

