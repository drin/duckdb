
# ------------------------------
# Headers and Sources

# Sources
duckdb_execution_index_art_sources = [
   'art_key.cpp'
  ,'node.cpp'
  ,'iterator.cpp'
  ,'leaf.cpp'
  ,'base_node.cpp'
  ,'node48.cpp'
  ,'node256.cpp'
  ,'prefix.cpp'
  ,'base_leaf.cpp'
  ,'node256_leaf.cpp'
  ,'art.cpp'
  ,'plan_art.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_execution_index_art = static_library('duckdb_execution_index_art'
  ,duckdb_execution_index_art_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_execution_index_art.extract_all_objects()

