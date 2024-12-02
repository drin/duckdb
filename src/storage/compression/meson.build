
# ------------------------------
# Headers and Sources

# Sources
duckdb_storage_compression_sources = [
   'numeric_constant.cpp'
  ,'fixed_size_uncompressed.cpp'
  ,'rle.cpp'
  ,'dictionary_compression.cpp'
  ,'string_uncompressed.cpp'
  ,'uncompressed.cpp'
  ,'validity_uncompressed.cpp'
  ,'bitpacking.cpp'
  ,'bitpacking_hugeint.cpp'
  ,'patas.cpp'
  ,'alprd.cpp'
  ,'fsst.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories
subdir(chimp)
subdir(alp)

# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_storage_compression = static_library('duckdb_storage_compression'
  ,duckdb_storage_compression_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_storage_compression.extract_all_objects()

