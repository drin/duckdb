# ------------------------------
# Project Definition

# >> Define project info
project('libduckdb'
  ,'cpp'
  ,version         : '1.0.0.dev12057'
  ,meson_version   : '1.6.0'
  ,license         : 'Apache-2.0'
  ,license_files   : 'LICENSE'
  ,default_options : ['warning_level=3','cpp_std=c++17']
)

# >> Access platform information (system, environment, and application)
cpp_compiler = meson.get_compiler('cpp')

cpu_fam  = build_machine.cpu_family()
sys_name = build_machine.system()
cmp_name = cpp_compiler.get_id()

git_result = run_command('/usr/bin/env', 'git', 'log', '-1', '--format=%h', check: false)
if git_result.returncode() == 0
  git_commitid = git_result.stdout().strip()

else
  git_commitid = ''

endif

# >> Set project configuration

# project versioning
version_str = meson.project_version()

if get_option('DUCKDB_EXPLICIT_VERSION') != ''
  version_str = get_option('DUCKDB_EXPLICIT_VERSION')

endif

# >> Set build arguments

# Array of dynamic build arguments; eventually sent to the compiler
duck_buildargs = []

# platform-dependent build args
duck_wasmargs = []

# warnings only set for clang or apple clang (just check for darwin system)
if cmp_name == 'clang' or sys_name == 'darwin'
  add_project_arguments('-Wimplicit-int-conversion', language: 'cpp')
  add_project_arguments('-Wshorten-64-to-32'       , language: 'cpp')
  add_project_arguments('-Wnarrowing'              , language: 'cpp')
  add_project_arguments('-Wsign-conversion'        , language: 'cpp')
  add_project_arguments('-Wsign-compare'           , language: 'cpp')
  add_project_arguments('-Wconversion'             , language: 'cpp')

  # NOTE: certain object libs always disable warnings for exit time destructors
  # see: src/common/meson.build and any meson.build under src/common/types
  add_project_arguments('-Wexit-time-destructors'  , language: 'cpp')
endif


version_fields = version_str.split('.')
duckdb_cfgdata = configuration_data({
   'VERSION_STR'         : version_str
  ,'DUCKDB_MAJOR_VERSION': version_fields[0]
  ,'DUCKDB_MINOR_VERSION': version_fields[1]
  ,'DUCKDB_PATCH_VERSION': version_fields[2]
  ,'DUCKDB_DEV_ITERATION': version_fields[3]
  ,'DUCKDB_COMMIT_HASH'  : git_commitid
  ,'BUILD_IS_DEBUG'      : get_option('buildtype') == 'debug' ? 1 : 0
})


# ------------------------------
# Environmental information


# ------------------------------
# Reference paths

# base directory
cpp_srcdir      = 'src'
duck_tooldir    = 'tools'

extension_rootdir  = 'extension'
extension_dirpath  = meson.current_source_dir() / extension_rootdir
extension_builddir = meson.current_build_dir()  / extension_rootdir

codegen_rootdir = 'codegen'
codegen_dirpath = meson.current_source_dir() / codegen_rootdir

ep_rootdir = 'third_party'
ep_dirpath = meson.current_source_dir() / ep_rootdir


# ------------------------------
# Dependencies

# meson modules for resolving dependencies
pymod = import('python')

# project dependencies
libthreads = dependency('threads', required: true)

if not get_option('CLANG_TIDY')
  pymod.find_installation('python3')
endif


# ------------------------------
# Conditional build args

# >> Variables to determine how to build duckdb that derive from build options
# NOTE: these are used because meson does not allow mutating build options
duckopt_build_main = (
          get_option('BUILD_MAIN_DUCKDB_LIBRARY')
  and not get_option('BUILD_EXTENSIONS_ONLY')
  and not get_option('EXTENSION_CONFIG_BUILD')
)

duckopt_link_exts = (
      not get_option('DISABLE_BUILTIN_EXTENSIONS')
  and not get_option('GENERATE_EXTENSION_ENTRIES')
  and     get_option('BUILD_MAIN_DUCKDB_LIBRARY')
)

# The cmake version of this seems to have a bug
if get_option('EXTENSION_STATIC_BUILD')
  if cmp_name == 'gcc'
    duck_buildargs += [ '-ffunction-sections', '-fdata-sections' ]

  elif cmp_name == 'msvc' and sys_name == 'windows'
    duck_buildargs += ['/Gy']

  endif
endif

# Prepare for wasm things
if get_option('USE_WASM_THREADS')
  add_project_arguments('-pthread', language: 'c'  )
  add_project_arguments('-pthread', language: 'cpp')
  duck_wasmargs += [ '-pthread', '-sSHARED_MEMORY=1' ]
endif

# Coloring
if get_option('FORCE_COLORED_OUTPUT')
  if cmp_name == 'gcc'
    duck_buildargs += ['-fdiagnostics-color=always']

  elif cmp_name == 'clang'
    duck_buildargs += ['-fcolor-diagnostics']

  endif
endif

# 32-bit architecture?
if get_option('FORCE_32_BIT')

  # I'm not sure why duckdb wants i386 instead of x86
  if cpu_fam == 'x86_64' or cpu_fam == 'x86'
    duck_buildargs += ['-m32', '-DOS_ARCH=i386']

  else
    duck_buildargs += ['-m32']

  endif

else
  duck_buildargs += ['-DOS_ARCH=amd64']

endif

# OS name
if sys_name == 'darwin'
  duck_buildargs += ['-DOS_NAME=osx']

elif sys_name == 'windows'
  duck_buildargs += ['-DOS_NAME=windows']

elif sys_name == 'linux'
  duck_buildargs += ['-DOS_NAME=linux']

endif

# C++ exceptions
if get_option('EXPLICIT_EXCEPTIONS')
  duck_buildargs += ['-fexceptions']
endif


# >> Add conditional arguments to build
add_project_arguments(duck_buildargs, language: 'cpp')


# ------------------------------
# Build targets

# >> Include targets

# A list of internal include targets
libduckdb_inc = [ include_directories('.') ]

# A list of include targets for third party libs (external projects)
ep_inc = []


# >> Targets from subdirectories

# creates third-party targets
if not get_option('CLANG_TIDY')
  if get_option('BUILD_UNITTESTS')
    subdir('test')

    if get_option('BUILD_BENCHMARKS') and sys_name != 'windows' and sys_name != 'sunos'
      subdir('benchmark')
    endif
  endif

  if not get_option('EXTENSION_CONFIG_BUILD')
    # Add third-party libs to build
    subdir(ep_rootdir)
  endif
endif

# core targets
subdir(cpp_srcdir)
subdir(duck_tooldir)


# ------------------------------
# Package configurations

# use pkg-config to generate library build info
module_pkgcfg = import('pkgconfig')
module_pkgcfg.generate(libduckdb, subdirs: 'duckdb')


# ------------------------------
# Build artifacts (binaries)

# >> simple reader for Arrow files
readarrow_sources = [ cpp_tooldir  / 'read-arrow.cpp' ]

