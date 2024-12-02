
# ------------------------------
# Headers and Sources

# Sources
duckdb_value_operations_sources = [
   'comparison_operations.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_value_operations = static_library('duckdb_value_operations'
  ,duckdb_value_operations_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default   : false
  ,install            : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_value_operations.extract_all_objects()

