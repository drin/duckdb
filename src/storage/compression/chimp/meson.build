
# ------------------------------
# Headers and Sources

# Sources
duckdb_storage_compression_chimp_sources = [
   'bit_reader.cpp'
  ,'chimp_constants.cpp'
  ,'flag_buffer.cpp'
  ,'leading_zero_buffer.cpp'
  ,'chimp.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_storage_compression_chimp = static_library('duckdb_storage_compression_chimp'
  ,duckdb_storage_compression_chimp_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_storage_compression_chimp.extract_all_objects()

