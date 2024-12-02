
# ------------------------------
# Headers and Sources

# Sources
duckdb_storage_metadata_sources = [
   'metadata_manager.cpp'
  ,'metadata_reader.cpp'
  ,'metadata_writer.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_storage_metadata = static_library('duckdb_storage_metadata'
  ,duckdb_storage_metadata_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_storage_metadata.extract_all_objects()

