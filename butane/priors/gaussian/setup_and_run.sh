#!/usr/bin/env bash

# Hyperparameters for Gaussian prior
TAU=nuisance
REPEATS=(0 1 2 3 4 5 6 7 8 9 10 11 12 14 13 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 31 31 32 33 34 35 36 37 38 39)
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
        sed "s/REPLACE/-rj $RJ -d ${DBNAME}.sqlite -i $SAMPLES -r $C/" ../../submit_dummy > submit
        qsub submit
        #python ../../run_sampler.py -rj $RJ -d ${DBNAME}.sqlite -i $SAMPLES -t $T -r $C
        cd ../
     done
     cd ../
done
