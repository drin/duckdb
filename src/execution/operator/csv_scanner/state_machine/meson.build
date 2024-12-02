
# ------------------------------
# Headers and Sources

# Sources
duckdb_csv_state_machine_sources = [
   'csv_state_machine.cpp'
  ,'csv_state_machine_cache.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_csv_state_machine = static_library('duckdb_csv_state_machine'
  ,duckdb_csv_state_machine_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_csv_state_machine.extract_all_objects()

