#!/usr/bin/env python

# ------------------------------
# Overview

"""
This is a one-off or adhoc script that was written to make it easier to convert ~110
CMakeLists.txt files to meson.build files. A huge majority of these files are very simple
and the transformation is straight-forward (use of `static_library`, `subdir`,
`include_directories`). For the few that are much more complicated, this script should
print "please check" and the path to the file that contains anything not straightforward
(`include_directories` is also considered not straightforward).

Even though this script was written adhoc, it seems reasonable to keep it around for
posterity and just in case I need it in the future.
"""

# >> Dependencies
import os
import sys
import re

from enum import Enum
from dataclasses import dataclass


# >> Variables
pattern_subdir     = r'add_subdirectory[(](.*)[)]'
pattern_addlib     = r'add_library(?:_unity)?[(]'
pattern_addlib_end = r'.cpp\s*[)]\s*$'
pattern_appobj     = r'set[(]ALL_OBJECT_FILES'
pattern_appobj_end = r'PARENT_SCOPE[)]'


meson_template_sourcelist = '''
# ------------------------------
# Headers and Sources

# Sources
{lib_name}_sources = [
   {src_list}
]
'''

meson_header_targets = '''
# ------------------------------
# Build targets and artifacts
'''

meson_template_subdirs = '''
# >> Artifacts from subdirectories
{subdirs}
'''

meson_template_objlib = '''
# >> Artifacts from this directory
# An object library (only its objects will be linked against)
objlib_{lib_name} = static_library('{lib_name}'
  ,{lib_name}_sources
  ,build_by_default: false
  ,install         : false
)

# Accumulate the object files for the final library target
duck_objfiles += objlib_{lib_name}.extract_all_objects()

'''


# >> Classes

# enum classes for parsing
class State(Enum):
    SUBDIR        = 1
    SRCLIST       = 2
    SRCLIST_STOP  = 3
    OBJLIB        = 4
    OBJLIB_STOP   = 5
    OTHER         = 6
    ERROR         = 7


# data classes for build commands
@dataclass
class Subdir:
    subdir_name: str

    def ToMeson(self):
        return f'subdir({self.subdir_name})'

@dataclass
class ObjLib:
    lib_name: str
    src_list: list[str]

    def ToMesonSourceList(self):
        return meson_template_sourcelist.format(
             lib_name=self.lib_name
            ,src_list='\n  ,'.join([f"'{src_name}'" for src_name in self.src_list])
        )

    def ToMesonObjLib(self):
        return meson_template_objlib.format(lib_name=self.lib_name)

@dataclass
class BuildDef:
    file_path      : str
    commands_subdir: list[Subdir]
    command_objlib : ObjLib

    def ToMesonSubdirs(self):
        return '\n'.join([cmd_subdir.ToMeson() for cmd_subdir in self.commands_subdir])

    def ToMeson(self) -> str:
        meson_builddef  = ''

        if self.command_objlib is not None:
            meson_builddef += self.command_objlib.ToMesonSourceList()

        meson_builddef += f'\n{meson_header_targets}'
        meson_builddef += (
              '\n'
            + meson_template_subdirs.format(subdirs=self.ToMesonSubdirs())
        )

        if self.command_objlib is not None:
            meson_builddef += self.command_objlib.ToMesonObjLib()

        return meson_builddef


# >> Functions

# Matchers for parsing state machine
def MatchSubdir(build_cmd: str) -> State:
    re_match = re.fullmatch(pattern_subdir, build_cmd)

    if re_match is None: return State.OTHER
    return State.SUBDIR

def MatchSourceList(build_cmd: str, prev_state: State) -> State:
    re_match_start = re.match(pattern_addlib, build_cmd)
    re_match_stop  = re.search(pattern_addlib_end, build_cmd)

    if re_match_stop is not None:
        return State.SRCLIST_STOP

    elif re_match_start is None and prev_state.value != State.SRCLIST.value:
        return State.OTHER

    return State.SRCLIST

