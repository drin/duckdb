
# ------------------------------
# Headers and Sources

# Sources
duckdb_operator_join_sources = [
   'outer_join_marker.cpp'
  ,'physical_asof_join.cpp'
  ,'physical_blockwise_nl_join.cpp'
  ,'physical_comparison_join.cpp'
  ,'physical_cross_product.cpp'
  ,'physical_delim_join.cpp'
  ,'physical_left_delim_join.cpp'
  ,'physical_hash_join.cpp'
  ,'physical_iejoin.cpp'
  ,'physical_join.cpp'
  ,'physical_nested_loop_join.cpp'
  ,'perfect_hash_join_executor.cpp'
  ,'physical_piecewise_merge_join.cpp'
  ,'physical_positional_join.cpp'
  ,'physical_range_join.cpp'
  ,'physical_right_delim_join.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_operator_join = static_library('duckdb_operator_join'
  ,duckdb_operator_join_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_operator_join.extract_all_objects()

