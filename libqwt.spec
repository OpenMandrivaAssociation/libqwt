%define realname qwt
%define major 6
%define libname %mklibname %{realname} %{major}
%define libnamedev %mklibname %{realname} -d

%define lib5name %mklibname %{realname} 5

%define debug_package %{nil}

Name:		libqwt
Version:	6.1.5
Release:	1
Summary:	2D plotting widget extension to the Qt GUI
License:	Qwt License 1.0
Group:		System/Libraries
Url:		http://sourceforge.net/projects/qwt
Source0:	http://freefr.dl.sourceforge.net/sourceforge/qwt/%{realname}-%{version}.tar.bz2
# fix pkgconfig support
Patch50:        qwt-6.1.1-pkgconfig.patch
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
%{_qt5_libdir}/libqwtmathml-qt5.so.%{major}{,.*}
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
%docdir %{_qt5_docdir}/html/
%{_qt5_docdir}/html/qwt/
%{_qt5_includedir}/qwt/
%{_qt5_libdir}/libqwt-qt5.so
%{_qt5_libdir}/libqwtmathml-qt5.so
%{_qt5_libdir}/pkgconfig/Qt5Qwt6.pc
%{_qt5_libdir}/pkgconfig/qwtmathml-qt5.pc
%{_qt5_archdatadir}/mkspecs/*
%{_mandir}/man3/*

%prep
%setup -q -n %{realname}-%{version}
%autopatch -p1

#sed -i -e 's|{QWT_INSTALL_PREFIX}/lib|{QWT_INSTALL_PREFIX}/%{_lib}|' qwtconfig.pri
#sed -i -e 's|{QWT_INSTALL_PREFIX}/plugins/designer|{QWT_INSTALL_PREFIX}/%{_lib}/qt4/plugins/designer|' qwtconfig.pri
#sed -i -e 's|{QWT_INSTALL_PREFIX}/features|{QWT_INSTALL_PREFIX}/%{_lib}/qt4/features|' qwtconfig.pri

%build
%qmake_qt5
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

mv %{buildroot}%{_qt5_docdir}/html/html %{buildroot}%{_qt5_docdir}/html/qwt
mkdir -p %{buildroot}%{_mandir}
mv %{buildroot}%{_qt5_docdir}/html/man/man3 %{buildroot}%{_mandir}/


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

