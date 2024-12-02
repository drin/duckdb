
# ------------------------------
# Headers and Sources

# Sources
duckdb_parser_tableref_sources = [
   'basetableref.cpp'
  ,'delimgetref.cpp'
  ,'emptytableref.cpp'
  ,'expressionlistref.cpp'
  ,'column_data_ref.cpp'
  ,'joinref.cpp'
  ,'pivotref.cpp'
  ,'showref.cpp'
  ,'subqueryref.cpp'
  ,'table_function.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_parser_tableref = static_library('duckdb_parser_tableref'
  ,duckdb_parser_tableref_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_parser_tableref.extract_all_objects()

