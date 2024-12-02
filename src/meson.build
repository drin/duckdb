# ------------------------------
# Build targets (internal libraries, e.g. "object libraries")

# >> Include targets
libduckdb_inc += [include_directories('include')]

# TODO: enable unity build

# A list of object files for final duckdb target
duck_objfiles = []

subdir('transaction')
subdir('parallel')


# ------------------------------
# Build artifacts (executables and final libraries)

# TODO: add artifact for unity build

libduckdb = library('duckdb'
  ,include_directories: [libduckdb_inc, ep_inc]
  ,objects            : duck_objfiles
  ,install_rpath      : get_option('prefix') / get_option('libdir')
  ,install            : true
)

duckdb_bin = executable('duckdb'
  ,include_directories: [libduckdb_inc, ep_inc]
  ,dependencies       : [libduckdb]
  ,install_rpath      : get_option('prefix') / get_option('bindir')
  ,install            : true
)

