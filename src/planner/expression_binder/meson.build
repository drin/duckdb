# ------------------------------
# Headers and Sources

# Sources
expression_binders_sources = [
   'aggregate_binder.cpp'
  ,'alter_binder.cpp'
  ,'base_select_binder.cpp'
  ,'check_binder.cpp'
  ,'column_alias_binder.cpp'
  ,'constant_binder.cpp'
  ,'group_binder.cpp'
  ,'having_binder.cpp'
  ,'lateral_binder.cpp'
  ,'qualify_binder.cpp'
  ,'index_binder.cpp'
  ,'insert_binder.cpp'
  ,'order_binder.cpp'
  ,'relation_binder.cpp'
  ,'returning_binder.cpp'
  ,'select_binder.cpp'
  ,'select_bind_state.cpp'
  ,'table_function_binder.cpp'
  ,'update_binder.cpp'
  ,'where_binder.cpp'
]


# ------------------------------
# Build artifacts (libraries)

# An object library (only its objects will be linked against)
objlib_duckdb_expression_binders = static_library('duckdb_expression_binders'
  ,expression_binders_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_expression_binders.extract_all_objects()

