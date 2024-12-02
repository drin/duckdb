# TODO: need to do an alternate way of dynamically resolving extensions

# ------------------------------
# Convenience variables

# NOTE: ep_dirpath defined in top-level build file (meson.build)
# NOTE: codegen_dirpath defined in top-level build definition (meson.build)

generated_hdr_path = codegen_dirpath / 'include' / 'generated_extension_headers.hpp'
generated_src_path = codegen_dirpath / 'src'     / 'generated_extension_loader.cpp'

ext_inc = []


# ------------------------------
# Conditional build args

# >> Variables to gather build arguments into
ext_buildargs = ['-Wno-exit-time-destructors', '-DGENERATED_EXTENSION_HEADERS=1']
ext_linkargs  = []

# >> Flags to set now for adding to build arguments later
is_apple_static = false

if get_option('DISABLE_EXTENSION_LOAD')
  ext_buildargs += '-DDUCKDB_DISABLE_EXTENSION_LOAD'
endif

# Check if there are extensions we should test loading of
if get_option('TEST_WITH_LOADABLE_EXTENSION') != ''
  ext_testlist    = get_option('TEST_WITH_LOADABLE_EXTENSION').split(';')
  ext_load_optval = ext_testlist.join(',')

  # add extra commas for easier substring matching in C++
  ext_buildargs += '-DDUCKDB_EXTENSIONS_TEST_WITH_LOADABLE=",@ext_load_optval@,"'
  ext_buildargs += '-DDUCKDB_EXTENSIONS_BUILD_PATH="@extension_builddir@"'
endif

# Check if we should propagate an extension to test installation of
if get_option('TEST_REMOTE_INSTALL') != ''
  ext_buildargs += (
    '-DDUCKDB_TEST_REMOTE_INSTALL="' + get_option('TEST_REMOTE_INSTALL') + '"'
  )
endif

if get_option('WASM_LOADABLE_EXTENSIONS').enabled()
  ext_buildargs += [ '-sSIDE_MODULE=1', '-DWASM_LOADABLE_EXTENSIONS' ]

elif get_option('EXTENSION_STATIC_BUILD')
  if cmp_name == 'gcc' or cmp_name == 'clang'
    if sys_name == 'darwin'
      is_apple_static = true

      ext_buildargs += ['-fvisibility=hidden']

    # NOTE: duckdb has a separate block for z/OS, but meson doesn't have builtin support
    else
      ext_buildargs += ['-fvisibility=hidden']
      ext_linkargs  += ['-Wl,--gc-sections', '-Wl,--exclude-libs,ALL']

    endif

  elif sys_name != 'windows'
    error('EXTENSION_STATIC_BUILD only supported for macos, linux, and windows (MSVC)')

  endif

# NOTE: this is the common case (for me)
elif cmp_name == 'clang' and sys_name == 'darwin'
  extra_linkargs += [ '-undefined dynamic_lookup' ]

endif


# ------------------------------
# Code generation (constructing the content to be substituted into template files)

# >> An array of extensions to statically link (`get_statically_linked_extensions`)
exts_static_link = []

if duckopt_link_exts
  # if linking builtin extensions is not disabled, statically link all extensions
  exts_static_link = get_option('DUCKDB_EXTENSION_NAMES')

elif not get_option('GENERATE_EXTENSION_ENTRIES')
  # if not statically linking or generating, maybe link core_functions
  exts_static_link = []

  foreach ext_name : get_option('DUCKDB_EXTENSION_NAMES')
    if ext_name == 'core_functions'
      exts_static_link += 'core_functions'
    endif
  endforeach

endif

# >> Generate the code to substitute into templated files
exthdr_includes = [] # `include` directives for generated_extension_headers.hpp
extloader_names = [] # names for extension loader
extloader_body  = '' # code to substitute in generated_extension_loader.cpp

