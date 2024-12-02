# ------------------------------
# Headers and Sources

# Sources
optimizer_pushdown_sources = [
   'pushdown_aggregate.cpp'
  ,'pushdown_cross_product.cpp'
  ,'pushdown_distinct.cpp'
  ,'pushdown_filter.cpp'
  ,'pushdown_get.cpp'
  ,'pushdown_inner_join.cpp'
  ,'pushdown_limit.cpp'
  ,'pushdown_left_join.cpp'
  ,'pushdown_mark_join.cpp'
  ,'pushdown_projection.cpp'
  ,'pushdown_semi_anti_join.cpp'
  ,'pushdown_set_operation.cpp'
  ,'pushdown_single_join.cpp'
  ,'pushdown_window.cpp'
  ,'pushdown_unnest.cpp'
]


# ------------------------------
# Build artifacts (libraries)

# An object library (only its objects will be linked against)
objlib_duckdb_optimizer_pushdown = static_library('duckdb_optimizer_pushdown'
  ,optimizer_pushdown_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_optimizer_pushdown.extract_all_objects()

