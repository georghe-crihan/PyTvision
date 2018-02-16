#!/usr/bin/make
#
# Copyright (c) 2003-2004 by Salvador E. Tropea.
# Covered by the GPL license.
#
ifeq ($(prefix),)
  prefix=/usr/local
endif
ifeq ($(INSTALL),)
  INSTALL=install
endif
EXE_EXT=
libdir=$(prefix)/lib
OS=UNIX

DARWIN=1
export

.PHONY:  static-lib rhtv-config$(EXE_EXT) dynamic-lib internac install-static install-dynamic install-internac  install-headers install-config clean \
	intl-dummy examples

all:  static-lib rhtv-config$(EXE_EXT) dynamic-lib internac intl-dummy



static-lib:
	$(MAKE) -C makes -f librhtv.mkf
	ranlib makes/librhtv.a

dynamic-lib: intl-dummy
	$(MAKE) DYNAMIC_LIB=1 -C makes -f librhtv.mkf
	-cd makes; rm -f librhtv.dylib; ln -s librhtv.2.2.1.dylib librhtv.dylib
	-cd makes; rm -f librhtv.2.dylib; ln -s librhtv.2.2.1.dylib librhtv.2.dylib

internac:
	$(MAKE) -C intl


intl-dummy:
	$(MAKE) -C intl/dummy
	cp intl/dummy/libtvfintl.a makes
	ranlib makes/libtvfintl.a


examples:
	$(MAKE) -C examples

rhtv-config$(EXE_EXT): rhtv-config.c include/tv/configtv.h
	g++ -o rhtv-config$(EXE_EXT) -Iinclude rhtv-config.c

install-headers:
	$(INSTALL) -d -m 0755 $(prefix)/include/rhtvision
	rm -f $(prefix)/include/rhtvision/*.h
	$(INSTALL) -m 0644 include/*.h $(prefix)/include/rhtvision
	$(INSTALL) -d -m 0755 $(prefix)/include/rhtvision/tv
	$(INSTALL) -m 0644 include/tv/*.h $(prefix)/include/rhtvision/tv
	$(INSTALL) -d -m 0755 $(prefix)/include/rhtvision/tv/linux
	$(INSTALL) -m 0644 include/tv/linux/*.h $(prefix)/include/rhtvision/tv/linux
	$(INSTALL) -d -m 0755 $(prefix)/include/rhtvision/tv/x11
	$(INSTALL) -m 0644 include/tv/x11/*.h $(prefix)/include/rhtvision/tv/x11
	$(INSTALL) -d -m 0755 $(prefix)/include/rhtvision/cl
	$(INSTALL) -m 0644 include/cl/*.h $(prefix)/include/rhtvision/cl


install-static: static-lib
	$(INSTALL) -d -m 0755 $(libdir)
	$(INSTALL) -m 0644 makes/librhtv.a $(libdir)

install-dynamic: dynamic-lib
	$(INSTALL) -d -m 0755 $(libdir)
	rm -f $(libdir)/librhtv.dylib
	rm -f $(libdir)/librhtv.2.dylib
	rm -f $(libdir)/librhtv.2.2.1.dylib
	cd $(libdir); ln -s librhtv.2.2.1.dylib librhtv.dylib
	$(INSTALL) -m 0644 makes/librhtv.2.2.1.dylib $(libdir)
	strip -S $(libdir)/librhtv.2.2.1.dylib

install-internac:
	$(MAKE) -C intl install


install-intl-dummy: intl-dummy
	$(INSTALL) -d -m 0755 $(libdir)
	$(INSTALL) -m 0644 intl/dummy/libtvfintl.a $(libdir)
	ranlib $(libdir)/libtvfintl.a


install-config:
	$(INSTALL) -d -m 0755 $(prefix)/bin
	$(INSTALL) -m 0755 rhtv-config$(EXE_EXT) $(prefix)/bin


install: install-static install-dynamic install-internac  install-headers install-intl-dummy install-config

clean:
	rm -f makes/librhtv.so*
	rm -f makes/obj/*.o
	rm -f makes/obj/*.lo
	rm -f makes/librhtv.a
	rm -f compat/obj/*.o
	rm -f compat/obj/*.lo
	rm -f intl/dummy/*.o
	rm -f intl/dummy/*.lo
	rm -f intl/dummy/*.a
	-$(MAKE) -C examples clean
	-$(MAKE) -C intl clean
	rm -f configure.cache
	rm -f rhtv-config$(EXE_EXT)


#
# For compatibility with automake:
# needed to 'make dist' of tiger
#
distdir: clean
	@cp -pR * $(distdir)

