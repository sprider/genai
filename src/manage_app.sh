#!/bin/bash

APP_BASE_PATH=/opt/apps/gen-ai
PYTHON_INTERPRETER=/opt/apps/gen-ai/.venv/bin/python3
USAGE="app ... [Usage: $0 { start | restart } OR $0 { stop | status }]"

get_PID() {
    if [ `uname -s` = 'Linux' ]; then
        pslist=`/bin/ps -elf | grep 'app.py'`
    elif [ `uname -s` = 'FreeBSD' ]; then
        pslist=`/bin/ps ajxw | grep 'app.py'`
    else
        pslist=`/bin/ps -ef | grep 'app.py'`
    fi

    if [ `uname -s` = 'Linux' ]; then
        PID=`echo "$pslist" | grep -v grep | awk '{ print $4 }'`
    else
        PID=`echo "$pslist" | grep -v grep | awk '{ print $2 }'`
    fi
}

stop_process () {
    get_PID
    if [ ! -z "$PID" ]; then
        echo "app ... [attempting to stop the app with PID(s): $PID.]"
        /bin/kill ${PID} > /dev/null 2>&1
        echo "app ... [stopped]"
    else
        echo "app ... [no running app processes.]"
    fi
}

status_process () {
    get_PID
    if [ ! -z "$PID" ]; then
        echo "app ... [process(es) running with PID(s): $PID.]"
    else
        echo "app ... [no running app processes.]"
    fi
}

start_process () {
    get_PID
    if [ ! -z "$PID" ]
    then
        echo "app ... [app process(es) already running with PID(s): $PID.]"
    else
        nohup $PYTHON_INTERPRETER $APP_BASE_PATH/app.py > /dev/null 2>&1 &
        echo "app ... [started]"
    fi
}

restart_process () {
    stop_process
    sleep 1
    start_process
}

case "$1" in
'start')
    start_process
    ;;
'status')
    status_process
    ;;
'stop')
    stop_process
    ;;
'restart')
    restart_process
    ;;
*)
    echo $USAGE
    ;;
esac
