These scripts are based on cx_Freeze. It's purpose is to faciliate building
PyTVision/PythonD executables that run under DOS without LFN (long file names)
support. As a side effect it speeds up resulting program loading by several
times, as compared to un-frozen layout.

This is a reduced functionality version of cx_Freeze, customized for
PyTVision linking.
See http://starship.python.net/crew/atuining/cx_Freeze/ for the full
versions of cx_Freeze.

The scripts also require cx_PyGenLib package available from:
http://prdownloads.sourceforge.net/cx-freeze/cx_PyGenLib-2.2.tar.gz?download


USAGE

1. Build a base executable by invoking  MakePyTVBase.py script. 
2. Run freeze.sh script. The frozen test binary will be put into bin/
   subdirectory.

