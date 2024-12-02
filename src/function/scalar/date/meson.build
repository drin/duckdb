
# ------------------------------
# Headers and Sources

# Sources
duckdb_func_date_sources = [
   'strftime.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_func_date = static_library('duckdb_func_date'
  ,duckdb_func_date_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_func_date.extract_all_objects()

