#! /usr/bin/env bash

# Run FastAPI web API via uvicorn ASGI Server

# PRODUCTION MODE
#uvicorn main:app

# DEBUG MODE
# Causes automatic reloading. TODO: See what other things --debug does
uvicorn main:app --debug

##
#
