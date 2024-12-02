
# ------------------------------
# Headers and Sources

# Sources
duckdb_storage_statistics_sources = [
   'base_statistics.cpp'
  ,'column_statistics.cpp'
  ,'distinct_statistics.cpp'
  ,'array_stats.cpp'
  ,'list_stats.cpp'
  ,'numeric_stats.cpp'
  ,'segment_statistics.cpp'
  ,'string_stats.cpp'
  ,'struct_stats.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_storage_statistics = static_library('duckdb_storage_statistics'
  ,duckdb_storage_statistics_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_storage_statistics.extract_all_objects()

