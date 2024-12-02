# ------------------------------
# Headers and Sources

# Sources
bind_tableref_sources = [
   'bind_basetableref.cpp'
  ,'bind_delimgetref.cpp'
  ,'bind_emptytableref.cpp'
  ,'bind_expressionlistref.cpp'
  ,'bind_column_data_ref.cpp'
  ,'bind_joinref.cpp'
  ,'bind_pivot.cpp'
  ,'bind_showref.cpp'
  ,'bind_subqueryref.cpp'
  ,'bind_table_function.cpp'
  ,'bind_named_parameters.cpp'
  ,'plan_basetableref.cpp'
  ,'plan_delimgetref.cpp'
  ,'plan_dummytableref.cpp'
  ,'plan_expressionlistref.cpp'
  ,'plan_column_data_ref.cpp'
  ,'plan_joinref.cpp'
  ,'plan_subqueryref.cpp'
  ,'plan_table_function.cpp'
  ,'plan_cteref.cpp'
  ,'plan_pivotref.cpp'
]


# ------------------------------
# Build artifacts (libraries)

# An object library (only its objects will be linked against)
objlib_duckdb_bind_tableref = static_library('duckdb_bind_tableref'
  ,bind_tableref_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_bind_tableref.extract_all_objects()

