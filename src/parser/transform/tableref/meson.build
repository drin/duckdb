
# ------------------------------
# Headers and Sources

# Sources
duckdb_transformer_tableref_sources = [
   'transform_base_tableref.cpp'
  ,'transform_join.cpp'
  ,'transform_from.cpp'
  ,'transform_pivot.cpp'
  ,'transform_subquery.cpp'
  ,'transform_table_function.cpp'
  ,'transform_tableref.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_transformer_tableref = static_library('duckdb_transformer_tableref'
  ,duckdb_transformer_tableref_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_transformer_tableref.extract_all_objects()

