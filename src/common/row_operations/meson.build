
# ------------------------------
# Headers and Sources

# Sources
duckdb_row_operations_sources = [
   'row_aggregate.cpp'
  ,'row_scatter.cpp'
  ,'row_gather.cpp'
  ,'row_matcher.cpp'
  ,'row_external.cpp'
  ,'row_radix_scatter.cpp'
  ,'row_heap_scatter.cpp'
  ,'row_heap_gather.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_row_operations = static_library('duckdb_row_operations'
  ,duckdb_row_operations_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default   : false
  ,install            : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_row_operations.extract_all_objects()

