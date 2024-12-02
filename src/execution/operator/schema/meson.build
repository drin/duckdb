
# ------------------------------
# Headers and Sources

# Sources
duckdb_operator_schema_sources = [
   'physical_alter.cpp'
  ,'physical_attach.cpp'
  ,'physical_create_art_index.cpp'
  ,'physical_create_schema.cpp'
  ,'physical_create_type.cpp'
  ,'physical_create_sequence.cpp'
  ,'physical_create_table.cpp'
  ,'physical_create_view.cpp'
  ,'physical_create_function.cpp'
  ,'physical_detach.cpp'
  ,'physical_drop.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_operator_schema = static_library('duckdb_operator_schema'
  ,duckdb_operator_schema_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_operator_schema.extract_all_objects()

