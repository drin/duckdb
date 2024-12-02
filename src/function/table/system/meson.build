
# ------------------------------
# Headers and Sources

# Sources
duckdb_table_func_system_sources = [
   'duckdb_columns.cpp'
  ,'duckdb_constraints.cpp'
  ,'duckdb_databases.cpp'
  ,'duckdb_dependencies.cpp'
  ,'duckdb_extensions.cpp'
  ,'duckdb_functions.cpp'
  ,'duckdb_keywords.cpp'
  ,'duckdb_indexes.cpp'
  ,'duckdb_memory.cpp'
  ,'duckdb_optimizers.cpp'
  ,'duckdb_schemas.cpp'
  ,'duckdb_secrets.cpp'
  ,'duckdb_which_secret.cpp'
  ,'duckdb_sequences.cpp'
  ,'duckdb_settings.cpp'
  ,'duckdb_tables.cpp'
  ,'duckdb_temporary_files.cpp'
  ,'duckdb_types.cpp'
  ,'duckdb_variables.cpp'
  ,'duckdb_views.cpp'
  ,'pragma_collations.cpp'
  ,'pragma_database_size.cpp'
  ,'pragma_metadata_info.cpp'
  ,'pragma_storage_info.cpp'
  ,'pragma_table_info.cpp'
  ,'pragma_user_agent.cpp'
  ,'test_all_types.cpp'
  ,'test_vector_types.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_table_func_system = static_library('duckdb_table_func_system'
  ,duckdb_table_func_system_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_table_func_system.extract_all_objects()

