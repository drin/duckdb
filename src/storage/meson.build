
# ------------------------------
# Headers and Sources

# Sources
duckdb_storage_sources = [
   'arena_allocator.cpp'
  ,'buffer_manager.cpp'
  ,'checkpoint_manager.cpp'
  ,'temporary_memory_manager.cpp'
  ,'block.cpp'
  ,'data_pointer.cpp'
  ,'data_table.cpp'
  ,'index.cpp'
  ,'local_storage.cpp'
  ,'magic_bytes.cpp'
  ,'storage_manager.cpp'
  ,'standard_buffer_manager.cpp'
  ,'temporary_file_manager.cpp'
  ,'table_index_list.cpp'
  ,'write_ahead_log.cpp'
  ,'optimistic_data_writer.cpp'
  ,'partial_block_manager.cpp'
  ,'single_file_block_manager.cpp'
  ,'storage_info.cpp'
  ,'storage_lock.cpp'
  ,'wal_replay.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories
subdir(buffer)
subdir(checkpoint)
subdir(compression)
subdir(metadata)
subdir(serialization)
subdir(statistics)
subdir(table)

# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_storage = static_library('duckdb_storage'
  ,duckdb_storage_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_storage.extract_all_objects()

