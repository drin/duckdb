
# ------------------------------
# Headers and Sources

# Sources
duckdb_operator_helper_sources = [
   'physical_batch_collector.cpp'
  ,'physical_buffered_collector.cpp'
  ,'physical_buffered_batch_collector.cpp'
  ,'physical_create_secret.cpp'
  ,'physical_execute.cpp'
  ,'physical_explain_analyze.cpp'
  ,'physical_limit.cpp'
  ,'physical_limit_percent.cpp'
  ,'physical_load.cpp'
  ,'physical_materialized_collector.cpp'
  ,'physical_pragma.cpp'
  ,'physical_prepare.cpp'
  ,'physical_reservoir_sample.cpp'
  ,'physical_result_collector.cpp'
  ,'physical_set.cpp'
  ,'physical_set_variable.cpp'
  ,'physical_reset.cpp'
  ,'physical_streaming_limit.cpp'
  ,'physical_streaming_sample.cpp'
  ,'physical_transaction.cpp'
  ,'physical_update_extensions.cpp'
  ,'physical_vacuum.cpp'
  ,'physical_verify_vector.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_operator_helper = static_library('duckdb_operator_helper'
  ,duckdb_operator_helper_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_operator_helper.extract_all_objects()

