
# ------------------------------
# Headers and Sources

# Sources
duckdb_common_operators_sources = [
   'cast_operators.cpp'
  ,'convert_to_string.cpp'
  ,'string_cast.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_common_operators = static_library('duckdb_common_operators'
  ,duckdb_common_operators_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_common_operators.extract_all_objects()

