set -x
c++ -c -fpic  all_wrap.cxx   -Itvision-py/include -DHAVE_CONFIG_H -I/home/drdivano/include/python2.2 -I/home/drdivano/include/python2.2/config
c++ -c -fpic  inithelper.cpp   -Itvision-py/include -DHAVE_CONFIG_H -I/home/drdivano/include/python2.2 -I/home/drdivano/lib/python2.2/config
c++ -shared   all_wrap.o inithelper.o  -Ltvision-py/makes -lrhtv  -o _tv.so
