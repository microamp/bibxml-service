#!/bin/bash

set -ex

pip install -r requirements-dev.txt
mypy --ignore-missing-imports --install-types --non-interactive --exclude docs .
