#!/bin/bash
MAX_TEMP=100.0

while :
do
	ctemp=`vcgencmd measure_temp | cut -d = -f2 | cut -d \' -f1`
	ftemp=`echo "$ctemp * 1.8 + 32" | bc -l`
	echo $ftemp
	if (( `echo $ftemp'>'$MAX_TEMP | bc` )); then
		echo above
		say temerature is now $ftemp
	fi
	sleep 3
done
