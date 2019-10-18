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

export SPOTIPY_CLIENT_ID="f90cbc0d6e2341ccb0c22848a27517ca"
export SPOTIPY_CLIENT_SECRET="9c12de9367334e2eb6cd4c594c2e3bd1"
export SPOTIPY_REDIRECT_URI="https://localhost:8888/callback/"

if [ ! -d $VENV ]; then
    #pip3 install virtualenv
    virtualenv --python python3.6 $VENV
fi

$VENV/bin/pip install \
              -r $SCRIPT_HOME/requirements.txt

$VENV/bin/python3 inference.py