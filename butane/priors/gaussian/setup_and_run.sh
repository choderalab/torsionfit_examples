#!/usr/bin/env bash

# Hyperparameters for Gaussian prior
TAU=(0.001 0.01 0.1 1.0 10 100 1000 10000)
REPEATS=(0 1 2 3 4 5 6 7 8 9)
DB=Gaussian_tau
SAMPLES=10000
RJ=True
for T in ${TAU[*]}; do
    mkdir tau_${T}
    cd tau_${T}
    for C in ${REPEATS[*]}; do
        mkdir tau_${T}_${C}
        cd tau_${T}_${C}
        DBNAME=tau_${T}_${C}
        sed "s/REPLACE/-rj $RJ -d ${DBNAME}.sqlite -i $SAMPLES -tau $T -r $C/" ../../submit_dummy > submit
        #qsub submit
        python ../../run_sampler.py -rj $RJ -d ${DBNAME}.sqlite -i $SAMPLES -t $T -r $C
        cd ../
     done
     cd ../
done
