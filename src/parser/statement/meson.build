
# ------------------------------
# Headers and Sources

# Sources
duckdb_statement_sources = [
   'alter_statement.cpp'
  ,'attach_statement.cpp'
  ,'call_statement.cpp'
  ,'copy_statement.cpp'
  ,'copy_database_statement.cpp'
  ,'create_statement.cpp'
  ,'detach_statement.cpp'
  ,'delete_statement.cpp'
  ,'drop_statement.cpp'
  ,'execute_statement.cpp'
  ,'explain_statement.cpp'
  ,'export_statement.cpp'
  ,'extension_statement.cpp'
  ,'insert_statement.cpp'
  ,'load_statement.cpp'
  ,'multi_statement.cpp'
  ,'pragma_statement.cpp'
  ,'prepare_statement.cpp'
  ,'relation_statement.cpp'
  ,'select_statement.cpp'
  ,'set_statement.cpp'
  ,'transaction_statement.cpp'
  ,'update_statement.cpp'
  ,'update_extensions_statement.cpp'
  ,'vacuum_statement.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_statement = static_library('duckdb_statement'
  ,duckdb_statement_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_statement.extract_all_objects()

