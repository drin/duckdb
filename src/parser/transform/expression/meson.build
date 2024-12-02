
# ------------------------------
# Headers and Sources

# Sources
duckdb_transformer_expression_sources = [
   'transform_array_access.cpp'
  ,'transform_bool_expr.cpp'
  ,'transform_boolean_test.cpp'
  ,'transform_case.cpp'
  ,'transform_cast.cpp'
  ,'transform_coalesce.cpp'
  ,'transform_columnref.cpp'
  ,'transform_constant.cpp'
  ,'transform_expression.cpp'
  ,'transform_function.cpp'
  ,'transform_grouping_function.cpp'
  ,'transform_lambda.cpp'
  ,'transform_interval.cpp'
  ,'transform_is_null.cpp'
  ,'transform_operator.cpp'
  ,'transform_param_ref.cpp'
  ,'transform_positional_reference.cpp'
  ,'transform_subquery.cpp'
  ,'transform_multi_assign_reference.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_transformer_expression = static_library('duckdb_transformer_expression'
  ,duckdb_transformer_expression_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_transformer_expression.extract_all_objects()

