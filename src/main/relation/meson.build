
# ------------------------------
# Headers and Sources

# Sources
duckdb_main_relation_sources = [
   'aggregate_relation.cpp'
  ,'create_table_relation.cpp'
  ,'create_view_relation.cpp'
  ,'cross_product_relation.cpp'
  ,'delete_relation.cpp'
  ,'delim_get_relation.cpp'
  ,'distinct_relation.cpp'
  ,'explain_relation.cpp'
  ,'filter_relation.cpp'
  ,'insert_relation.cpp'
  ,'join_relation.cpp'
  ,'limit_relation.cpp'
  ,'order_relation.cpp'
  ,'update_relation.cpp'
  ,'projection_relation.cpp'
  ,'query_relation.cpp'
  ,'read_csv_relation.cpp'
  ,'read_json_relation.cpp'
  ,'setop_relation.cpp'
  ,'subquery_relation.cpp'
  ,'table_function_relation.cpp'
  ,'table_relation.cpp'
  ,'value_relation.cpp'
  ,'materialized_relation.cpp'
  ,'view_relation.cpp'
  ,'write_parquet_relation.cpp'
  ,'write_csv_relation.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_main_relation = static_library('duckdb_main_relation'
  ,duckdb_main_relation_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_main_relation.extract_all_objects()

