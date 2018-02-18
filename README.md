# PyTVison - Python bindings (through SWIG) for TurboVision by Salvador Tropea

Initial SWIG bindings are Copyright (C) 2004 Alex Novgorodov (drdivano).

PyTVision taken from: http://pytvision.sourceforge.net

Archive URL: https://sourceforge.net/projects/pytvision/files/pytvision/0.0.2/.

TVision 2.2.1-4 by Salvador E. Tropea (SET) taken from: https://sourceforge.net/projects/tvision/files/UNIX/2.2.1%20CVS20161117/

### DONE:
* Builds and runs under OSX Sierra with XCode, ncurses, as well as GCC 4.3 and SWIG from macports.
* All the examples from TurboVision distribution, apart from those requiring libintl and TurboVision Streams, compile and work in console and XQuartz GUI.

### TODO:
* Fix core dump when run from Python under console and XQuartz.
* Possibly support Java bindings to allow use with Jython.
* Possibly enable libintl support.
* Possibly add TurboVision Streams support.

## DESCRIPTION

This is PyTVision - a set of Python bindings for Turbo Vision.

The distribution includes a version of Turbo Vision, with removed streams and
some other minor modifications, to simpify wrappers and reduce bloat. (There
are plans to create even smaller version of Turbo Vision, by adding a
preprocessor definition, that disables its rarely used features).

The current version PyTVision compiles under Linux and under DOS using
DJGPP/PythonD (although creating proper compile environment under DOS
is a non-trivial task).

### tv-patches
This directory contains a set of patches against vanilla RHTVLib 2.2.1-4 by
Salvador E. Tropea. Read their descriptions for details.

## BUILDING

To build the module you will need SWIG (I used 1.3.21).

Use the following to build the module and run the example under Linux:
```
cd tvision-py
sh configure --no-intl
make
cd ..

python setup.py build --build-lib .

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$PWD/tvision-py/makes
python test.py
```
For OS X use:
```
cd tvision-py
sh configure --no-intl --x-lib=/opt/X11/lib --x-include=/opt/X11/include --cxxflags=-DNO_STREAM --include=${PWD}
make
cd ..

# Now, either do a
rm tvision.py/makes/*.dylib
# or
(cd py-tvision; sudo make install)
# as the DYLD_INSERT_LIBRARIES won't allow to load a shared object with embedded full path in it.
make

./test.py
```

