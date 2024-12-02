# ------------------------------
# Headers and Sources

# Headers are all in the root build definition (`meson.build`)

# Sources
transaction_sources = [
   'duck_transaction_manager.cpp'
  ,'duck_transaction.cpp'
  ,'meta_transaction.cpp'
  ,'undo_buffer_allocator.cpp'
  ,'undo_buffer.cpp'
  ,'transaction_context.cpp'
  ,'transaction.cpp'
  ,'transaction_manager.cpp'
  ,'commit_state.cpp'
  ,'rollback_state.cpp'
  ,'cleanup_state.cpp'
  ,'wal_write_state.cpp'
]


# ------------------------------
# Build artifacts (libraries)

# An object library (only its objects will be linked against)
objlib_duckdb_transaction = static_library('duckdb_transaction'
  ,transaction_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_transaction.extract_all_objects()

