# -*- coding: utf-8 -*-


# def async_run(): # TODO
    # {
    #     eval "$@" &>/dev/null
    # } &


# db_echo() {
#     # report data and errors in scripting
#     #    - SET_DEBUG is set to '1' to report errors
#     #    - use log_toggle() to include file logging
#     # using stream 2 (stderr)

#     if [[ $SET_DEBUG == '1' ]]; then
#         warn "debug info ($(date "+%D %T")) - $@" >&2
#     fi
#     # printf "%b\n" "${cyan:-}dotnet-install:${normal:-} $1" >&3
# }
# die() {
#     # exit program with $exit_code ($1) and optional $message ($2)
#     # https://stackoverflow.com/questions/7868818/in-bash-is-there-an-equivalent-of-die-error-msg/7869065

#     warn "${2:-script} died...${USAGE:-}" >&2
#     db_echo "${MAIN:-}line ${BLUE:-}${BASH_LINENO[0]}${MAIN:-} of ${ATTN:-}${FUNCNAME[1]}${MAIN:-} in ${BASH_SOURCE[1]}${MAIN:-}." >&2
#     [[ ! "$DONT_DIE" == '1' ]] && exit "${1:1}"
# }
# yes_no() {
#     # Accept a Yes/no (default Yes) user response to prompt ($1 or default)
#     echo -n "${1:-'[Yes/no]: '}"
#     read yno
#     case $yno in
#     [nN] | [n | N][O | o])
#         return 1
#         ;;
#     *) # default 'Yes' ... see function no_yes for default 'No'
#         return 0
#         ;;
#     esac
# }
# no_yes() {
#     # Accept a yes/No (default No) user response to prompt ($1 or default)
#     echo -n "${1:-'[No/yes]: '}"
#     read yno
#     case $yno in
#     [yY] | [yY][Ee][Ss])
#         return 1
#         ;;
#     *) # default 'No' ... see function yes_no for default 'Yes'
#         return 0
#         ;;
#     esac
# }
# exit_usage() {
#     # Print script usage and exit
#     # TODO replace with die()
#     # Parameters:
#     #   $1 - specific message (e.g. 'file not found')
#     #   $2 - optional usage text
#     die "$@"
# }
# print_usage() {
#     set_man_page
#     echo "$MAN_PAGE"
# }
# #* ######################## program logging functions
# log_toggle() {
#     #   usage: log_toggle [filename]
#     #   toggle on and off logging to file
#     #       parameter
#     #           filename    - name of new logfile (default LOGFILE)
#     #       variable $LOG stores state
#     #       variable $LOGFILE stores filename
#     #   reference: https://unix.stackexchange.com/questions/80988/how-to-stop-redirection-in-bash