def MatchObjLib(build_cmd: str, prev_state: State) -> State:
    re_match_start = re.match(pattern_appobj    , build_cmd)
    re_match_stop  = re.search(pattern_appobj_end, build_cmd)

    if re_match_stop is not None:
        return State.OBJLIB_STOP

    elif re_match_start is None and prev_state.value != State.OBJLIB.value:
        return State.OTHER

    return State.OBJLIB


# Builders for parts of a build definition
def BuildCommandSubdir(build_cmd: str) -> Subdir | None:
    re_match = re.fullmatch(pattern_subdir, build_cmd)

    if re_match is None: return
    return Subdir(re_match.group(1))

def BuildCommandObjLib(build_srclist: list[str]) -> ObjLib | None:
    for src_ndx in range(len(build_srclist)):
        if build_srclist[src_ndx] == 'OBJECT':
            objlib_name = build_srclist[src_ndx - 1]

            if objlib_name.startswith('add_library'):
                split_pos = objlib_name.find('(')
                objlib_name = objlib_name[split_pos + 1:]

            break

    # Remove the closing parenthesis from the last line
    build_srclist[-1] = build_srclist[-1].rstrip(')')

    return ObjLib(objlib_name, build_srclist[src_ndx + 1:])


def ExtractCmakeBuild(build_fpath):
    command_objlib  = None
    commands_subdir = []
    other_commands  = []

    src_list    = None
    parse_state = None
    with open(build_fpath, 'r') as build_handle:
        for build_line in build_handle:
            build_line = build_line.strip()
            if not build_line: continue

            # Check if it's a subdir command
            parse_state = MatchSubdir(build_line)
            if parse_state.value == State.SUBDIR.value:
                commands_subdir.append(BuildCommandSubdir(build_line))
                continue

            # Check if it's an object library target
            parse_state = MatchSourceList(build_line, parse_state)
            if parse_state.value == State.SRCLIST.value:
                src_list = build_line.split()

                try:
                    build_line = next(build_handle).strip()
                    parse_state = MatchSourceList(build_line, parse_state)

                    # Consume lines until we hit the end of `add_library`
                    while parse_state.value != State.SRCLIST_STOP.value:
                        src_list.extend(build_line.split())
                        build_line = next(build_handle).strip()
                        parse_state = MatchSourceList(build_line, parse_state)

                except StopIteration:
                    pass

            if parse_state.value == State.SRCLIST_STOP.value:
                if src_list is None: src_list = build_line.split()
                else               : src_list.extend(build_line.split())

                command_objlib = BuildCommandObjLib(src_list)
                if command_objlib is None: return

                # Reset state and go to next iteration
                # parse_state will get overwritten later
                src_list = None
                continue

            # Check if it's gathering object library artifacts
            parse_state = MatchObjLib(build_line, parse_state)
            if (   parse_state.value == State.OBJLIB.value
                or parse_state.value == State.OBJLIB_STOP.value):
                try:
                    build_line  = next(build_handle).strip()
                    parse_state = MatchObjLib(build_line, parse_state)

                    while parse_state.value != State.OBJLIB_STOP.value:
                        build_line  = next(build_handle).strip()
                        parse_state = MatchObjLib(build_line, parse_state)

                except StopIteration:
                    pass

                finally:
                    if parse_state.value == State.OBJLIB_STOP.value: continue

            # If nothing else matched, just propagate for now
            if parse_state.value == State.OTHER.value:
                other_commands.append(build_line)

    if len(other_commands) > 0:
        print(f'please check: {build_fpath}')
        # print(other_commands)

    return BuildDef(build_fpath, commands_subdir, command_objlib)


# >> Main
if __name__ == '__main__':
    if not os.path.isfile('todo-files.txt'):
        sys.exit(
            'Please create "todo-files.txt" containing '
            'a list of file paths to be converted. '
            'Each line should contain a single, plain file path.'
        )

    with open('todo-files.txt', 'r') as todo_handle:
        files_to_transform = todo_handle.read().split()

    for file_ndx, meson_fpath in enumerate(files_to_transform):
        build_def = ExtractCmakeBuild(meson_fpath)

        if build_def is None: continue

        # print(meson_fpath)
        # print(build_def.ToMeson())
        with open(meson_fpath, 'w') as meson_handle:
            meson_handle.write(build_def.ToMeson())

