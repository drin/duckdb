
# ------------------------------
# Headers and Sources

# Sources
duckdb_storage_table_sources = [
   'chunk_info.cpp'
  ,'column_checkpoint_state.cpp'
  ,'column_data_checkpointer.cpp'
  ,'column_data.cpp'
  ,'column_segment.cpp'
  ,'array_column_data.cpp'
  ,'list_column_data.cpp'
  ,'update_segment.cpp'
  ,'persistent_table_data.cpp'
  ,'row_group.cpp'
  ,'row_group_collection.cpp'
  ,'row_version_manager.cpp'
  ,'scan_state.cpp'
  ,'standard_column_data.cpp'
  ,'struct_column_data.cpp'
  ,'table_statistics.cpp'
  ,'validity_column_data.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_storage_table = static_library('duckdb_storage_table'
  ,duckdb_storage_table_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_storage_table.extract_all_objects()

