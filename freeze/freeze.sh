#!/bin/sh

BASE_BINARY=StaticTVBase

if [ ! -f $BASE_BINARY ]
then
  BASE_BINARY="$BASE_BINARY".exe
fi

python FreezePython.py --base-binary $BASE_BINARY --install-dir=bin/ ../test.py
