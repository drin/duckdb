
# ------------------------------
# Headers and Sources

# Sources
duckdb_transformer_constraint_sources = [
   'transform_constraint.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_transformer_constraint = static_library('duckdb_transformer_constraint'
  ,duckdb_transformer_constraint_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_transformer_constraint.extract_all_objects()

