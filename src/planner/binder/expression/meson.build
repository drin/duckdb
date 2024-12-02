# ------------------------------
# Headers and Sources

# Sources
bind_expression_sources = [
   bind_aggregate_expression.cpp
  ,bind_between_expression.cpp
  ,bind_case_expression.cpp
  ,bind_cast_expression.cpp
  ,bind_collate_expression.cpp
  ,bind_columnref_expression.cpp
  ,bind_comparison_expression.cpp
  ,bind_conjunction_expression.cpp
  ,bind_constant_expression.cpp
  ,bind_function_expression.cpp
  ,bind_lambda.cpp
  ,bind_macro_expression.cpp
  ,bind_operator_expression.cpp
  ,bind_parameter_expression.cpp
  ,bind_positional_reference_expression.cpp
  ,bind_unpacked_star_expression.cpp
  ,bind_star_expression.cpp
  ,bind_subquery_expression.cpp
  ,bind_unnest_expression.cpp
  ,bind_window_expression.cpp
]


# ------------------------------
# Build artifacts (libraries)

# An object library (only its objects will be linked against)
objlib_duckdb_bind_expression = static_library('duckdb_bind_expression'
  ,bind_expression_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_bind_expression.extract_all_objects()

