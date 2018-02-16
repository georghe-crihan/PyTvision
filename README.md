# PyTVison - Python bindings (through SWIG) for TurboVision by Salvador Tropea

Initial SWIG bindings are Copyright (C) 2004 Alex Novgorodov (drdivano).

Taken from: http://pytvision.sourceforge.net

Archive URL: https://sourceforge.net/projects/pytvision/files/pytvision/0.0.2/.

## DESCRIPTION

This is PyTVision - a set of Python bindings for Turbo Vision.

The distribution includes a version of Turbo Vision, with removed streams and
some other minor modifications, to simpify wrappers and reduce bloat. (There
are plans to create even smaller version of Turbo Vision, by adding a
preprocessor definition, that disables its rarely used features).

The current version PyTVision compiles under Linux and under DOS using
DJGPP/PythonD (although creating proper compile environment under DOS
is a non-trivial task).


## BUILDING

To build the module you will need swig 1.3.21.

Use the following to build the module and run the example under Linux:

cd tvision-py
sh configure --no-intl
make
cd ..

python setup.py build --build-lib .

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$PWD/tvision-py/makes
python test.py


