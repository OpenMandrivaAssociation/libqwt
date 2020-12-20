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
#Patch0:		qwt-6.0.1-qwtconfig.patch
#Patch1:		qwt-6.0.1-do-not-install-docs.patch
#Patch2:		qwt-6.0.1-linkage.patch
#Patch3:		qwt-6.0.1-sfmt.patch

BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
Qwt is an extension to the Qt GUI library from Troll Tech AS.
The Qwt library contains widgets and components which are
primarily useful for technical and scientifical purposes.
It includes a 2-D plotting widget, different kinds of sliders,
and much more.

%package -n %{libname}
Summary:	2D plotting widget extension to the Qt GUI
Group:		System/Libraries

%description -n %{libname}
The libqwt-devel package contains the header files and static libraries
necessary for developing programs using the Qwt Widget set

If you want to develop programs which will use this set of widgets,
you should install this package. You need also to install the libqwt package.

%package -n %{libnamedev}
Summary:	Development tools for programs which uses Qwt Widget set
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}
Requires:	qt4-devel
Provides:	libqwt-devel = %{EVRD}
Provides:	qwt-devel = %{EVRD}
Obsoletes:	%{libname}-devel
Conflicts:	%{lib5name}

%description -n %{libnamedev}
The libqwt-devel package contains the header files and static libraries
necessary for developing programs using the Qwt Widget set

If you want to develop programs which will use this set of widgets,
you should install this package. You need also to install the libqwt package.

%prep
%setup -q -n %{realname}-%{version}

#sed -i -e 's|{QWT_INSTALL_PREFIX}/lib|{QWT_INSTALL_PREFIX}/%{_lib}|' qwtconfig.pri
#sed -i -e 's|{QWT_INSTALL_PREFIX}/plugins/designer|{QWT_INSTALL_PREFIX}/%{_lib}/qt4/plugins/designer|' qwtconfig.pri
#sed -i -e 's|{QWT_INSTALL_PREFIX}/features|{QWT_INSTALL_PREFIX}/%{_lib}/qt4/features|' qwtconfig.pri

%build
%qmake_qt5 QWT_CONFIG+=QwtPkgConfig ..
%make_build

%install
make install INSTALL_ROOT=%{buildroot}

%files -n %{libname}
%doc CHANGES COPYING README
%{_libdir}/*.so.%{major}*

%files -n %{libnamedev}
%doc examples doc/html
%{_includedir}/*
%{qt4lib}/*.so
%{qt4plugins}/designer/*.so
%{qt4lib}/qt4/features



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

