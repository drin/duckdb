# ------------------------------
# Headers and Sources

# Sources
optimizer_statistics_op_sources = [
   'propagate_aggregate.cpp'
  ,'propagate_cross_product.cpp'
  ,'propagate_filter.cpp'
  ,'propagate_get.cpp'
  ,'propagate_limit.cpp'
  ,'propagate_join.cpp'
  ,'propagate_order.cpp'
  ,'propagate_projection.cpp'
  ,'propagate_set_operation.cpp'
  ,'propagate_window.cpp'
]


# ------------------------------
# Build artifacts (libraries)

# An object library (only its objects will be linked against)
objlib_duckdb_optimizer_statistics_op = static_library('duckdb_optimizer_statistics_op'
  ,optimizer_statistics_op_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_optimizer_statistics_op.extract_all_objects()

