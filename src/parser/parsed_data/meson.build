
# ------------------------------
# Headers and Sources

# Sources
duckdb_parsed_data_sources = [
   'alter_info.cpp'
  ,'alter_scalar_function_info.cpp'
  ,'alter_table_function_info.cpp'
  ,'alter_table_info.cpp'
  ,'attach_info.cpp'
  ,'comment_on_column_info.cpp'
  ,'copy_info.cpp'
  ,'create_info.cpp'
  ,'create_function_info.cpp'
  ,'create_index_info.cpp'
  ,'create_aggregate_function_info.cpp'
  ,'create_collation_info.cpp'
  ,'create_copy_function_info.cpp'
  ,'create_macro_info.cpp'
  ,'create_pragma_function_info.cpp'
  ,'create_secret_info.cpp'
  ,'create_sequence_info.cpp'
  ,'create_schema_info.cpp'
  ,'create_scalar_function_info.cpp'
  ,'create_table_function_info.cpp'
  ,'create_table_info.cpp'
  ,'create_type_info.cpp'
  ,'create_view_info.cpp'
  ,'detach_info.cpp'
  ,'drop_info.cpp'
  ,'exported_table_data.cpp'
  ,'extra_drop_info.cpp'
  ,'load_info.cpp'
  ,'sample_options.cpp'
  ,'parse_info.cpp'
  ,'transaction_info.cpp'
  ,'pragma_info.cpp'
  ,'vacuum_info.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_parsed_data = static_library('duckdb_parsed_data'
  ,duckdb_parsed_data_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_parsed_data.extract_all_objects()

