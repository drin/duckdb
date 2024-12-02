
# ------------------------------
# Headers and Sources

# Sources
duckdb_operator_csv_table_function_sources = [
   'csv_file_scanner.cpp'
  ,'global_csv_state.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_operator_csv_table_function = static_library('duckdb_operator_csv_table_function'
  ,duckdb_operator_csv_table_function_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_operator_csv_table_function.extract_all_objects()

