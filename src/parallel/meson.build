# ------------------------------
# Headers and Sources

# Headers are all in the root build definition (`meson.build`)

# Sources
parallel_sources = [
   'base_pipeline_event.cpp'
  ,'meta_pipeline.cpp'
  ,'executor_task.cpp'
  ,'executor.cpp'
  ,'event.cpp'
  ,'interrupt.cpp'
  ,'pipeline.cpp'
  ,'pipeline_complete_event.cpp'
  ,'pipeline_event.cpp'
  ,'pipeline_executor.cpp'
  ,'pipeline_finish_event.cpp'
  ,'pipeline_initialize_event.cpp'
  ,'pipeline_prepare_finish_event.cpp'
  ,'task_executor.cpp'
  ,'task_scheduler.cpp'
  ,'thread_context.cpp'
]


# ------------------------------
# Build artifacts (libraries)

# An object library (only its objects will be linked against)
objlib_duckdb_parallel = static_library('duckdb_parallel'
  ,parallel_sources
  ,include_directories: [ libduckdb_inc ]
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_parallel.extract_all_objects()

