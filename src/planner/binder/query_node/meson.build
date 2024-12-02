# ------------------------------
# Headers and Sources

# Sources
bind_query_node_sources = [
   'bind_select_node.cpp'
  ,'bind_setop_node.cpp'
  ,'bind_recursive_cte_node.cpp'
  ,'bind_cte_node.cpp'
  ,'bind_table_macro_node.cpp'
  ,'plan_query_node.cpp'
  ,'plan_recursive_cte_node.cpp'
  ,'plan_cte_node.cpp'
  ,'plan_select_node.cpp'
  ,'plan_setop.cpp'
  ,'plan_subquery.cpp'
]


# ------------------------------
# Build artifacts (libraries)

# An object library (only its objects will be linked against)
objlib_duckdb_bind_query_node = static_library('duckdb_bind_query_node'
  ,bind_query_node_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_bind_query_node.extract_all_objects()

