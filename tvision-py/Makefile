#!/usr/bin/make
#
# Copyright (c) 2003 by Salvador E. Tropea.
# Covered by the GPL license.
#
ifeq ($(prefix),)
  prefix=/usr/local
endif
EXE_EXT=
libdir=$(prefix)/lib
OS=UNIX

export

.PHONY:  static-lib rhtv-config$(EXE_EXT) dynamic-lib internac install-static install-dynamic install-internac  install-headers install-config clean \
	intl-dummy examples

all:  static-lib rhtv-config$(EXE_EXT) dynamic-lib internac intl-dummy



static-lib:
	$(MAKE) -C makes -f librhtv.mkf
	ranlib makes/librhtv.a

dynamic-lib:
	$(MAKE) DYNAMIC_LIB=1 -C makes -f librhtv.mkf
	cd makes; ln -sf librhtv.so.2.0.2 librhtv.so
	cd makes; ln -sf librhtv.so.2.0.2 librhtv.so.2

internac:
	$(MAKE) -C intl


intl-dummy:
	$(MAKE) -C intl/dummy
	cp intl/dummy/libtvfintl.a makes
	ranlib makes/libtvfintl.a


examples:
	$(MAKE) -C examples

rhtv-config$(EXE_EXT): rhtv-config.c include/tv/configtv.h
	cc -o rhtv-config$(EXE_EXT) -Iinclude rhtv-config.c

install-headers:
	install -d -m 0755 $(prefix)/include/rhtvision
	rm -f $(prefix)/include/rhtvision/*.h
	install -m 0644 include/*.h $(prefix)/include/rhtvision
	install -d -m 0755 $(prefix)/include/rhtvision/tv
	install -m 0644 include/tv/*.h $(prefix)/include/rhtvision/tv
	install -d -m 0755 $(prefix)/include/rhtvision/tv/linux
	install -m 0644 include/tv/linux/*.h $(prefix)/include/rhtvision/tv/linux
	install -d -m 0755 $(prefix)/include/rhtvision/cl
	install -m 0644 include/cl/*.h $(prefix)/include/rhtvision/cl


install-static: static-lib
	install -d -m 0755 $(libdir)
	install -m 0644 makes/librhtv.a $(libdir)

install-dynamic: dynamic-lib
	rm -f $(libdir)/librhtv.so
	rm -f $(libdir)/librhtv.so.2
	rm -f $(libdir)/librhtv.so.2.0.2
	cd $(libdir); ln -s librhtv.so.2.0.2 librhtv.so
	install -m 0644 makes/librhtv.so.2.0.2 $(libdir)
	strip --strip-debug $(libdir)/librhtv.so.2.0.2
	-ldconfig

install-internac:
	$(MAKE) -C intl install


install-intl-dummy: intl-dummy
	install -d -m 0755 $(libdir)
	install -m 0644 intl/dummy/libtvfintl.a $(libdir)/libtvfintl.a


install-config:
	install -d -m 0755 $(prefix)/bin
	install -m 0755 rhtv-config$(EXE_EXT) $(prefix)/bin

install: install-static install-dynamic install-internac  install-headers install-intl-dummy install-config

clean:
	rm -f makes/*.so* makes/*.a
	rm -f makes/obj/*.o makes/obj/*.lo
	rm -f compat/obj/*.o
	rm -f intl/dummy/*.o
	rm -f intl/dummy/*.a
	-$(MAKE) -C examples clean
	rm -f configure.cache
	rm -f rhtv-config$(EXE_EXT)

