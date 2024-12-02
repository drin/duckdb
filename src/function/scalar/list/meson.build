
# ------------------------------
# Headers and Sources

# Sources
duckdb_func_list_nested_sources = [
   'contains_or_position.cpp'
  ,'list_extract.cpp'
  ,'list_resize.cpp'
  ,'list_zip.cpp'
  ,'list_select.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_func_list_nested = static_library('duckdb_func_list_nested'
  ,duckdb_func_list_nested_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_func_list_nested.extract_all_objects()

