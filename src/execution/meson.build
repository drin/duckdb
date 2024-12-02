
# ------------------------------
# Headers and Sources

# Sources
duckdb_execution_sources = [
   'adaptive_filter.cpp'
  ,'aggregate_hashtable.cpp'
  ,'base_aggregate_hashtable.cpp'
  ,'column_binding_resolver.cpp'
  ,'expression_executor.cpp'
  ,'expression_executor_state.cpp'
  ,'join_hashtable.cpp'
  ,'perfect_aggregate_hashtable.cpp'
  ,'physical_operator.cpp'
  ,'physical_plan_generator.cpp'
  ,'radix_partitioned_hashtable.cpp'
  ,'reservoir_sample.cpp'
  ,'window_executor.cpp'
  ,'window_segment_tree.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories
subdir(expression_executor)
subdir(nested_loop_join)
subdir(operator)
subdir(physical_plan)
subdir(index)

# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_execution = static_library('duckdb_execution'
  ,duckdb_execution_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_execution.extract_all_objects()

