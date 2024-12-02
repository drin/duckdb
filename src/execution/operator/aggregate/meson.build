
# ------------------------------
# Headers and Sources

# Sources
duckdb_operator_aggregate_sources = [
   'aggregate_object.cpp'
  ,'distinct_aggregate_data.cpp'
  ,'physical_hash_aggregate.cpp'
  ,'grouped_aggregate_data.cpp'
  ,'physical_partitioned_aggregate.cpp'
  ,'physical_perfecthash_aggregate.cpp'
  ,'physical_ungrouped_aggregate.cpp'
  ,'physical_window.cpp'
  ,'physical_streaming_window.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_operator_aggregate = static_library('duckdb_operator_aggregate'
  ,duckdb_operator_aggregate_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_operator_aggregate.extract_all_objects()

