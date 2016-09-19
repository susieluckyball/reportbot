#!/bin/bash

mkdir -vp ${PREFIX}/bin;

touch requirements.txt;

${PYTHON} $RECIPE_DIR/setup.py install || exit 1;
