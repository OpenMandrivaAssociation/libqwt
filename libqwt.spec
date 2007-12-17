%define name libqwt
%define version 5.0.2
%define release 1

%define realname qwt
%define major 5
%define libname %mklibname %{realname} %major
%define libnamedev %mklibname %{realname} -d

%define debug_package %{nil} 

Name: %name
Version: %version
Release: %mkrel %release
Summary: 2D plotting widget extension to the Qt GUI
License: LGPL
Group: System/Libraries
Url: http://sourceforge.net/projects/qwt
Source: %realname-%version.tar.bz2
Patch0: qwt-5.0.2-qwtconfig-installbase.patch
Patch1: qwt-5.0.1-do-not-install-docs.patch

# Automatically added by buildreq on Fri Dec 03 2004
BuildRequires: fontconfig freetype2 gcc-c++ qt4-devel libstdc++-devel X11-devel


%description
Qwt is an extension to the Qt GUI library from Troll Tech AS.
The Qwt library contains widgets and components which are
primarily useful for technical and scientifical purposes.
It includes a 2-D plotting widget, different kinds of sliders,
and much more.

%package -n %libname 
Summary: 2D plotting widget extension to the Qt GUI
Group: System/Libraries

%description -n %libname
The libqwt-devel package contains the header files and static libraries
necessary for developing programs using the Qwt Widget set

If you want to develop programs which will use this set of widgets,
you should install this package. You need also to install the libqwt package.

%package -n %libnamedev
Summary: Development tools for programs which uses Qwt Widget set
Group: System/Libraries
Requires: %libname = %version
Provides: libqwt-devel = %version-%release
Obsoletes: %libname-devel

%description -n %libnamedev
The libqwt-devel package contains the header files and static libraries
necessary for developing programs using the Qwt Widget set

If you want to develop programs which will use this set of widgets,
you should install this package. You need also to install the libqwt package.

%prep
%setup -q -n %realname-%version
%patch0 -p0
%patch1 -p0
sed -i -e 's|INSTALLBASE/lib|INSTALLBASE/%{_lib}|' qwtconfig.pri

%build
%{qt4dir}/bin/qmake qwt.pro
make

%install
rm -rf %{buildroot}
make install INSTALL_ROOT=%{buildroot}

mkdir -p %{buildroot}%{_mandir}/man3/
install doc/man/man3/* %{buildroot}%{_mandir}/man3/

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %libname
%defattr (-,root,root)
%doc CHANGES COPYING README
%_libdir/libqwt.so.*
%{qt4plugins}/designer/*

%files -n %libnamedev
%defattr (-,root,root)
%doc COPYING doc/html/*.css doc/html/*.html doc/html/*.gif doc/html/*.png
%doc examples
%_includedir/*
%_libdir/*.so
%_mandir/man3/*
