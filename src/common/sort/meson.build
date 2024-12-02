
# ------------------------------
# Headers and Sources

# Sources
duckdb_sort_sources = [
   'comparators.cpp'
  ,'merge_sorter.cpp'
  ,'partition_state.cpp'
  ,'radix_sort.cpp'
  ,'sort_state.cpp'
  ,'sorted_block.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_sort = static_library('duckdb_sort'
  ,duckdb_sort_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_sort.extract_all_objects()

