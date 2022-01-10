#!/bin/bash -eu
#set -x

# create python virtual environment
[[ -d ./venv ]] || python -m venv ./venv

# activate python virtual environment
source venv/Scripts/activate || echo "couldn't find Windows activation"
source venv/bin/activate ||  echo "couldn't find Linux activation"

python -m pip install --upgrade pip

# install packages from requirements.txt
pip install -r requirements.txt

# source env file if it exists
[[ -f .env ]] && source .env

exit 0