#     # set default log filename or $1
#     if [[ -z "$1" ]]; then
#         if [[ -z "$LOG_FILE_NAME" ]]; then
#             LOG_FILE_NAME="${script_source:-'./'}LOGFILE.log"
#         fi
#     else
#         LOG_FILE_NAME="${1}"
#     fi
#     touch "$LOG_FILE_NAME"
#     # if log is on, turn it off
#     if [[ "$LOG" == '1' ]]; then
#         LOG='0'
#         exec 1>&4- 2>&5-
#         attn "logging off ..."
#     else # if it is off ... turn it on
#         LOG='1'
#         exec 4>&1 5>&2
#         # log to the filename stored in $LOG_FILE_NAME
#         db_echo "\${LOG_FILE_NAME}: ${LOG_FILE_NAME}"
#         exec > >(tee -a -i "${LOG_FILE_NAME}") 2>&1
#         attn "logging on ..."
#     fi
# }
# test_echo() {
#     # log the current value of a given variable ($1)
#     # usage: test_echo <test name> <test code>
#     # report test results if:
#     #    - SET_DEBUG is set to '1' or cli [test] option set
#     #    - use log_toggle() to include file logging
#     if [[ $SET_DEBUG == '1' ]] && [[ -n "$1" ]]; then
#         printf "%bFunction Test -> %bPID %s %b" "$MAIN" "$CANARY" "$$" "$GO"
#         printf '%(%Y-%m-%d)T' -1
#         printf "%b test name: %s\n%b" "$ATTN" "$1" "${RESET_FG:-}"
#         shift
#         eval "$@"
#         printf "%bResult = %s%b\n" "$COOL" "$?" "${RESET_FG:-}"
#     fi
# }
# test_var() {
#     # usage: test_var <test variable>
#     # report test results if:
#     #    - SET_DEBUG is set to '1' or cli [test] option set
#     #    - use log_toggle() to include file logging
#     # reference:
#     #   indirect variables: https://wiki.bash-hackers.org/syntax/pe#indirection
#     #   bash printf: https://www.linuxjournal.com/content/bashs-built-printf-function
#     if [[ $SET_DEBUG == '1' ]] && [[ -n "$1" ]]; then
#         local testvar="${1}"
#         echo "\$testvar: $testvar"
#         echo "testvar: " ${!testvar}
#         echo ''
#         printf "%bVariable Test -> %bPID %s %b" "$MAIN" "$CANARY" "$$" "$GO"
#         printf '%(%Y-%m-%d)T' -1
#         printf "%b %15s -%b %s %b\n" "$ATTN" "\$$testvar" "$WARN" "$testvar" "$RESET_FG"
#     fi
# }
# log_flag() {
#     rain "#? ############################################################################"
# }
# #* ######################## path manipulation functions
# real_name() {
#     # TODO test this further ... working on a bash only method
#     # test_var "$1"
#     # log_flag
#     filename="${!1}"
#     filename="${1##*/}"
#     echo $filename
# }
# parse_filename() {
#     #   usage: parse_filename [filename]
#     #   parameter
#     #       filename    - $1 or global $filename used
#     #   returns
#     #       base_name   - file name only (no path)
#     #       dir         - path only
#     #       name_only   - name without extension
#     #       extension   - file extension or '' if none

#     [[ -z "$filename" ]] && filename="$1"
#     if [[ -r "$1" ]]; then
#         exit_usage "\$filename not readable ..." "${MAIN:-}${FUNCNAME[0]} ${WHITE:-}[filename]"

#         base_name="${filename##*/}"
#         # Strip longest match of */ from start
#         dir="${filename:0:${#filename}-${#base_name}}"
#         # Substring from 0 thru pos of filename
#         name_only="${base_name%.[^.]*}"
#         # Strip shortest match of . plus at least one non-dot char from end
#         extension="${base_name:${#name_only}+1}"
#         # Substring from len of base thru end
#         if [[ -z "$name_only" && -n "$extension" ]]; then
#             # If we have an extension and no base, it's really the base
#             name_only="$extension"
#             extension=""
#         fi
#     fi
#     test_var "$filename"
#     log_flag

# }
# get_safe_new_filename() {
#     # usage: get_safe_new_filename filename /path/to/file [extension]
#     #   returns
#     #       $new_safe_name      - new file name WITH path and extension
#     #       $new_safe_name_only - new file name (no path / ext)
#     #   eliminates duplicates by adding integers to filename as needed
#     #   (e.g. file_2, file_3 ...)
#     if [[ "$#" > 1 ]]; then
#         safe_name="$1"
#         safe_path="$2"
#         [[ -z "$3" ]] && safe_ext='' || safe_ext=".$3"
#         new_safe_name="${safe_path}/${safe_name}${safe_ext}"
#         declare -i i=2
#         while [ -f "$new_safe_name" ]; do
#             new_safe_name="${safe_path}/${safe_name}_${i}${safe_ext}"
#             i=$((i + 1))
#         done
#         new_safe_name_only="${safe_name}_${i}"
#     else
#         exit_usage "Invalid parameters ..." "usage: ${MAIN}get_safe_new_filename ${WHITE}filename /path/to/file [extension]"
#     fi
# }
# #* ######################## file manipulation functions

# hex_dump() { [[ -r "$1" ]] && od -A x -t x1z -v "$1"; }
# url_encode() {
#     [[ -z "$1" ]] && return 64
#     encoded=$(php -r "echo rawurlencode('$1');") && return 0 || return "$EX_DATAERR"
# }
# url_decode() {
#     [[ -z "$1" ]] && return 1
#     decoded=$(php -r "echo rawurldecode('$1');") && return 0 || return "$EX_DATAERR"
# }
# #* ######################## paramter handling

