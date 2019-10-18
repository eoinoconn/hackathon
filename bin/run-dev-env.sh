#!/bin/bash

set -e
set -o pipefail

: ' Bash script to create enviornment and run django application.

Confidentiality and Proprietary Notice:
This document and/or code contains confidential and proprietary information of Jaguar Land Rover Limited.
Copyright 2018 (c) Jaguar Land Rover Limited. All rights reserved
'

SCRIPT_HOME=$(cd $(dirname $0)/.. ; pwd)
VENV=/tmp/emote-dev-env

if [ ! -d $VENV ]; then
    pip install virtualenv
    virtualenv --python python $VENV
fi

$VENV/bin/pip install \
              -r $SCRIPT_HOME/requirements.txt

$VENV/bin/python3 inference.py