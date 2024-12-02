
# ------------------------------
# Headers and Sources

# Sources
duckdb_func_table_sources = [
   'arrow.cpp'
  ,'arrow_conversion.cpp'
  ,'checkpoint.cpp'
  ,'glob.cpp'
  ,'query_function.cpp'
  ,'range.cpp'
  ,'repeat.cpp'
  ,'repeat_row.cpp'
  ,'copy_csv.cpp'
  ,'read_csv.cpp'
  ,'sniff_csv.cpp'
  ,'read_file.cpp'
  ,'system_functions.cpp'
  ,'summary.cpp'
  ,'table_scan.cpp'
  ,'unnest.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories
subdir(system)
subdir(version)
subdir(arrow)

# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_func_table = static_library('duckdb_func_table'
  ,duckdb_func_table_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_func_table.extract_all_objects()

