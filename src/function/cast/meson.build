# ------------------------------
# Headers and Sources

# Sources
func_cast_sources = [
   'array_casts.cpp'
  ,'blob_cast.cpp'
  ,'bit_cast.cpp'
  ,'cast_function_set.cpp'
  ,'decimal_cast.cpp'
  ,'default_casts.cpp'
  ,'enum_casts.cpp'
  ,'list_casts.cpp'
  ,'map_cast.cpp'
  ,'numeric_casts.cpp'
  ,'pointer_cast.cpp'
  ,'string_cast.cpp'
  ,'struct_cast.cpp'
  ,'time_casts.cpp'
  ,'union_casts.cpp'
  ,'uuid_casts.cpp'
  ,'varint_casts.cpp'
  ,'vector_cast_helpers.cpp'
]


# ------------------------------
# Build artifacts (libraries)

# >> Artifacts from subdirectories
subdir('union')

# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_func_cast = static_library('duckdb_func_cast'
  ,func_cast_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_func_cast.extract_all_objects()

