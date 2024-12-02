
# ------------------------------
# Headers and Sources

# Sources
duckdb_func_string_main_sources = [
   'caseconvert.cpp'
  ,'concat.cpp'
  ,'concat_ws.cpp'
  ,'length.cpp'
  ,'like.cpp'
  ,'md5.cpp'
  ,'nfc_normalize.cpp'
  ,'regexp.cpp'
  ,'substring.cpp'
  ,'prefix.cpp'
  ,'regexp_escape.cpp'
  ,'sha1.cpp'
  ,'sha256.cpp'
  ,'strip_accents.cpp'
  ,'string_split.cpp'
  ,'suffix.cpp'
  ,'contains.cpp'
]


# ------------------------------
# Build targets and artifacts


# >> Artifacts from subdirectories
subdir(regexp)

# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_duckdb_func_string_main = static_library('duckdb_func_string_main'
  ,duckdb_func_string_main_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_func_string_main.extract_all_objects()

