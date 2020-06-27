%define major	3
%define api	2.0

%define libname %mklibname plist %{api} %{major}
%define devname %mklibname -d plist
%define libnamecxx %mklibname plist++ %{api} %{major}
%define devnamecxx %mklibname -d plist++

Summary:	Library for manipulating Apple Binary and XML Property Lists
Name:		libplist
Version:	2.2.0
Release:	1
Group:		System/Libraries
License:	LGPLv2+
Url:		http://www.libimobiledevice.org/
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.gz
BuildRequires:	make
BuildRequires:	python-cython
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(python)

%description
libplist is a library for manipulating Apple Binary and XML Property Lists.

%package -n %{libname}
Group:		System/Libraries
Summary:	Library for manipulating Apple Binary and XML Property Lists
Suggests:	%{name} >= %{version}-%{release}

%description -n %{libname}
libplist is a library for manipulating Apple Binary and XML Property Lists.

%package -n %{devname}
Summary:	Development package for libplist
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
%{name}, development headers and libraries.

%package -n %{libnamecxx}
Summary:	C++ binding for libplist
Group:		Development/C++
Suggests:	%{name} >= %{version}-%{release}

%description -n %{libnamecxx}
C++ bindings for %{name}.

%package -n %{devnamecxx}
Summary:	Development package for libplist++
Group:		Development/C++
Requires:	%{libnamecxx} = %{version}-%{release}
Provides:	%{name}++-devel = %{version}-%{release}

%description -n %{devnamecxx}
%name, C++ development headers and libraries.

%package -n python-plist
Summary:	Python package for libplist
Group:		Development/Python
Requires:	python
BuildRequires:	pkgconfig(python)
#BuildRequires:	swig

%description -n python-plist
%{name}, python libraries and support.

%prep
%setup -q

%build

%configure \
	--disable-static \
	PYTHON=%{__python3} \
	CYTHON=%{_bindir}/cython-3
	

%make_build -j1

%install
%make_install


%files
%doc AUTHORS COPYING.LESSER
%{_bindir}/plistutil
%{_mandir}/man1/plistutil.1*

%files -n %{libname}
%{_libdir}/%{name}-%{api}.so.%{major}{,.*}

%files -n %{devname}
%{_includedir}/plist
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/%{name}-%{api}.so

%files -n %{libnamecxx}
%{_libdir}/%{name}++-%{api}.so.%{major}{,.*}

%files -n %{devnamecxx}
%exclude %{_includedir}/plist/plist.h
%{_libdir}/pkgconfig/%{name}++-%{api}.pc
%{_libdir}/%{name}++-%{api}.so

%files -n python-plist
%{python_sitearch}/plist.so
