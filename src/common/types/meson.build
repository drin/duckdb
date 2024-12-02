# ------------------------------
# Headers and Sources

# Sources
duckdb_common_types_sources = [
   'batched_data_collection.cpp'
  ,'bit.cpp'
  ,'blob.cpp'
  ,'cast_helpers.cpp'
  ,'conflict_manager.cpp'
  ,'conflict_info.cpp'
  ,'data_chunk.cpp'
  ,'date.cpp'
  ,'decimal.cpp'
  ,'hash.cpp'
  ,'hugeint.cpp'
  ,'uhugeint.cpp'
  ,'uuid.cpp'
  ,'hyperloglog.cpp'
  ,'interval.cpp'
  ,'list_segment.cpp'
  ,'selection_vector.cpp'
  ,'string_heap.cpp'
  ,'string_type.cpp'
  ,'timestamp.cpp'
  ,'time.cpp'
  ,'validity_mask.cpp'
  ,'value.cpp'
  ,'varint.cpp'
  ,'vector_buffer.cpp'
  ,'vector.cpp'
  ,'vector_cache.cpp'
  ,'vector_constants.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories
subdir(column)
subdir(row)

# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_common_types = static_library('duckdb_common_types'
  ,duckdb_common_types_sources
  ,include_directories: [ libduckdb_inc ]
  ,cpp_args           : [ '-Wno-exit-time-destructors' ]
  ,build_by_default   : false
  ,install            : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_common_types.extract_all_objects()

