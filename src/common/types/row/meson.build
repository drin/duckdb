# ------------------------------
# Headers and Sources

# Sources
duckdb_common_types_row_sources = [
   'partitioned_tuple_data.cpp'
  ,'row_data_collection.cpp'
  ,'row_data_collection_scanner.cpp'
  ,'row_layout.cpp'
  ,'tuple_data_allocator.cpp'
  ,'tuple_data_collection.cpp'
  ,'tuple_data_iterator.cpp'
  ,'tuple_data_layout.cpp'
  ,'tuple_data_scatter_gather.cpp'
  ,'tuple_data_segment.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_common_types_row = static_library('duckdb_common_types_row'
  ,duckdb_common_types_row_sources
  ,include_directories: [ libduckdb_inc ]
  ,cpp_args           : [ '-Wno-exit-time-destructors' ]
  ,build_by_default   : false
  ,install            : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_common_types_row.extract_all_objects()

