#! /usr/bin/env bash

# Create virtualenv
python3 -m venv .venv

# Activate virtualenv
source .venv/bin/activate


# Now from within the active virtualenv

# Upgrade pip and setuptools as the virtualenv never seems
# to come with the latest versions.

# Upgrade pip.
python3 -m pip install --upgrade pip

# Upgrade setuptools.
python3 -m pip install --upgrade setuptools

# Install the project's required modules
pyhton3 -m pip install -r requirements.txt



##
#
