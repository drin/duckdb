
# ------------------------------
# Headers and Sources

# Sources
duckdb_arrow_conversion_sources = [
   'arrow_duck_schema.cpp'
  ,'arrow_array_scan_state.cpp'
  ,'arrow_type_info.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_arrow_conversion = static_library('duckdb_arrow_conversion'
  ,duckdb_arrow_conversion_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_arrow_conversion.extract_all_objects()

