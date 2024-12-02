
# ------------------------------
# Headers and Sources

# Sources
duckdb_main_chunk_scan_state_sources = [
   'query_result.cpp'
  ,'batched_data_collection.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_main_chunk_scan_state = static_library('duckdb_main_chunk_scan_state'
  ,duckdb_main_chunk_scan_state_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_main_chunk_scan_state.extract_all_objects()