# parse_options() {
#     # parse basic options [help|test|usage|version] & SET_DEBUG
#     # TODO the 'exits' and lack of shifts make this function inadequate
#     # TODO use standard functions in a wrapper instead
#     case "$1" in
#     -h | --help | help)
#         set_man_page
#         echo "$MAN_PAGE"
#         return
#         # exit 0
#         ;;
#     -t | --test | test)
#         [[ ! "$SET_DEBUG" == '1' ]] && _run_tests
#         return
#         # exit 0
#         ;;
#     -u | --usage | usage)
#         me "$USAGE"
#         return
#         # exit 0
#         ;;
#     -v | --version | version)
#         ce "${MAIN}${NAME}${WHITE} (version ${VERSION})${RESET_FG}"
#         return
#         # exit 0
#         ;;
#         # *) ;;
#     esac
# }

# #* ######################## error handling
# _set_traps() {
#     cur_opts="$-"
#     debug_opts="axET"
#     set "-${cur_opts}${debug_opts}"
# }

# _trap_error() {
#     # me "ERR: $ERR"
#     # set "-${cur_opts}"
#     return 0
# }
# _trap_debug() {
#     return 0
#     # ce "Script source:$MAIN $BASH_SOURCE$RESET_FG $@ \n"
#     # attn "echo VARIABLE ($VARIABLE) is being used here."
# }
# _trap_exit() {
#     # https://stackoverflow.com/a/50270940/9878098
#     exitcode=$?
#     printf 'error executing script...\n' 1>&2
#     printf 'exit code returned: %s\n' "$exitcode"
#     printf 'the command executing at the time of the error was: %s\n' "$BASH_COMMAND"
#     printf 'command present on line: %d' "${BASH_LINENO[0]}"
#     # Some more clean up code can be added here before exiting
#     set "-${cur_opts}"
#     exec 4>&- 5>&- 6>&-
#     if [[ "$LOG" == '1' ]]; then
#         LOG='0'
#         exec 1>&4 2>&5
#         exec 4>&- 5>&-
#         attn "logging off ..."
#     fi

#     exit $exitcode
# }
# #* ######################## script tests
# _run_tests() {
#     _run_debug_config() {
#         green "\$dotfiles_path is set to $dotfiles_path."
#         green "\$here is set to as $here."
#     }
#     _bt_color_sample_test() {
#         echo -e "${MAIN}C ${WARN}O ${COOL}L ${GO}O ${CHERRY}R   ${CANARY}T ${ATTN}E ${PURPLE}S ${RESET_FG}T"
#         echo -e "${MAIN}MAIN   ${WARN}WARN   ${COOL}COOL   ${GO}GO   ${CHERRY}CHERRY   ${CANARY}CANARY   ${ATTN}ATTN   ${RAIN}RAIN   ${RESET_FG}RESET_FG"
#     }
#     _test_standard_script_modules() {
#         _EXIT_USAGE_TEXT="${MAIN}${script_name}${WHITE} - macOS script"
#         # log file for test sesssion
#         LOG_FILE_NAME="${script_source}ssm_debug_test.log"
#         # functions that include an 'exit' will skip it so tests can continue
#         DONT_DIE='1'
#         # log everything to LOG_FILE_NAME
#         log_toggle

#         ce "${COOL}BASH_SOURCE:$MAIN $BASH_SOURCE$RESET_FG"
#         log_flag

#         test_var "$script_name"
#         test_var "$script_source"
#         test_var "$SET_DEBUG"
#         test_var "$DONT_DIE"
#         test_var "$LOG"
#         test_var "$LOG_FILE_NAME"

#         # TODO add tests for these functions as needed
#         test_echo "die() test" "die 'die test!'"
#         test_echo "db_echo() test" "db_echo 'This is the test argument'"
#         test_echo "urlencode() test" "url_encode 'http://www.github.com/skeptycal'"
#         db_echo "$encoded"
#         test_echo "urlencode() test" "url_decode 'http%3A%2F%2Fwww.github.com%2Fskeptycal'"
#         db_echo "$decoded"
#         fake_filename="$LOG_FILE_NAME"
#         test_var "$fake_filename"
#         test_echo "real_name() test" "real_name $fake_filename"

