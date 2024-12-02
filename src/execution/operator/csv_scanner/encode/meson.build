
# ------------------------------
# Headers and Sources

# Sources
duckdb_csv_encode_sources = [
   'csv_encoder.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_csv_encode = static_library('duckdb_csv_encode'
  ,duckdb_csv_encode_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_csv_encode.extract_all_objects()

