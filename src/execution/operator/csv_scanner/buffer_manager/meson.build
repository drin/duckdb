
# ------------------------------
# Headers and Sources

# Sources
duckdb_csv_buffer_manager_sources = [
   'csv_buffer.cpp'
  ,'csv_buffer_manager.cpp'
  ,'csv_file_handle.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_csv_buffer_manager = static_library('duckdb_csv_buffer_manager'
  ,duckdb_csv_buffer_manager_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_csv_buffer_manager.extract_all_objects()

