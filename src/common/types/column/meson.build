# ------------------------------
# Headers and Sources

# Sources
duckdb_common_types_column_sources = [
   'column_data_allocator.cpp'
  ,'column_data_collection.cpp'
  ,'column_data_collection_segment.cpp'
  ,'column_data_consumer.cpp'
  ,'partitioned_column_data.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_common_types_column = static_library('duckdb_common_types_column'
  ,duckdb_common_types_column_sources
  ,include_directories: [ libduckdb_inc ]
  ,cpp_args           : [ '-Wno-exit-time-destructors' ]
  ,build_by_default   : false
  ,install            : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_common_types_column.extract_all_objects()

