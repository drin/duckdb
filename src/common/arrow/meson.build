
# ------------------------------
# Headers and Sources

# Sources
duckdb_common_arrow_sources = [
   'arrow_appender.cpp'
  ,'arrow_converter.cpp'
  ,'arrow_util.cpp'
  ,'arrow_merge_event.cpp'
  ,'arrow_query_result.cpp'
  ,'arrow_wrapper.cpp'
  ,'physical_arrow_collector.cpp'
  ,'physical_arrow_batch_collector.cpp'
  ,'schema_metadata.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories
subdir(appender)

# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_common_arrow = static_library('duckdb_common_arrow'
  ,duckdb_common_arrow_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_common_arrow.extract_all_objects()

