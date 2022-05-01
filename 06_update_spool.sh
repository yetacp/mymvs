#!/bin/bash

timeinterval=5;
prtfolder="./prt"
chksum1=""
while [[ true ]]; do
    chksum2=`find $prtfolder -type f -printf "%T@ %p\n" | md5sum | cut -d " " -f 1`;
    if [[ $chksum1 != $chksum2 ]] ; then 
        echo "Updating spool... [$chksum2]";
        rm -f spool/*.prt
        python3 jobsplit.py
        chksum1=$chksum2
    fi
    sleep $timeinterval;
done
