%define realname qwt
%define major 6
%define libname %mklibname %{realname} %{major}
%define libnamedev %mklibname %{realname} -d

# crisb - seems not defined anywhere?
%define qmake_qt6 \
  %set_build_flags \
  CPPFLAGS="${CPPFLAGS:-$CPPFLAGS}" ; export CPPFLAGS ; \
  CFLAGS="${CFLAGS:-$CFLAGS}" ; export CFLAGS ; \
  CXXFLAGS="${CXXFLAGS:-$CXXFLAGS}" ; export CXXFLAGS ; \
  LDFLAGS="${LDFLAGS:-$LDFLAGS -Wl,-Bsymbolic-functions}" ; export LDFLAGS ; \
  %{_bindir}/qmake-qt6 \\\
    %if "%{_lib}" != "lib" \
       libsuff=64 \\\
    %endif \
    QMAKE_CFLAGS="${CFLAGS:-$CFLAGS}" \\\
    QMAKE_CFLAGS_RELEASE="${CFLAGS:-$CFLAGS}" \\\
    QMAKE_CFLAGS_OPTIMIZE="${CFLAGS:-$CFLAGS}" \\\
    QMAKE_CFLAGS_OPTIMIZE_FULL="${CFLAGS:-$CFLAGS}" \\\
    QMAKE_CXXFLAGS="${CXXFLAGS:-$CXXFLAGS}" \\\
    QMAKE_CXXFLAGS_RELEASE="${CXXFLAGS:-$CXXFLAGS}" \\\
    QMAKE_LFLAGS="$LDFLAGS" \\\
    QMAKE_LFLAGS_RELEASE="$LDFLAGS"


Name:		libqwt
Version:	6.2.0
Release:	7
Summary:	2D plotting widget extension to the Qt GUI
License:	Qwt License 1.0
Group:		System/Libraries
Url:		http://sourceforge.net/projects/qwt
Source0:	http://freefr.dl.sourceforge.net/sourceforge/qwt/%{realname}-%{version}.tar.bz2
# use QT_INSTALL_ paths instead of custom prefix
Patch51:        qwt-6.1.5-qt_install_paths.patch
# parallel-installable qt5 version
Patch52:        qwt-qt5.patch
#
Patch53:        qwt-6.1.3-no_rpath.patch

BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  qmake5

BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Designer)
BuildRequires:  pkgconfig(Qt6OpenGL)
BuildRequires:  pkgconfig(Qt6PrintSupport)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  qmake-qt6
BuildRequires:	qt6-cmake

%description
Qwt is an extension to the Qt GUI library from Troll Tech AS.
The Qwt library contains widgets and components which are
primarily useful for technical and scientifical purposes.
It includes a 2-D plotting widget, different kinds of sliders,
and much more.

%define libname_qt5 %mklibname %realname-qt5_ %{major}

%package -n     %{libname_qt5}
Summary:        2D plotting widget extension to the Qt5 GUI
Group:          System/Libraries

%description -n %{libname_qt5}
Qwt is an extension to the Qt5 GUI library from Troll Tech AS.
The Qwt library contains widgets and components which are
primarily useful for technical and scientifical purposes.
It includes a 2-D plotting widget, different kinds of sliders,
and much more.

This package provides the runtime library.

%files -n %{libname_qt5}
%doc CHANGES* README
%license COPYING
%{_qt5_libdir}/libqwt-qt5.so.%{major}{,.*}
%{_libdir}/libqwt.so.%{major}.*
%{_qt5_plugindir}/designer/libqwt_designer_plugin.so

#------------------------------------------------------------------------------

%define libnamedev_qt5 %mklibname qwt-qt5 -d

%package -n     %{libnamedev_qt5}
Summary:        Development tools for programs which uses Qt5 Qwt Widget set
Group:          System/Libraries
Requires:       %{libname_qt5} = %{version}
Provides:       libqwt-qt5-devel = %{version}-%{release}
Provides:       libqwtmathml-qt5-devel = %{version}-%{release}

%description -n %{libnamedev_qt5}
The %{libnamedev_qt5} package contains the header files and static libraries
necessary for developing programs using the Qt5 Qwt Widget set.

If you want to develop programs which will use this set of widgets,
you should install this package. You need also to install the libqwt-qt5 package.

