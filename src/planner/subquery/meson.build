# ------------------------------
# Headers and Sources

# Sources
planner_subquery_sources = [
   'flatten_dependent_join.cpp'
  ,'has_correlated_expressions.cpp'
  ,'rewrite_correlated_expressions.cpp'
  ,'rewrite_cte_scan.cpp'
]


# ------------------------------
# Build artifacts (libraries)

# An object library (only its objects will be linked against)
objlib_duckdb_planner_subquery = static_library('duckdb_planner_subquery'
  ,planner_subquery_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_planner_subquery.extract_all_objects()

