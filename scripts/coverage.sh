#!/bin/bash
# coverage.sh
# Script to run tests and generate code coverage report

pytest --maxfail=1 --disable-warnings -q
coverage run -m pytest
coverage report -m
