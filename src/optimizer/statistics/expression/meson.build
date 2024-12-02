# ------------------------------
# Headers and Sources

# Sources
optimizer_statistics_expr_sources = [
   'propagate_aggregate.cpp'
  ,'propagate_between.cpp'
  ,'propagate_case.cpp'
  ,'propagate_cast.cpp'
  ,'propagate_comparison.cpp'
  ,'propagate_conjunction.cpp'
  ,'propagate_constant.cpp'
  ,'propagate_columnref.cpp'
  ,'propagate_function.cpp'
  ,'propagate_operator.cpp')
]


# ------------------------------
# Build artifacts (libraries)

# An object library (only its objects will be linked against)
objlib_duckdb_optimizer_statistics_expr = static_library('duckdb_optimizer_statistics_expr'
  ,optimizer_statistics_expr_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_optimizer_statistics_expr.extract_all_objects()

