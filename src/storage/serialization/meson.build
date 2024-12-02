
# ------------------------------
# Headers and Sources

# Sources
duckdb_storage_serialization_sources = [
   'serialize_constraint.cpp'
  ,'serialize_create_info.cpp'
  ,'serialize_dependency.cpp'
  ,'serialize_expression.cpp'
  ,'serialize_extension_install_info.cpp'
  ,'serialize_extra_drop_info.cpp'
  ,'serialize_logical_operator.cpp'
  ,'serialize_macro_function.cpp'
  ,'serialize_nodes.cpp'
  ,'serialize_parsed_expression.cpp'
  ,'serialize_parse_info.cpp'
  ,'serialize_query_node.cpp'
  ,'serialize_result_modifier.cpp'
  ,'serialize_statement.cpp'
  ,'serialize_table_filter.cpp'
  ,'serialize_tableref.cpp'
  ,'serialize_types.cpp'
  ,'serialize_storage.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_storage_serialization = static_library('duckdb_storage_serialization'
  ,duckdb_storage_serialization_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_storage_serialization.extract_all_objects()

