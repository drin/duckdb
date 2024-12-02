# ------------------------------
# Headers and Sources

# Sources
planner_operator_sources = [
   'logical_aggregate.cpp'
  ,'logical_any_join.cpp'
  ,'logical_column_data_get.cpp'
  ,'logical_comparison_join.cpp'
  ,'logical_copy_to_file.cpp'
  ,'logical_copy_database.cpp'
  ,'logical_create.cpp'
  ,'logical_create_index.cpp'
  ,'logical_create_table.cpp'
  ,'logical_cross_product.cpp'
  ,'logical_cteref.cpp'
  ,'logical_delete.cpp'
  ,'logical_delim_get.cpp'
  ,'logical_dependent_join.cpp'
  ,'logical_distinct.cpp'
  ,'logical_dummy_scan.cpp'
  ,'logical_empty_result.cpp'
  ,'logical_export.cpp'
  ,'logical_expression_get.cpp'
  ,'logical_extension_operator.cpp'
  ,'logical_filter.cpp'
  ,'logical_get.cpp'
  ,'logical_insert.cpp'
  ,'logical_join.cpp'
  ,'logical_limit.cpp'
  ,'logical_order.cpp'
  ,'logical_pivot.cpp'
  ,'logical_positional_join.cpp'
  ,'logical_pragma.cpp'
  ,'logical_prepare.cpp'
  ,'logical_projection.cpp'
  ,'logical_recursive_cte.cpp'
  ,'logical_materialized_cte.cpp'
  ,'logical_sample.cpp'
  ,'logical_set.cpp'
  ,'logical_reset.cpp'
  ,'logical_set_operation.cpp'
  ,'logical_simple.cpp'
  ,'logical_top_n.cpp'
  ,'logical_unconditional_join.cpp'
  ,'logical_unnest.cpp'
  ,'logical_update.cpp'
  ,'logical_vacuum.cpp'
  ,'logical_window.cpp'
]


# ------------------------------
# Build artifacts (libraries)

# An object library (only its objects will be linked against)
objlib_duckdb_planner_operator = static_library('duckdb_planner_operator'
  ,planner_operator_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_planner_operator.extract_all_objects()

