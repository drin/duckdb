# ------------------------------
# Headers and Sources

# Sources
planner_sources = [
   'binding_alias.cpp'
  ,'bound_result_modifier.cpp'
  ,'bound_parameter_map.cpp'
  ,'collation_binding.cpp'
  ,'expression_iterator.cpp'
  ,'expression.cpp'
  ,'table_binding.cpp'
  ,'expression_binder.cpp'
  ,'joinside.cpp'
  ,'logical_operator.cpp'
  ,'binder.cpp'
  ,'bind_context.cpp'
  ,'planner.cpp'
  ,'pragma_handler.cpp'
  ,'logical_operator_visitor.cpp'
  ,'table_filter.cpp'
]


# ------------------------------
# Build artifacts (libraries)

subdir('expression')
subdir('binder')
subdir('expression_binder')
subdir('filter')
subdir('operator')
subdir('subquery')

# An object library (only its objects will be linked against)
objlib_duckdb_planner = static_library('duckdb_planner'
  ,planner_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_planner.extract_all_objects()

