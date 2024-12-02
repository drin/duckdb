# ------------------------------
# Headers and Sources

# Sources
duckdb_parser_sources = [
   'base_expression.cpp'
  ,'column_definition.cpp'
  ,'column_list.cpp'
  ,'constraint.cpp'
  ,'expression_util.cpp'
  ,'keyword_helper.cpp'
  ,'parsed_expression.cpp'
  ,'parsed_expression_iterator.cpp'
  ,'parser.cpp'
  ,'qualified_name.cpp'
  ,'query_error_context.cpp'
  ,'query_node.cpp'
  ,'result_modifier.cpp'
  ,'tableref.cpp'
  ,'transformer.cpp'
]


# ------------------------------
# Build targets and artifacts

# >> Include targets
# NOTE: ep_dirpath defined in top-level build file (meson.build)
parser_inc = [
   include_directories(ep_dirpath / 'libpg_query' / 'include')
  ,include_directories(ep_dirpath / 'libpg_query')
]

# >> Artifacts from subdirectories
subdir(constraints)
subdir(expression)
subdir(parsed_data)
subdir(query_node)
subdir(statement)
subdir(tableref)
subdir(transform)

# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_parser = static_library('duckdb_parser'
  ,duckdb_parser_sources
  ,include_directories: [ libduckdb_inc, parser_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_parser.extract_all_objects()

