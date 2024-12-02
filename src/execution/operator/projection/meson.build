
# ------------------------------
# Headers and Sources

# Sources
duckdb_operator_projection_sources = [
   'physical_projection.cpp'
  ,'physical_tableinout_function.cpp'
  ,'physical_pivot.cpp'
  ,'physical_unnest.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_operator_projection = static_library('duckdb_operator_projection'
  ,duckdb_operator_projection_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_operator_projection.extract_all_objects()

