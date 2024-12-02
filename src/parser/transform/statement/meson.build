
# ------------------------------
# Headers and Sources

# Sources
duckdb_transformer_statement_sources = [
   'transform_alter_table.cpp'
  ,'transform_attach.cpp'
  ,'transform_detach.cpp'
  ,'transform_call.cpp'
  ,'transform_checkpoint.cpp'
  ,'transform_create_function.cpp'
  ,'transform_comment_on.cpp'
  ,'transform_copy.cpp'
  ,'transform_copy_database.cpp'
  ,'transform_create_table_as.cpp'
  ,'transform_create_index.cpp'
  ,'transform_create_schema.cpp'
  ,'transform_create_table.cpp'
  ,'transform_create_view.cpp'
  ,'transform_create_type.cpp'
  ,'transform_delete.cpp'
  ,'transform_explain.cpp'
  ,'transform_export.cpp'
  ,'transform_drop.cpp'
  ,'transform_import.cpp'
  ,'transform_insert.cpp'
  ,'transform_load.cpp'
  ,'transform_pragma.cpp'
  ,'transform_rename.cpp'
  ,'transform_secret.cpp'
  ,'transform_select.cpp'
  ,'transform_select_node.cpp'
  ,'transform_set.cpp'
  ,'transform_pivot_stmt.cpp'
  ,'transform_prepare.cpp'
  ,'transform_show.cpp'
  ,'transform_show_select.cpp'
  ,'transform_transaction.cpp'
  ,'transform_update.cpp'
  ,'transform_upsert.cpp'
  ,'transform_use.cpp'
  ,'transform_create_sequence.cpp'
  ,'transform_vacuum.cpp'
  ,'transform_alter_sequence.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_transformer_statement = static_library('duckdb_transformer_statement'
  ,duckdb_transformer_statement_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_transformer_statement.extract_all_objects()

