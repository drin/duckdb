
# ------------------------------
# Headers and Sources

# Sources
duckdb_expression_executor_sources = [
   'execute_between.cpp'
  ,'execute_case.cpp'
  ,'execute_cast.cpp'
  ,'execute_comparison.cpp'
  ,'execute_conjunction.cpp'
  ,'execute_constant.cpp'
  ,'execute_function.cpp'
  ,'execute_operator.cpp'
  ,'execute_parameter.cpp'
  ,'execute_reference.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_expression_executor = static_library('duckdb_expression_executor'
  ,duckdb_expression_executor_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_expression_executor.extract_all_objects()

