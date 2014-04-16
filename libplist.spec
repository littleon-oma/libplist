%define major 2
%define libname %mklibname plist %{major}
%define devname %mklibname -d plist
%define libnamecxx %mklibname plist++ %{major}
%define devnamecxx %mklibname -d plist++

Summary:	Library for manipulating Apple Binary and XML Property Lists
Name:		libplist
Version:	1.11
Release:	2
Group:		System/Libraries
License:	LGPLv2+
Url:		http://www.libimobiledevice.org/
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.bz2

BuildRequires:	make
BuildRequires:	python-cython
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(glib-2.0)

%description
libplist is a library for manipulating Apple Binary and XML Property Lists

%package -n %{libname}
Group:		System/Libraries
Summary:	Library for manipulating Apple Binary and XML Property Lists
Suggests:	%{name} >= %{version}-%{release}

%description -n %{libname}
libplist is a library for manipulating Apple Binary and XML Property Lists

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
C++ bindings for %{name}

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
%{name}, python libraries and support

%prep
%setup -q

%build

%configure2_5x \
	--disable-static

make

%install
%makeinstall_std 
# Fix bogus pkgconfig file
sed -i -e 's,/usr//,/,g;s,-L/usr/%{_lib} ,,g;/Cflags:/d' %{buildroot}%{_libdir}/pkgconfig/*.pc
# Apparently not seen by automatic stripping
strip %{buildroot}%{_libdir}/python*/site-packages/plist.so

# Temporary fix for broken buidl system. The package libimobiledevice will not build python bindingw without this
mkdir -p $RPM_BUILD_ROOT/usr/include/plist/cython
cp cython/plist.pxd $RPM_BUILD_ROOT/usr/include/plist/cython/


%files
%doc AUTHORS COPYING.LESSER README
%{_bindir}/plistutil

%files -n %{libname}
%{_libdir}/libplist.so.%{major}*

%files -n %{devname}
%{_includedir}/plist
%{_libdir}/pkgconfig/libplist.pc
%{_libdir}/libplist.so

%files -n %{libnamecxx}
%{_libdir}/libplist++.so.%{major}*

%files -n %{devnamecxx}
%exclude %{_includedir}/plist/plist.h
%{_libdir}/pkgconfig/libplist++.pc
%{_libdir}/libplist++.so

%files -n python-plist
%{python_sitearch}/plist.so

