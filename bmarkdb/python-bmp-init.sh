#! /usr/bin/env bash
###############################################################################
 
# Create the python virtual environment
python3 -m venv .venv

# Activate this venv in the current script/shell context.
# This context ends with this init script. You always need to do this step
# when starting a new shell/context for running/developing:
# Most IDEs detect python virtual environments and do this automatically.
source .venv/bin/activate

# Versions provided initally by venv command usually/always need upgrading
echo; echo "- - - - - - - -"
python3 -m pip install --upgrade pip
echo; echo "- - - - - - - -"
python3 -m pip install --upgrade setuptools

# This is for IDE (VSCode) and brings in a handful of dependencies
echo; echo "- - - - - - - -"
python3 -m pip install pylint

# Project modules
echo; echo "- - - - - - - -"
python3 -m pip install -r requirements.txt

echo; echo "- - - - - - - -"
echo 'Current set of python modules installed in this virtual environment:'
python3 -m pip freeze

echo

# FROM:
# https://pypi.org/project/bookmarks-parser/

##
#

