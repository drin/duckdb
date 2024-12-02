# ------------------------------
# Headers and Sources

# Sources
optimizer_compressed_materialization_sources = [
   'compress_aggregate.cpp'
  ,'compress_comparison_join.cpp'
  ,'compress_distinct.cpp'
  ,'compress_order.cpp'
]


# ------------------------------
# Build artifacts (libraries)

# An object library (only its objects will be linked against)
objlib_duckdb_optimizer_compressed_materialization = static_library('duckdb_optimizer_compressed_materialization'
  ,optimizer_compressed_materialization_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_optimizer_compressed_materialization.extract_all_objects()

