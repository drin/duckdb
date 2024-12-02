# ------------------------------
# Headers and Sources

# Sources
catalog_sources = [
   'catalog_entry.cpp'
  ,'catalog_entry_retriever.cpp'
  ,'catalog.cpp'
  ,'catalog_search_path.cpp'
  ,'catalog_set.cpp'
  ,'catalog_catalog.cpp'
  ,'duck_catalog.cpp'
  ,'dependency_manager.cpp'
  ,'dependency_list.cpp'
  ,'dependency_catalog_set.cpp'
  ,'similar_catalog_entry.cpp'
]


# ------------------------------
# Build artifacts (libraries)

# >> Artifacts from subdirectories
subdir('catalog_entry')
subdir('default')

# NOTE: this doesn't seem to be referenced anywhere?
if not get_option('BUILD_CORE_FUNCTIONS_EXTENSION')
  add_project_arguments('-DDISABLE_CORE_FUNCTIONS_EXTENSION=1', language: 'cpp')
endif

# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_catalog = static_library('duckdb_catalog'
  ,catalog_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_catalog.extract_all_objects()

