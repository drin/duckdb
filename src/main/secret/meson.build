
# ------------------------------
# Headers and Sources

# Sources
duckdb_main_secret_sources = [
   'secret.cpp'
  ,'secret_manager.cpp'
  ,'secret_storage.cpp'
  ,'default_secrets.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_main_secret = static_library('duckdb_main_secret'
  ,duckdb_main_secret_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_main_secret.extract_all_objects()

