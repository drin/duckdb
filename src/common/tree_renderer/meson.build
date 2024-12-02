
# ------------------------------
# Headers and Sources

# Sources
duckdb_common_tree_renderer_sources = [
   'json_tree_renderer.cpp'
  ,'html_tree_renderer.cpp'
  ,'graphviz_tree_renderer.cpp'
  ,'text_tree_renderer.cpp'
  ,'tree_renderer.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_common_tree_renderer = static_library('duckdb_common_tree_renderer'
  ,duckdb_common_tree_renderer_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default   : false
  ,install            : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_common_tree_renderer.extract_all_objects()

