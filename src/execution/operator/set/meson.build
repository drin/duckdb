
# ------------------------------
# Headers and Sources

# Sources
duckdb_operator_set_sources = [
   'physical_union.cpp'
  ,'physical_recursive_cte.cpp'
  ,'physical_cte.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_operator_set = static_library('duckdb_operator_set'
  ,duckdb_operator_set_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_operator_set.extract_all_objects()

