#!/usr/bin/env bash

# Parameters for toy model
RJ=True
DB=from_rj

SAMPLES='10000'

REPEATS=(0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24)

mkdir from_rj_${SAMPLES}
cd from_rj_${SAMPLES}

for C in ${REPEATS[*]}; do
    mkdir ${DB}_${SAMPLES}_${C}
    cd ${DB}_${SAMPLES}_${C}
    DBNAME=${DB}_${SAMPLES}_${C}
    sed "s/REPLACE/-rj $RJ -d ${DBNAME}.sqlite -i $SAMPLES -r $C/" ../../submit_dummy > submit
    qsub submit
    cd ../
done