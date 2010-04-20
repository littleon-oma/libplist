%define name libplist
%define version 1.3
%define release %mkrel 1
%define major 1
%define libname %mklibname plist %major
%define libnamedev %mklibname -d plist
%define libnamecxx %mklibname plist++ %major
%define libnamecxxdev %mklibname -d plist++

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Library for manipulating Apple Binary and XML Property Lists

Group:          System/Libraries
License:        LGPLv2+
URL:            http://matt.colyer.name/projects/iphone-linux/

Source0:        http://cloud.github.com/downloads/JonathanBeck/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: libxml2-devel
BuildRequires: glib2-devel
BuildRequires: cmake

%description
libplist is a library for manipulating Apple Binary and XML Property Lists

%package -n %libname
Group: System/Libraries
Summary: Library for manipulating Apple Binary and XML Property Lists
Requires: %name >= %version

%description -n %libname
libplist is a library for manipulating Apple Binary and XML Property Lists

%package -n %libnamedev
Summary: Development package for libplist
Group: Development/C
Requires: %libname = %version
Provides: %name-devel = %version-%release

%description -n %libnamedev
%{name}, development headers and libraries.

%package -n %libnamecxx
Summary: C++ binding for libplist
Group: Development/C++
Requires: %name >= %version

%description -n %libnamecxx
C++ bindings for %name

%package -n %libnamecxxdev
Summary: Development package for libplist++
Group: Development/C++
Requires: %libnamecxx = %version
%define libnamedev %mklibname -d plist
Provides: %name++-devel = %version-%release
Conflicts: %{mklibname plist++ 0} < 1.0

%description -n %libnamecxxdev
%name, C++ development headers and libraries.


%package -n python-plist
Summary: Python package for libplist
Group: Development/Python
%py_requires -d
Requires: python
BuildRequires: python-devel
BuildRequires: swig

%description -n python-plist
%{name}, python libraries and support

%prep
%setup -q

%build
export CMAKE_PREFIX_PATH=/usr
%cmake

%make

%install
#export CMAKE_PREFIX_PATH=/usr
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING.LESSER README
%{_bindir}/plutil
%{_bindir}/plutil-%{version}

%files -n %libname
%defattr(-,root,root,-)
%{_libdir}/libplist.so.%{major}*

%files -n %libnamedev
%defattr(-,root,root,-)
%{_includedir}/plist
%{_includedir}/plist/plist.h
%exclude %{_includedir}/plist/swig/*
%exclude %{_includedir}/plist/swig
%{_libdir}/pkgconfig/libplist.pc
%{_libdir}/libplist.so

%files -n %libnamecxx
%defattr(-,root,root,-)
%{_libdir}/libplist++.so.%{major}*

%files -n %libnamecxxdev
%defattr(-,root,root,-)
%{_includedir}/plist/swig
%exclude %{_includedir}/plist/plist.h
%{_libdir}/pkgconfig/libplist++.pc
%{_libdir}/libplist++.so

%files -n python-plist
%defattr(-,root,root,-)
%{python_sitearch}/plist

