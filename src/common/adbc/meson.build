
# ------------------------------
# Headers and Sources

# Sources
duckdb_adbc_sources = [
   'adbc.cpp'
  ,'driver_manager.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories
subdir(nanoarrow)

# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_adbc = static_library('duckdb_adbc'
  ,duckdb_adbc_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_adbc.extract_all_objects()

