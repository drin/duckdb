
# ------------------------------
# Headers and Sources

# Sources
duckdb_storage_buffer_sources = [
   'buffer_handle.cpp'
  ,'block_handle.cpp'
  ,'block_manager.cpp'
  ,'buffer_pool.cpp'
  ,'buffer_pool_reservation.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_storage_buffer = static_library('duckdb_storage_buffer'
  ,duckdb_storage_buffer_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_storage_buffer.extract_all_objects()

