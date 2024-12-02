
# ------------------------------
# Headers and Sources

# Sources
duckdb_constraints_sources = [
   'check_constraint.cpp'
  ,'not_null_constraint.cpp'
  ,'unique_constraint.cpp'
  ,'foreign_key_constraint.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_constraints = static_library('duckdb_constraints'
  ,duckdb_constraints_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_constraints.extract_all_objects()

