
# ------------------------------
# Headers and Sources

# Sources
duckdb_progress_bar_sources = [
   'progress_bar.cpp'
  ,'terminal_progress_bar_display.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories


# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_progress_bar = static_library('duckdb_progress_bar'
  ,duckdb_progress_bar_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_progress_bar.extract_all_objects()

