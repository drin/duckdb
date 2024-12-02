
# ------------------------------
# Headers and Sources

# Sources
duckdb_nested_loop_join_sources = [
   'nested_loop_join_inner.cpp'
  ,'nested_loop_join_mark.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_nested_loop_join = static_library('duckdb_nested_loop_join'
  ,duckdb_nested_loop_join_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_nested_loop_join.extract_all_objects()

