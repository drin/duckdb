# ------------------------------
# Headers and Sources

# Sources
catalog_entries_sources = [
   'copy_function_catalog_entry.cpp'
  ,'duck_index_entry.cpp'
  ,'duck_schema_entry.cpp'
  ,'duck_table_entry.cpp'
  ,'type_catalog_entry.cpp'
  ,'index_catalog_entry.cpp'
  ,'macro_catalog_entry.cpp'
  ,'pragma_function_catalog_entry.cpp'
  ,'schema_catalog_entry.cpp'
  ,'sequence_catalog_entry.cpp'
  ,'table_catalog_entry.cpp'
  ,'column_dependency_manager.cpp'
  ,'scalar_function_catalog_entry.cpp'
  ,'table_function_catalog_entry.cpp'
  ,'view_catalog_entry.cpp'
]


# ------------------------------
# Build artifacts (libraries)

# >> Artifacts from subdirectories
subdir('dependency')

# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_catalog_entries = static_library('duckdb_catalog_entries'
  ,catalog_entries_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_catalog_entries.extract_all_objects()

