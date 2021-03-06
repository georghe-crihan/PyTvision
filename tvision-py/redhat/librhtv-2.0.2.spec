%define name librhtv
%define version 2.0.2
%define rel 3
%define namefull %{name}.so.%{version}
%define incname rhtvision

Summary:   An intuitive TUI interface for console applications. 
Name:      %{name}
Version:   %{version}
Release:   %{rel}
Copyright: GPL
Packager:  Michel Catudal <bbcat@users.sf.net>
Vendor:    Salvador Eduardo Tropea <set@users.sf.net>
URL:       http://tvision.sf.net/
Group:     System Environment/Libraries
Source:    %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}

%description 
This is the shared library for programs using the RHTVision library.

The RHTVision library gives an intuitive and user friendly TUI (Textual User
Interface) for programs using this library and running in a console.

This library is based on the Turbo Vision library made by Borland Corporation.
That library was released by Borland under a Public Domain license. RHTVision
is Borland's Turbo Vision library but with enhancements, some changes and a
GPL license.

If you would like to develop applications using the RHTVision library, you'll
also need to install librhtv-devel.

%package devel
Summary:   RHTVision library development.
Group:     Development/Libraries
Requires:  %{name} = %{PACKAGE_VERSION}

%description devel
Libraries and include files you can use for developing applications using
the RHTVision library.

The RHTVision library gives an intuitive and user friendly TUI (Textual User
Interface) for programs using this library and running in a console.

This library is based on the Turbo Vision library made by Borland Corporation.
That library was released by Borland under a Public Domain license. RHTVision
is Borland's Turbo Vision library but with enhancements, some changes and a
GPL license.

You should install the librhtv-devel package only if you would like to develop
applications using the RHTVision library or you would like to compile programs
that use the RHTVision library.

%prep
%setup -q
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/%{name}-%{version}
rm -f $RPM_BUILD_DIR/tvision
ln -s $RPM_BUILD_DIR/%{name}-%{version} $RPM_BUILD_DIR/tvision

%setup
./configure

%build
make

%install

install -d -m 0755 $RPM_BUILD_ROOT/usr/include/rhtvision
rm -f $RPM_BUILD_ROOT/usr/include/rhtvision/*.h
install -m 0644 include/*.h $RPM_BUILD_ROOT/usr/include/rhtvision
install -d -m 0755 $RPM_BUILD_ROOT/usr/include/rhtvision/tv
install -m 0644 include/tv/*.h $RPM_BUILD_ROOT/usr/include/rhtvision/tv
install -d -m 0755 $RPM_BUILD_ROOT/usr/include/rhtvision/tv/linux
install -m 0644 include/tv/linux/*.h $RPM_BUILD_ROOT/usr/include/rhtvision/tv/linux
install -d -m 0755 $RPM_BUILD_ROOT/usr/include/rhtvision/tv/x11
install -m 0644 include/tv/x11/*.h $RPM_BUILD_ROOT/usr/include/rhtvision/tv/x11
install -d -m 0755 $RPM_BUILD_ROOT/usr/include/rhtvision/cl
install -m 0644 include/cl/*.h $RPM_BUILD_ROOT/usr/include/rhtvision/cl
install -d -m 0755 $RPM_BUILD_ROOT/usr/lib
install -m 0644 makes/librhtv.a $RPM_BUILD_ROOT/usr/lib
rm -f $RPM_BUILD_ROOT/usr/lib/librhtv.so
rm -f $RPM_BUILD_ROOT/usr/lib/librhtv.so.2
rm -f $RPM_BUILD_ROOT/usr/lib/librhtv.so.%{version}
cd $RPM_BUILD_ROOT/usr/lib; ln -s librhtv.so.%{version} librhtv.so
cd $RPM_BUILD_DIR/%{name}-%{version}
install -m 0755 makes/librhtv.so.%{version} $RPM_BUILD_ROOT/usr/lib
strip --strip-debug $RPM_BUILD_ROOT/usr/lib/librhtv.so.%{version}
install -d -m 0755 $RPM_BUILD_ROOT/usr/lib
install -m 0644 intl/dummy/libtvfintl.a $RPM_BUILD_ROOT/usr/lib/libtvfintl.a
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/packages/librhtv
install -m 0644 doc/*.txt doc/*.html  $RPM_BUILD_ROOT/usr/share/doc/packages/librhtv

%clean
#rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
/usr/lib/lib*.so.*

%files devel
%defattr(-,root,root)
%dir /usr/include/%{incname}
%dir /usr/include/%{incname}/tv
/usr/include/%{incname}/*.h
/usr/include/%{incname}/tv/*.h
/usr/include/%{incname}/tv/linux/*.h
/usr/include/%{incname}/tv/x11/*.h
/usr/include/%{incname}/cl/*.h
/usr/lib/*.a
/usr/lib/lib*.so
/usr/share/doc/packages/librhtv/*


%changelog -n librhtv
* Tue Feb 18 2003 - Michel Catudal bbcat@netonecom.net
- Add documentation
* Sun Jan 5 2003 - Michel Catudal bbcat@netonecom.net
- Released 2.0.1 version
* Sat Oct 6 2002 - Michel Catudal bbcat@netonecom.net
- Version 2 from CVS
* Mon Nov 5 2001 - Michel Catudal bbcat@netonecom.net
- Added copying of include files on include/cl which were missing
* Sun Nov 4 2001 - "Ernas M. Jamil" <ernasm@samba.co.id>
- Added copying of include files which were not done due
  to changes that I was not aware of in the include files.
  The same install script worked before.
  Thanks to Ernas M. Jamil for pointing it out.
