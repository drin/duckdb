
# ------------------------------
# Headers and Sources

# Sources
duckdb_transformer_helpers_sources = [
   'transform_alias.cpp'
  ,'transform_cte.cpp'
  ,'transform_groupby.cpp'
  ,'transform_orderby.cpp'
  ,'transform_sample.cpp'
  ,'transform_typename.cpp'
  ,'nodetype_to_string.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_transformer_helpers = static_library('duckdb_transformer_helpers'
  ,duckdb_transformer_helpers_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_transformer_helpers.extract_all_objects()

