
# ------------------------------
# Headers and Sources

# Sources
duckdb_main_capi_cast_sources = [
   'utils-c.cpp'
  ,'from_decimal-c.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_main_capi_cast = static_library('duckdb_main_capi_cast'
  ,duckdb_main_capi_cast_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_main_capi_cast.extract_all_objects()

