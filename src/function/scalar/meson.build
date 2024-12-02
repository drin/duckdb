# ------------------------------
# Headers and Sources

# Sources
func_scalar_sources = [
   'compressed_materialization_utils.cpp'
  ,'create_sort_key.cpp'
  ,'strftime_format.cpp'
  ,'nested_functions.cpp'
  ,'pragma_functions.cpp'
]


# ------------------------------
# Build artifacts (libraries)

# >> Artifacts from subdirectories
subdir('compressed_materialization')
subdir('date')
subdir('generic')
subdir('list')
subdir('map')
subdir('operator')
subdir('sequence')
subdir('string')
subdir('struct')
subdir('system')

# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_func_scalar = static_library('duckdb_func_scalar'
  ,func_scalar_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_func_scalar.extract_all_objects()

