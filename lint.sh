#!/bin/bash

for i in shang
do
    echo "Checking: $i"
    pylint --rcfile=pylint.rc $i
    pep8 --repeat --ignore=E501,E128,E124 --exclude='migrations' $i
done
