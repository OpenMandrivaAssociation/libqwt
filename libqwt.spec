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
Version:	6.3.0
Release:	3
Summary:	2D plotting widget extension to the Qt GUI
License:	Qwt License 1.0
Group:		System/Libraries
Url:		https://sourceforge.net/projects/qwt
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
%doc README
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
%doc %{_docdir}/qt5/html/html
%{_qt5_includedir}/qwt/
%{_qt5_libdir}/libqwt-qt5.so
#{_qt5_libdir}/libqwtmathml-qt5.so
%{_qt5_libdir}/pkgconfig/Qt5Qwt6.pc
%{_libdir}/qt5/mkspecs/*

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
%make_install INSTALL_ROOT=%{buildroot}
%make_install INSTALL_ROOT=%{buildroot} -C qt6

mv %{buildroot}%{_libdir}/qt6/doc/html/html %{buildroot}%{_libdir}/qt6/doc/html/qwt
rm -Rf %{buildroot}%{_libdir}/qt6/doc/html/man

mkdir -p %{buildroot}%{_libdir}/pkgconfig/
mv %{buildroot}/%{_libdir}/qt6/lib/pkgconfig/Qt6Qwt6.pc %{buildroot}%{_libdir}/pkgconfig/
