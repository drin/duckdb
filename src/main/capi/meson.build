
# ------------------------------
# Headers and Sources

# Sources
duckdb_main_capi_sources = [
   'aggregate_function-c.cpp'
  ,'appender-c.cpp'
  ,'arrow-c.cpp'
  ,'cast_function-c.cpp'
  ,'config-c.cpp'
  ,'data_chunk-c.cpp'
  ,'datetime-c.cpp'
  ,'duckdb-c.cpp'
  ,'duckdb_value-c.cpp'
  ,'helper-c.cpp'
  ,'hugeint-c.cpp'
  ,'logical_types-c.cpp'
  ,'pending-c.cpp'
  ,'prepared-c.cpp'
  ,'profiling_info-c.cpp'
  ,'replacement_scan-c.cpp'
  ,'result-c.cpp'
  ,'scalar_function-c.cpp'
  ,'stream-c.cpp'
  ,'table_function-c.cpp'
  ,'table_description-c.cpp'
  ,'threading-c.cpp'
  ,'value-c.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories
subdir(cast)

# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_main_capi = static_library('duckdb_main_capi'
  ,duckdb_main_capi_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_main_capi.extract_all_objects()

