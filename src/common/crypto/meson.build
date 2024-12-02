
# ------------------------------
# Headers and Sources

# Sources
duckdb_common_crypto_sources = [
   'md5.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_common_crypto = static_library('duckdb_common_crypto'
  ,duckdb_common_crypto_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_common_crypto.extract_all_objects()

