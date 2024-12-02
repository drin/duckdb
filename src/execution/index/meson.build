
# ------------------------------
# Headers and Sources

# Sources
duckdb_execution_index_sources = [
   'fixed_size_allocator.cpp'
  ,'fixed_size_buffer.cpp'
  ,'unbound_index.cpp'
  ,'index_type_set.cpp'
  ,'bound_index.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories
subdir(art)

# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_execution_index = static_library('duckdb_execution_index'
  ,duckdb_execution_index_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_execution_index.extract_all_objects()

