# ------------------------------
# Headers and Sources

# Sources
catalog_default_entries_sources = [
   'default_functions.cpp'
  ,'default_generator.cpp'
  ,'default_schemas.cpp'
  ,'default_table_functions.cpp'
  ,'default_types.cpp'
  ,'default_views.cpp'
]


# ------------------------------
# Build artifacts (libraries)

# An object library (only its objects will be linked against)
objlib_duckdb_catalog_default_entries = static_library('duckdb_catalog_default_entries'
  ,catalog_default_entries_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_catalog_default_entries.extract_all_objects()

