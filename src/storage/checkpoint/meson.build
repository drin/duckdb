
# ------------------------------
# Headers and Sources

# Sources
duckdb_storage_checkpoint_sources = [
   'row_group_writer.cpp'
  ,'table_data_writer.cpp'
  ,'table_data_reader.cpp'
  ,'write_overflow_strings_to_disk.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_storage_checkpoint = static_library('duckdb_storage_checkpoint'
  ,duckdb_storage_checkpoint_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_storage_checkpoint.extract_all_objects()

