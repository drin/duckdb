# ------------------------------
# Headers and Sources

# Sources
func_pragma_sources = [
   'pragma_functions.cpp'
  ,'pragma_queries.cpp'
]


# ------------------------------
# Build artifacts (libraries)

# An object library (only its objects will be linked against)
objlib_duckdb_func_pragma = static_library('duckdb_func_pragma'
  ,func_pragma_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_func_pragma.extract_all_objects()

