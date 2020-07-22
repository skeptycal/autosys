#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
    # shellcheck shell=bash
    # shellcheck source=/dev/null
    # shellcheck disable=2016,2086,2230

. $(which ssm)
declare -g PREVIOUS_URL
PREVIOUS_URL=''


getURL() {
    # copy URL from active tab of Google Chrome to macOS clipboard
    if [[ $OS = 'darwin' ]]; then
        # set <url> to active Chrome tab url
        url=$(osascript -e 'tell application "Google Chrome" to return URL of active tab of front window')

        # copy to clipboard
        printf "%s" "$url" | pbcopy

        # -v is verbose : if -v ... print url to stdout in addition
        [ "$1" = '-q' ] || printf "%s\n" "$url"
    fi
    }

ping_avg() {
    usage="$0 [-h] | [COUNT URL]"
    case $1 in
        '-h'|'--help'|'help')
            me $usage
            exit
            ;;
        *)
            # extract the average ping time (ms) from 'ping' output
            # $1 = number of pings to average
            count=$1

            # $2 = url to test
            # remove schema and folders
            url_short=$(echo "$2" | cut -d '/' -f 3)

            # ww
            ping -c "$count" "$url_short" | tail -n 1 | cut -d '/' -f 6
            ;;
    esac
    }

log_urls() {
    declare -g usage="log_urls [COUNT] [SLEEP_TIME] [URL_LOG]"

    if [ "$1" = '-h' ]; then
        ce "$usage"
    else
        # number of repeats for average ping measurement - default 2
        declare -g count=${1:-2}

        # time to sleep between checks                   - default 10s
        declare -g sleep_time=${2:-10}

        # location of log file                           - default ~/.url_log.log
        declare -g url_log=${3:-~/.url_log.log}

        # shellcheck disable=SC2078 # ignore constant expression  `while [ : ]`
        while [ : ]
        do
            # get url of Chrome active tab
            declare -g url=$(osascript -e 'tell application "Google Chrome" to return URL of active tab of front window')

            #TODO - check if url = PREVIOUS_URL ... to keep down the spam
            if [[ $url = "$PREVIOUS_URL" ]]; then
                true #TODO do stuff if $url is the same ...
            else
                PREVIOUS_URL=$url
            fi

            # remove schema and folders
            declare -g url_short=$(echo "$url" | cut -d '/' -f 3)

            # comparison site
            # comp="www.example.com"
            # comp="www.google.com"
            # comp="192.168.1.100"
            declare -g comp="skeptycal.com"

            # test ping of site
            # ping -c "$count" "$url_short" | tail -n 1 | cut -d '/' -f 6

            me "$(date), $url, $(ping_avg $count $url), $(ping_avg $count $comp)" >&2

            # log to $url_log
            printf "%s\n" "$(date), $url, $(ping_avg $count $url), $(ping_avg $count $comp)" >>$url_log

            sleep $sleep_time
        done
    fi
    unset url_short count comp sleep_time
}

