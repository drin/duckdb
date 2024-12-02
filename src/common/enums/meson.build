
# ------------------------------
# Headers and Sources

# Sources
duckdb_common_enums_sources = [
   'catalog_type.cpp'
  ,'compression_type.cpp'
  ,'date_part_specifier.cpp'
  ,'expression_type.cpp'
  ,'file_compression_type.cpp'
  ,'join_type.cpp'
  ,'logical_operator_type.cpp'
  ,'metric_type.cpp'
  ,'optimizer_type.cpp'
  ,'physical_operator_type.cpp'
  ,'statement_type.cpp'
  ,'relation_type.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_common_enums = static_library('duckdb_common_enums'
  ,duckdb_common_enums_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_common_enums.extract_all_objects()