%files -n %{libnamedev_qt5}
%doc COPYING
%doc examples
%doc %{_datadir}/doc/qt5/html/qwt/
%{_qt5_includedir}/qwt/
%{_qt5_libdir}/libqwt-qt5.so
#{_qt5_libdir}/libqwtmathml-qt5.so
%{_qt5_libdir}/pkgconfig/Qt5Qwt6.pc
%{_libdir}/qt5/mkspecs/*
%{_mandir}/man3/

%define libname_qt6 %mklibname %realname-qt6_ %{major}

%package -n     %{libname_qt6}
Summary:        2D plotting widget extension to the Qt6 GUI
Group:          System/Libraries

%description -n %{libname_qt6}
Qwt is an extension to the Qt6 GUI library from Troll Tech AS.
The Qwt library contains widgets and components which are
primarily useful for technical and scientifical purposes.
It includes a 2-D plotting widget, different kinds of sliders,
and much more.

This package provides the runtime library.

%files -n %{libname_qt6}
#doc CHANGES* README
#license COPYING
%{_libdir}/qt6/lib/libqwt-qt6.so.%{major}{,.*}
%{_libdir}/qt6/plugins/designer/libqwt_designer_plugin.so

#------------------------------------------------------------------------------

%define libnamedev_qt6 %mklibname qwt-qt6 -d

%package -n     %{libnamedev_qt6}
Summary:        Development tools for programs which uses Qt6 Qwt Widget set
Group:          System/Libraries
Requires:       %{libname_qt6} = %{version}
Provides:       libqwt-qt6-devel = %{version}-%{release}
Provides:       libqwtmathml-qt6-devel = %{version}-%{release}

%description -n %{libnamedev_qt6}
The %{libnamedev_qt6} package contains the header files and static libraries
necessary for developing programs using the Qt Qwt Widget set.

If you want to develop programs which will use this set of widgets,
you should install this package. You need also to install the libqwt-qt6 package.

%files -n %{libnamedev_qt6}
#doc COPYING
#doc examples
%doc %{_libdir}/qt6/doc/html/qwt/
%{_libdir}/qt6/include/qwt/
%{_libdir}/qt6/lib/libqwt-qt6.so
%{_libdir}/qt6/lib/libqwt.so.%{major}.*
#{_libdir}/libqwtmathml-qt6.so
%{_libdir}/pkgconfig/Qt6Qwt6.pc
%{_libdir}/qt6/mkspecs/*

%prep
%setup -q -n %{realname}-%{version}
%autopatch -p1

%build

mkdir qt6
pushd qt6
%{qmake_qt6} QWT_CONFIG+=QwtPkgConfig CONFIG+=nostrip ..
%{make_build}
popd

%qmake_qt5 QWT_CONFIG+=QwtPkgConfig CONFIG+=nostrip
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot} -C qt6
%make_install INSTALL_ROOT=%{buildroot}

mv %{buildroot}%{_qt5_docdir}/html/html %{buildroot}%{_qt5_docdir}/html/qwt
mkdir -p %{buildroot}%{_mandir}
mv %{buildroot}%{_qt5_docdir}/html/man/man3 %{buildroot}%{_mandir}/

mv %{buildroot}%{_libdir}/qt6/doc/html/html %{buildroot}%{_libdir}/qt6/doc/html/qwt
rm -Rf %{buildroot}%{_libdir}/qt6/doc/html/man

mkdir -p %{buildroot}%{_libdir}/pkgconfig/
mv %{buildroot}/%{_libdir}/qt6/lib/pkgconfig/Qt6Qwt6.pc %{buildroot}%{_libdir}/pkgconfig/

%changelog
* Tue May 08 2012 Alexander Khrukin <akhrukin@mandriva.org> 6.0.1-2
+ Revision: 797461
- make install instead of macro
- rebuild

* Sat Apr 28 2012 Andrey Bondrov <abondrov@mandriva.org> 6.0.1-1
+ Revision: 794201
- New version 6.0.1, new major 6, update patches, Requires, Conflicts and file list

* Tue May 17 2011 Paulo Andrade <pcpa@mandriva.com.br> 5.2.1-3
+ Revision: 675373
- Rename conflicting manpage filename

* Sat Feb 05 2011 Funda Wang <fwang@mandriva.org> 5.2.1-2
+ Revision: 636050
- tighten BR

* Mon Aug 23 2010 Yuri Myasoedov <omerta13@mandriva.org> 5.2.1-1mdv2011.0
+ Revision: 572091
- New version 5.2.1

* Fri May 01 2009 Funda Wang <fwang@mandriva.org> 5.2.0-1mdv2010.0
+ Revision: 369350
- New version 5.2.0

* Fri Mar 13 2009 Funda Wang <fwang@mandriva.org> 5.1.1-1mdv2009.1
+ Revision: 354460
- rediff patch

* Tue Aug 05 2008 Funda Wang <fwang@mandriva.org> 5.1.1-1mdv2009.0
+ Revision: 263932
- New version 5.1.1

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu May 15 2008 Funda Wang <fwang@mandriva.org> 5.1.0-1mdv2009.0
+ Revision: 207499
- New version 5.1.0

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 5.0.2-1mdv2008.1
+ Revision: 140928
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Jul 21 2007 Funda Wang <fwang@mandriva.org> 5.0.2-1mdv2008.0
+ Revision: 54251
- New version
- renew file list
- Build qt4 version

* Mon Apr 23 2007 Lenny Cartier <lenny@mandriva.org> 5.0.1-1mdv2008.0
+ Revision: 17323
- Update to 5.0.1

