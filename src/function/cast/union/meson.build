# ------------------------------
# Headers and Sources

# Sources
union_cast_sources = [
  'from_struct.cpp'
]


# ------------------------------
# Build artifacts (libraries)

# An object library (only its objects will be linked against)
objlib_duckdb_union_cast = static_library('duckdb_union_cast'
  ,union_cast_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_union_cast.extract_all_objects()

