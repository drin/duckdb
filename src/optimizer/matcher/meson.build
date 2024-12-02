# ------------------------------
# Headers and Sources

# Sources
optimizer_matcher_sources = [
  'expression_matcher.cpp'
]


# ------------------------------
# Build artifacts (libraries)

# An object library (only its objects will be linked against)
objlib_duckdb_optimizer_matcher = static_library('duckdb_optimizer_matcher'
  ,optimizer_matcher_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_optimizer_matcher.extract_all_objects()

