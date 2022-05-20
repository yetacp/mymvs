#!/bin/bash
# System dependent
HERCHOST=127.0.0.1
HERCPORT=3505
RDRPREP=./rdrprep/rdrprep
echo "Installing application..."
${RDRPREP} $1 tmp.jcl_E
echo "Installing files..."
nc -w1 ${HERCHOST} ${HERCPORT} < tmp.jcl_E
