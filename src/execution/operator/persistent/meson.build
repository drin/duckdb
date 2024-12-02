
# ------------------------------
# Headers and Sources

# Sources
duckdb_operator_persistent_sources = [
   'csv_rejects_table.cpp'
  ,'physical_batch_copy_to_file.cpp'
  ,'physical_batch_insert.cpp'
  ,'physical_copy_database.cpp'
  ,'physical_copy_to_file.cpp'
  ,'physical_delete.cpp'
  ,'physical_export.cpp'
  ,'physical_insert.cpp'
  ,'physical_update.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_operator_persistent = static_library('duckdb_operator_persistent'
  ,duckdb_operator_persistent_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_operator_persistent.extract_all_objects()

