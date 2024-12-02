
# ------------------------------
# Headers and Sources

# Sources
duckdb_csv_sniffer_sources = [
   'csv_sniffer.cpp'
  ,'dialect_detection.cpp'
  ,'header_detection.cpp'
  ,'type_detection.cpp'
  ,'type_refinement.cpp'
  ,'type_replacement.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_csv_sniffer = static_library('duckdb_csv_sniffer'
  ,duckdb_csv_sniffer_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_csv_sniffer.extract_all_objects()

