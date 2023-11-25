#!/bin/bash

dpap monitor memory ah E3

function param_usage

#echo -e "\e[4m\e[lm\e[1;34mMonitor and generate program resource utilization\e[om\n\e[lm\e[1;33mUsage Instructions:\e[om\nüsa echo -e "\e[4m\e[lm\e[1;34mMonitor and generate program resource utilization\e[0m\n\e[lm\e[1;33mUsage Instructions: \e[0m\nUsage: $0 [Arguments] [or] -help\n\e[lm\e[1;32mAvailable Arguments:\e[0m \n\t-stats_dir \t [Value] (Mandatory param) Specify parent path to store stats e.g. '/dpap/public/kafka/data/stats' \n\t -program \t [Value] (Optional param) Program name to monitor the utilization \n\t -filterl \t [Value] (Optional param)

Filter keyword 1 to select specific jobs\n\t-filter2 \t (Value) (Optional param) Filter keyword 2 to select specific jobs\n\t-delay \t [Value] (Optional param) Delay interval to extract utilization

stats in secs [Default : 5] \n\t -onerun \t\t (Optional param) Flag to stop monitoring the program after first funn

memStats()

PARAMI-$1

PARAM2-$2

PGM-$13:-/dpap/public/kat cer/p hon/scripts/dpap quartz main.py)

DELAY-S $(4:-5)

ROCESS- ps -ef | grep -i "$(PGM)" "| egrep -i "${ ${PARAM1)" | egrep -i "$(PARAM2)" | tail -1' PRO if [ (PROCESS)"

then

TOT MEM-S (grep -i 'MemTotal:' /proc/memi eminfo | awk '{print $2)') CPU S STATS-1scpu | egrep Thread! d]^Core|^Socket|^CP

SOCK CKTS=$(echo $CPU STATS | grep grep -oP'(?<=Socket\ (s\)) [ cket\ (s\)) [^0-9]*\K([0-9]+)')

CPS-$ (echo $CPU ST STATS| grep -op'(?<-Core\(\))[^0-9] -9]*\K([0-9]+)) TPC-$ (echo $SCPU STATS | grep -OP(?<-Thread\ (s\)) [^0-9]*\K 0-9]*\K([0-9]+)')

LCPU-$ (echo "$(SOCKTS)*$(CPS)*S(TPC)" | bc)
