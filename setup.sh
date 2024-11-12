#!/usr/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $SCRIPT_DIR

rm -rf .venv
uv venv
uv pip install ./memsharded-conan
uv pip install dunamai==1.22.0

export CONAN_HOME=$SCRIPT_DIR/.conan2
$SCRIPT_DIR/.venv/bin/conan profile detect --force
