
# ------------------------------
# Headers and Sources

# Sources
duckdb_function_map_sources = [
   'map_contains.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_function_map = static_library('duckdb_function_map'
  ,duckdb_function_map_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_function_map.extract_all_objects()

