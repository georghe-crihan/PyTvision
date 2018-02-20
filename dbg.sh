#!/bin/sh
if [ ! -r _tv.so ]; then
	python setup.py build --debug --build-lib .
fi

rm -f core
ulimit -c unlimited
#unset DISPLAY
sleep 1
LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${PWD}/tvision-py/makes \
	gdb /usr/bin/python2.7
#reset

if [ -e core ]; then
#	if [ core -nt _tv.so ]; then
#		gdb -c core /usr/bin/python2.7
#	fi
fi
