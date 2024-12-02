
# ------------------------------
# Headers and Sources

# Sources
duckdb_vector_operations_sources = [
   'boolean_operators.cpp'
  ,'vector_cast.cpp'
  ,'comparison_operators.cpp'
  ,'vector_copy.cpp'
  ,'generators.cpp'
  ,'vector_hash.cpp'
  ,'vector_storage.cpp'
  ,'null_operations.cpp'
  ,'numeric_inplace_operators.cpp'
  ,'is_distinct_from.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_vector_operations = static_library('duckdb_vector_operations'
  ,duckdb_vector_operations_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_vector_operations.extract_all_objects()

