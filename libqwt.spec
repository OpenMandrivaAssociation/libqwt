%define name libqwt
%define version 5.0.1
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

# Automatically added by buildreq on Fri Dec 03 2004
BuildRequires: fontconfig freetype2 gcc-c++ qt4-devel libstdc++-devel X11-devel

BuildRoot: %{_tmppath}/%{name}-root

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
Provides: libqwt-devel
Obsoletes: %libname-devel

%description -n %libnamedev
The libqwt-devel package contains the header files and static libraries
necessary for developing programs using the Qwt Widget set

If you want to develop programs which will use this set of widgets,
you should install this package. You need also to install the libqwt package.

%prep
%setup -q -n %realname-%version

%build
%{qt4dir}/bin/qmake qwt.pro
make
(cd examples; %{qt4dir}/bin/qmake examples.pro; make)
(cd designer; sed -i "s,plugins/designer,plugins/%_lib/designer,g" qwtplugin.pro; %{qt4dir}/bin/qmake qwtplugin.pro; make)

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{qt4dir}/include/qwt
mkdir -p %{buildroot}%{_mandir}/man3
mkdir -p %{buildroot}%{_libdir}

for n in src/*.h ; do
    install -m 644 $n %{buildroot}%{qt4include}/qwt
done

# install, preserving links
chmod 644 lib/libqwt.so*
for n in lib/libqwt.so* ; do
    cp -d $n %{buildroot}/%{_libdir}
done

# build the designer plugin
if [ -e %{qt4dir}/bin/qmake ]; then
    (cd designer; make install INSTALL_ROOT=%{buildroot})
    echo "%qt3dir/plugins/designer/libqwtplugin.so" > plugin.list
else
    echo >plugin.list
fi

for n in doc/man/man3/*.3 ; do
    install -m 644 $n %{buildroot}/%{_mandir}/man3
done

# clean up the example tree
(cd examples; make distclean)
(cd examples; rm -f .*.cache */.*.cache */*/.*.cache)
(cd examples; rm -rf Makefile */moc */obj */*/moc */*/obj)

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %libname
%defattr (-,root,root)
%doc CHANGES COPYING README
%_libdir/libqwt.so.*

%files -n %libnamedev -f plugin.list
%defattr (-,root,root)
%doc COPYING doc/html/*.css doc/html/*.html doc/html/*.gif doc/html/*.png
%doc examples
%qt4include/qwt
%_libdir/libqwt.so
%_mandir/man3/*
