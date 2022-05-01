#!/bin/bash
# set environment
export LANGUAGE=English

# create folders
mkdir -p backups dasd http log prt shadows

cd ./shadows
rm -f *
# recover RAMDISK
if [ -f ../dasd_shadows.tar.gz ]; then
  tar -xzf ../dasd_shadows.tar.gz
fi
cd ..

# Clean printed jobs and logs
rm ./prt/*.txt
rm ./log/*.log

# X3270 waits MVS3.8j
bash 05_listen_console.sh &

# Start Hercules console
export HERCULES_RC=scripts/ipl.rc
hercules -f conf/mymvs.cnf > log/hercules.log 
