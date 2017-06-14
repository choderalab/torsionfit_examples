#!/usr/bin/env bash

# Parameters for toy model
RJ=True
DB=c-c-c-c_all

SAMPLES='10000'

REPEATS=(0 1 2 3 4 5 6 7 8 9 10)

mkdir c-c-c-_all_${SAMPLES}
cd c-c-c-c_all_${SAMPLES}

for C in ${REPEATS[*]}; do
    mkdir ${DB}_${SAMPLES}_${C}
    cd ${DB}_${SAMPLES}_${C}
    DBNAME=${DB}_${SAMPLES}_${C}
    sed "s/REPLACE/-rj $RJ -d ${DBNAME}.sqlite -i $SAMPLES -r $C/" ../../submit_dummy > submit
    qsub submit
    cd ../
done