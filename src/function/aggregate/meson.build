# ------------------------------
# Headers and Sources

# Sources
func_aggr_sources = [
  'sorted_aggregate_function.cpp'
]


# ------------------------------
# Build artifacts (libraries)

# >> Artifacts from subdirectories
subdir('distributive')

# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_func_aggr = static_library('duckdb_func_aggr'
  ,func_aggr_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_func_aggr.extract_all_objects()

