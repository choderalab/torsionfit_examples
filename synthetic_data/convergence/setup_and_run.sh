#!/usr/bin/env bash

# Parameters for toy model
RJ=True
PHASE=False
CONT=False
INIT=(1_10_180)
TRUE=(2_10_180)

CONDITION='rj'

CHUNKS=(0 1 2 3 4 5 6 7 8 9)

mkdir $CONDITION
cd $CONDITION

for C in ${CHUNKS[*]}; do
    mkdir ${CONDITION}_${C}
    cd ${CONDITION}_${C}
    sed "s/REPLACE/-rj $RJ -p $PHASE -c $CONT -i $INIT -t $TRUE/" ../../submit_dummy > submit
    qsub submit
    cd ../
done