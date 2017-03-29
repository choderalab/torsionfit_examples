#!/usr/bin/env bash

# Parameters for toy model
RJ=True
DB=random

SAMPLES='100000'

REPEATS=(20 21 22 23 24 25 26 27 28 29)

mkdir $SAMPLES
cd $SAMPLES

for C in ${REPEATS[*]}; do
    mkdir ${DB}_${SAMPLES}_${C}
    cd ${DB}_${SAMPLES}_${C}
    DBNAME=${DB}_${SAMPLES}_${C}
    sed "s/REPLACE/-rj $RJ -d ${DBNAME}.sqlite -i $SAMPLES/" ../../submit_dummy > submit
    qsub submit
    cd ../
done