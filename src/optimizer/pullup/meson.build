# ------------------------------
# Headers and Sources

# Sources
optimizer_pullup_sources = [
   'pullup_filter.cpp'
  ,'pullup_projection.cpp'
  ,'pullup_from_left.cpp'
  ,'pullup_both_side.cpp'
  ,'pullup_set_operation.cpp'
]


# ------------------------------
# Build artifacts (libraries)

# An object library (only its objects will be linked against)
objlib_duckdb_optimizer_pullup = static_library('duckdb_optimizer_pullup'
  ,optimizer_pullup_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_optimizer_pullup.extract_all_objects()

