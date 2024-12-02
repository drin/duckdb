
# ------------------------------
# Headers and Sources

# Sources
duckdb_storage_compression_alp_sources = [
   'alp_constants.cpp'
  ,'alp.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_storage_compression_alp = static_library('duckdb_storage_compression_alp'
  ,duckdb_storage_compression_alp_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_storage_compression_alp.extract_all_objects()

