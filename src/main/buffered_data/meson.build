
# ------------------------------
# Headers and Sources

# Sources
duckdb_main_buffered_data_sources = [
   'buffered_data.cpp'
  ,'simple_buffered_data.cpp'
  ,'batched_buffered_data.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_main_buffered_data = static_library('duckdb_main_buffered_data'
  ,duckdb_main_buffered_data_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_main_buffered_data.extract_all_objects()

