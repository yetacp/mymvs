#!/bin/bash
# Wait to start x3270 terminals
sleep 15
xx=""
while [ "${xx}." = "." ];
do
  xx=`netstat -an | grep 3270 | grep tcp | grep LISTEN`
  if [ "${xx}." = "." ];
  then
    echo "Waiting 3270 port"
    sleep 5
  fi
done

# Start first TK4- console
# screen -t c3270A -S c3270A -p c3270A -d -m c3270 -scriptport 3271 127.0.0.1:3270
x3270 -model 3279-3 -iconname x3270 -scriptport 3271 127.0.0.1:3270 &
