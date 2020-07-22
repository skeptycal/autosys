#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
    # shellcheck shell=bash
    # shellcheck source=/dev/null
    # shellcheck disable=2178,2128,2206,2034

    # profile start time
    t0=$(date "+%s.%n")

    # ssm - standard script modules
    . "$(command -v ssm)"
#* ##############################################################################
    #? ${PATH//:/\\n}    - replace all colons with newlines to display as a list
    #? ${PATH// /}       - strip all spaces
    #? ${VAR##*/}        - return only final element in path (program name)
    #? ${VAR%/*}         - return only path elements in path (without program name)


dprintf() {
    printf '%b' "$WARN"
    if [ -n "$1" ]; then
        printf ' -> %s' "$1"
        shift
    fi
    for arg in "$@"; do
        printf ' %s' "$arg"
    done
    printf '%s\n' ''
    }
_set_debug() {
    dprintf "SET_DEBUG =" "$SET_DEBUG" "Verbose debug mode enabled..."
    # setopt xtrace # verbose
    }
_end_timer() {
    # profile end time
    t1=$(date "+%s.%n")
    # display script time
    dt=$((t1-t0))
    printf '\n%bScript %s took %.3f seconds to load.\n\n' "$GO" "$0" "$dt"
    }

_get_repo_template() {
    #TODO This is a preset template directory - prefer github repo
    repo_template_location=~/Documents/coding/template
    repo_file_list=( README.md .gitignore LICENSE MANIFEST.in Pipfile setup.cfg setup.py )
    for f in $repo_file_list; do
        echo "cp -rf" "${repo_template_location}/${f}" "$repo_path"
    done


    # github repo template
    }
_config() {
    [[ $SET_DEBUG == 1 ]] && _set_debug "$@"
    SHELL_BIN="${SHELL##*/}" && export SHELL_BIN

    repo_path=$PWD
    dprintf "\$repo_path = $repo_path"
    repo_name=${PWD##*/}
    dprintf "\$repo_name = $repo_name"

    }

main() {
    SET_DEBUG=1
    br
    lime "**************************  Setup Github/Python repo **************************"
    _config "$@"
    _get_repo_template
    br

    ls $repo_template_location
    _end_timer
}

main "$@"
