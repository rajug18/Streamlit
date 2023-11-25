#!/bin/bash

#set-x

function param_usage

f

#echo -e "\e[4m\e[1m\e[1;34mMonitor and generate program resource utilization\e[om\n\e[1m\e[1;33mUsage Instructions:\e[em\nUsage: $0 [Arguments] [or] -help\n\e[1m\e[1;3 echo -e "\e[4m\e[1m\e[1;34mMonitor and generate program resource utilization\e[em\n\e[1m\e[1;33mUsage Instructions: \e[em\nUsage: $0 [Arguments] [or] -help\n\e[1m\e[1;32mAvailable Arguments:\e[em \n\t-stats_dir \t [Value] (Mandatory param) Specify parent path to store stats

e.g./dpap/public/kafka/data/stats \n\t-program \t [Value] (Optional param) Program name to monitor the utilization \n\t-filter1 \t [Value] (Optional param)

Filter keyword 1 to select specific jobs\n\t-filter2 \t [Value] (Optional param) Filter keyword 2 to select specific jobs\n\t-delay \t [Value] (Optional param) Delay interval to extract utilization stats in secs [Default: 5] \n\t-onerun \t\t (Optional param) Flag to stop monitoring the program after first run\n"

memStats() }

PARAM1-$1

PARAM2-$2

PGM-${3:-/dpap/public/kafka/app/producer/python/scripts/dpap_quartz_main.py}

DELAY-$(4:-5)

PROCESS ps-aef | grep -1 "$(PGM)" | egrep -i "${PARAM1}" | egrep -i "$(PARAM2)" | tail -1' if [ "${PROCESS}" - ""]

then

TOT MEM-$(grep -i 'MemTotal: /proc/meminfo | awk '{print $2}')

CPU STATS- Iscpu | egrep Thread|^Core|^Socket|^CPU\(" SOCKTS-$(echo $CPU_STATS | grep -OP (?<=Socket\(s\))[^0-9]*\K([0-9]+)')

CPS-$(echo $CPU STATS | grep -OP (?<-Core\(\))[^0-9]*\K([0-9]+)') TPC-S(echo $CPU_STATS | grep -OP(?<-Thread\(s\))[^0-9]*\K([0-9]+)')

LCPU-$(echo "$(SOCKTS} $(CPS)*${TPC)" | bc)

USER-$(echo "$(PROCESS}" | awk '{print $1}')

PID=$(echo "${PROCESS}" | awk '{print $2}')

PROGRAM-$(echo "${PROCESS)" | awk '{for (1-8; i<=NF;i++) printf("%s%s", $1, (i-end) ? "\n": OFS)}") echo "Hostname hostname"
