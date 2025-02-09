#!/bin/bash
# Coverage Script

coverage run --source=src -m pytest tests
coverage report -m
