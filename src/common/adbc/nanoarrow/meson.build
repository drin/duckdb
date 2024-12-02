
# ------------------------------
# Headers and Sources

# Sources
duckdb_adbc_nanoarrow_sources = [
   'metadata.cpp'
  ,'schema.cpp'
  ,'allocator.cpp'
  ,'single_batch_array_stream.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_adbc_nanoarrow = static_library('duckdb_adbc_nanoarrow'
  ,duckdb_adbc_nanoarrow_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_adbc_nanoarrow.extract_all_objects()

