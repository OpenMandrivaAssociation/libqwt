%define realname qwt
%define major 6
%define libname %mklibname %{realname} %{major}
%define libnamedev %mklibname %{realname} -d

%define lib5name %mklibname %{realname} 5

%define debug_package %{nil}

Name:		libqwt
Version:	6.0.1
Release:	2
Summary:	2D plotting widget extension to the Qt GUI
License:	Qwt License 1.0
Group:		System/Libraries
Url:		http://sourceforge.net/projects/qwt
Source0:	http://freefr.dl.sourceforge.net/sourceforge/qwt/%{realname}-%{version}.tar.bz2
Patch0:		qwt-6.0.1-qwtconfig.patch
Patch1:		qwt-6.0.1-do-not-install-docs.patch
Patch2:		qwt-6.0.1-linkage.patch
Patch3:		qwt-6.0.1-sfmt.patch
BuildRequires:	qt4-devel

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
%patch0 -p1 -b .installpath
%patch1 -p1 -b .doc
%patch2 -p1 -b .linkage
%patch3 -p1 -b .sfmt
sed -i -e 's|{QWT_INSTALL_PREFIX}/lib|{QWT_INSTALL_PREFIX}/%{_lib}|' qwtconfig.pri
sed -i -e 's|{QWT_INSTALL_PREFIX}/plugins/designer|{QWT_INSTALL_PREFIX}/%{_lib}/qt4/plugins/designer|' qwtconfig.pri
sed -i -e 's|{QWT_INSTALL_PREFIX}/features|{QWT_INSTALL_PREFIX}/%{_lib}/qt4/features|' qwtconfig.pri

%build
%qmake_qt4 QT_INSTALL_PREFIX=%{_prefix}
make

%install
%makeinstall_std

%files -n %{libname}
%doc CHANGES COPYING README
%{_libdir}/*.so.%{major}*

%files -n %{libnamedev}
%doc examples doc/html
%{_includedir}/*
%{qt4lib}/*.so
%{qt4plugins}/designer/*.so
%{qt4lib}/qt4/features

