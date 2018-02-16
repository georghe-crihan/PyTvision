INCLUDE    = -I/home/drdivano/include/python2.2 -I/home/drdivano/lib/python2.2/config -Itvision-py/include
LIB        = -Ltvision-py/makes -lrhtv -lX11 -lXmu

CPPFLAGS   = $(INCLUDE)
CFLAGS     = -pipe -O2

all:    distutils_build _tv.so

distutils_build:
	CC=g++ python setup.py build --build-lib .

all_wrap.cxx: *.i
	swig -c++ -python -DNO_STREAM all.i
	sed 's/TAppWrapper(),/TAppWrapper(arg0),TProgInit(\&TAppWrapper::_sInitStatusLine,\&TAppWrapper::_sInitMenuBar,\&TAppWrapper::_sInitDeskTop),/' all_wrap.cxx > all_wrap.cxx_
	mv -f all_wrap.cxx_ all_wrap.cxx

_tv.so: all_wrap.cxx inithelper.cpp
	c++ -c -fpic all_wrap.cxx -DHAVE_CONFIG_H $(INCLUDE)
	c++ -c -fpic  inithelper.cpp -DHAVE_CONFIG_H $(INCLUDE)
	c++ -shared   all_wrap.o inithelper.o $(LIB) -o _tv.so


clean:
	$(RM) -f *.o *.so *~ *.pyc core all_wrap.cxx
	$(RM) -rf build
	$(RM) freeze/*.pyc freeze/*Base freeze/*~ bin/*