foreach ext_name : exts_static_link
  duckext_subproject = subproject(ext_name)

  if is_apple_static
    ext_linkargs += [
       '-Wl,-dead-strip'
      ,'-Wl,-exported_symbol,_@ext_name@_init'
      ,'-Wl,-exported_symbol,_@ext_name@_version'
      ,'-Wl,-exported_symbol,_@ext_name@_storage_ini*'
    ]
  endif

  # >> Access build targets from subproject
  duckext_includes = duckext_subproject.get_variable('@ext_name@_ext_inc')
  duckext_loadlib  = duckext_subproject.get_variable(

  # >> Generate code to link extension
  ext_name = ext_name.to_upper()

  # Accumulate include directives for extension header
  exthdr_includes += f'#include "@ext_name@_extension.hpp"'

  # Accumulate names for extension loader
  extloader_names += f'\n        "@ext_name@"'

  # Accumulate code blocks to load duckdb extension
  ext_name_camel = ''
  foreach ext_nameword : ext_name.split('_')
    ext_name_camel += ext_nameword.substring(0, 1).to_upper()
    ext_name_camel += ext_nameword.substring(1).to_lower()
  endforeach

  # this is the code block we accumulate into `TryLoadLinkedExtension()`
  extloader_body += (
      f'\n    if (extension == "@ext_name@") {'
    + f'\n        db.LoadStaticExtension<@ext_name_camel@Extension>();'
    +  '\n        return true;'
    +  '\n    }\n'
  )

  # Add build arg signifying the extension was linked
  ext_buildargs += f'DUCKDB_EXTENSION_@ext_name@_LINKED=1'

  # add dynamic include targets
endforeach

# >> test paths for extensions whose SQLLogicTests need to be registered
ext_testpaths = []

foreach ext_name : get_option('DUCKDB_EXTENSION_NAMES')
  ext_name = ext_name.to_upper()
  string(TOUPPER ${EXT_NAME} EXT_NAME_UPPERCASE)

  if(${DUCKDB_EXTENSION_${EXT_NAME_UPPERCASE}_LOAD_TESTS})
    ext_tpathopt = f'DUCKDB_EXTENSION_@ext_name@_TEST_PATH'
    ext_tpathval = get_option(ext_tpathopt)
    ext_testpaths += f'\n        "@ext_tpathval@"'
  endif
endforeach


# ------------------------------
# Headers and Sources

# NOTE: cpp_compiler defined in top-level build definition (meson.build)

# >> Define generator for extension header and source

bin_python = find_program('python3')


# >> Headers

# To link extensions into DuckDB and auto-load them on startup, we generated an
# include file and a loader function based on the `DUCKDB_EXTENSION_NAMES`
# parameter.

# A generated cpp header file for an extension
generated_cpphdr = configure_file(
  ,input        : 'generated_extension_headers.hpp.in'
  ,output       : generated_hdr_path
  ,configuration: { 'EXT_HEADER_INCLUDES': exthdr_includes.join('\n') }
)


# >> Sources

# non-generated sources
main_extension_sources = [
   'extension_alias.cpp'
  ,'extension_helper.cpp'
  ,'extension_install.cpp'
  ,'extension_load.cpp'
  ,'extension_util.cpp'
]

# generated sources
generated_cppsrc = configure_file(
   input        : 'generated_extension_loader.cpp.in'
  ,output       : generated_src_path
  ,configuration: {
     'EXT_LOADER_BODY'            : extloader_body
    ,'EXT_NAME_VECTOR_INITIALIZER': extloader_names.join(',')
    ,'EXT_TEST_PATH_INITIALIZER'  : ext_testpaths.join(',')

)


# ------------------------------
# Build targets

# >> Known include targets
ext_inc += [
   include_directories(extension_dirpath)
  ,include_directories(codegen_dirpath / 'include')
  ,include_directories(ep_dirpath      / 'httplib')
]

# >> Library targets
# An object library (only its objects will be linked against)
objlib_duckdb_main_extension = static_library('duckdb_main_extension'
  ,main_extension_sources
  ,include_directories: [ libduckdb_inc, ext_inc ]
  ,cpp_args           : ext_buildargs
  ,build_by_default   : false
  ,install            : false
)

# An object library (only its objects will be linked against)
objlib_duckdb_ext_loader = static_library('duckdb_generated_ext_loader'
  ,generated_cppsrc
  ,include_directories: [ libduckdb_inc, ext_inc ]
  ,cpp_args           : ext_buildargs
  ,build_by_default   : false
  ,install            : false
)


# ------------------------------
# Final targets

# Accumulate the object files for the final library target
duck_objfiles += objlib_duckdb_main_extension.extract_all_objects()

# Accumulate the extension loader object files too
duck_objfiles += objlib_duckdb_ext_loader.extract_all_objects()

