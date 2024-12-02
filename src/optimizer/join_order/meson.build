# ------------------------------
# Headers and Sources

# Sources
optimizer_join_order_sources = [
   'query_graph.cpp'
  ,'join_relation_set.cpp'
  ,'join_node.cpp'
  ,'join_order_optimizer.cpp'
  ,'cardinality_estimator.cpp'
  ,'cost_model.cpp'
  ,'plan_enumerator.cpp'
  ,'relation_manager.cpp'
  ,'query_graph_manager.cpp'
  ,'relation_statistics_helper.cpp'
]


# ------------------------------
# Build artifacts (libraries)

# An object library (only its objects will be linked against)
objlib_duckdb_optimizer_join_order = static_library('duckdb_optimizer_join_order'
  ,optimizer_join_order_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_optimizer_join_order.extract_all_objects()

