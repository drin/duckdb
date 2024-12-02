# ------------------------------
# Headers and Sources

# Sources
aggr_distr_sources = [
   'count.cpp'
  ,'first_last_any.cpp'
  ,'minmax.cpp'
]


# ------------------------------
# Build artifacts (libraries)

# An object library (only its objects will be linked against)
objlib_duckdb_aggr_distr = static_library('duckdb_aggr_distr'
  ,aggr_distr_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_aggr_distr.extract_all_objects()

