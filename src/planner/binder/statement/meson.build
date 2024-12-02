# ------------------------------
# Headers and Sources

# Sources
bind_statement_sources = [
   'bind_attach.cpp'
  ,'bind_call.cpp'
  ,'bind_copy.cpp'
  ,'bind_copy_database.cpp'
  ,'bind_create.cpp'
  ,'bind_create_table.cpp'
  ,'bind_delete.cpp'
  ,'bind_detach.cpp'
  ,'bind_drop.cpp'
  ,'bind_execute.cpp'
  ,'bind_explain.cpp'
  ,'bind_export.cpp'
  ,'bind_extension.cpp'
  ,'bind_insert.cpp'
  ,'bind_load.cpp'
  ,'bind_logical_plan.cpp'
  ,'bind_pragma.cpp'
  ,'bind_prepare.cpp'
  ,'bind_relation.cpp'
  ,'bind_select.cpp'
  ,'bind_set.cpp'
  ,'bind_simple.cpp'
  ,'bind_summarize.cpp'
  ,'bind_update.cpp'
  ,'bind_update_extensions.cpp'
  ,'bind_vacuum.cpp'
]


# ------------------------------
# Build artifacts (libraries)

# An object library (only its objects will be linked against)
objlib_duckdb_bind_statement = static_library('duckdb_bind_statement'
  ,bind_statement_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_bind_statement.extract_all_objects()

