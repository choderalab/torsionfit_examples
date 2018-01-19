#!/usr/bin/env bash

DIH=($(ls -d */))
for D in ${DIH[*]}; do
    echo ${D}
    cd ${D}
    file=($(ls -d *.out))
    echo ${file}
    cat ${file} | grep "Optimization"
    cd ../
 done  