#         log_flag
#         result="${fake_filename##*/}"
#         test_var "$result"

#         # cleanup test environment
#         log_toggle
#         unset DONT_DIE
#         unset LOG_FILE_NAME
#         unset _EXIT_USAGE_TEXT
#         unset LOG
#     }
#     ce "Script source:$MAIN $BASH_SOURCE$RESET_FG"
#     _run_debug_config
#     _bt_color_sample_test
#     _test_standard_script_modules
#     return 0
# }
# #* ######################## main loop
# _main_standard_script_modules() {
#     # _debug_function_header
#     [[ $SET_DEBUG == 1 ]] && _set_traps
#     parse_options "$@"
#     [[ $SET_DEBUG == 1 ]] && _run_tests
#     # declare -f
# }

# #* ######################## entry point
# # echo ${filename##*/}
# # ce "Script source:$MAIN ${BASH_SOURCE[0]##*/}${RESET_FG:-}\n"
# # ce "Script parent:$MAIN ${BASH_SOURCE[1]##*/}${RESET_FG:-}\n"
# # ce "Script grandparent:$MAIN ${BASH_SOURCE[2]##*/}${RESET_FG:-}\n"

# trap _trap_error ERR
# # trap _trap_exit EXIT
# # trap _trap_debug DEBUG

# _main_standard_script_modules "$@"

# # generate a function list
# declare -F | sed "s/declare -fx //g" >ssm_functions.txt


# def main():
#     # debug info
#     print (__file__)
#     print (sys.argv[0])

# #? ############################################################################
# # References

# # determine if a function exists
# # https://stackoverflow.com/questions/85880/determine-if-a-function-exists-in-bash

# # url encoding
# # https://stackoverflow.com/questions/296536/how-to-urlencode-data-for-curl-command

# # parameter expansions for file and path names
# # identify this actual script name and current directory path
# # _self=${0##*/}
# # parameter expansion to remove trailing /filename
# # _path="${0%/*}"

# # printf and echo
# # https://unix.stackexchange.com/questions/65803/why-is-printf-better-than-echo

# # arguments in bash
# # https://stackoverflow.com/questions/255898/how-to-iterate-over-arguments-in-a-bash-script

# """

# """ list of functions from .functions dotfile
# a
# allopen
# anybar
# anyguard
# async_run
# attn
# azure_agent
# bak
# blue
# br
# brew_fix
# canary
# cdf
# ce
# check_file
# cherry
# chmod_all
# clip
# dataurl
# datelog
# db_echo
# die
# diff
# digga
# dist_hook
# exit_usage
# fileop
# find_broken
# fix_list
# fs
# gdv
# get_current_os_name
# get_linux_platform_name
# get_safe_new_filename
# get_template
# getcertnames
# gfg
# ggf
# ggfl
# ggl
# ggp
# ggpnp
# ggu
# git_com
# git_one
# green
# gz
# hex_dump
# iterm2_begin_osc
# iterm2_end_osc
# iterm2_print_state_data
# iterm2_print_user_vars
# iterm2_print_version_number
# iterm2_prompt_mark
# iterm2_prompt_prefix
# iterm2_prompt_suffix
# iterm2_set_user_var
# l
# lns
# log_flag
# log_toggle
# lt
# main
# main_aliases
# main_exports
# me
# mkd
# new
# no_yes
# nonzero_return
# o
# parse_filename
# parse_git_branch
# parse_git_dirty
# parse_options
# phpserver
# pk
# prettier_here
# pretty
# print_usage
# prompt_OFF
# prompt_off
# prompt_on
# prompt_tag
# purple
# pyver
# rain
# readlinkf
# real_name
# run_debug_aliases
# run_debug_exports
# server
# set_man_page
# setup_tools
# source_file
# targz
# test_echo
# test_var
# travis_trigger
# tre
# tree_html
# trw
# tt
# url_decode
# url_encode
# versions
# warn
# web_chmod
# white
# yes_no
# """
