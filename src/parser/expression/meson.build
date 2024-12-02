
# ------------------------------
# Headers and Sources

# Sources
duckdb_expression_sources = [
   'between_expression.cpp'
  ,'case_expression.cpp'
  ,'cast_expression.cpp'
  ,'collate_expression.cpp'
  ,'conjunction_expression.cpp'
  ,'columnref_expression.cpp'
  ,'comparison_expression.cpp'
  ,'constant_expression.cpp'
  ,'default_expression.cpp'
  ,'function_expression.cpp'
  ,'lambda_expression.cpp'
  ,'lambdaref_expression.cpp'
  ,'operator_expression.cpp'
  ,'parameter_expression.cpp'
  ,'positional_reference_expression.cpp'
  ,'star_expression.cpp'
  ,'subquery_expression.cpp'
  ,'window_expression.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_expression = static_library('duckdb_expression'
  ,duckdb_expression_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_expression.extract_all_objects()

