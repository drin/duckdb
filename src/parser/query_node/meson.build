
# ------------------------------
# Headers and Sources

# Sources
duckdb_query_node_sources = [
   'recursive_cte_node.cpp'
  ,'cte_node.cpp'
  ,'select_node.cpp'
  ,'set_operation_node.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_query_node = static_library('duckdb_query_node'
  ,duckdb_query_node_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_query_node.extract_all_objects()

