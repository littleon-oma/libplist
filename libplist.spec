%define major 1
%define libname %mklibname plist %major
%define libnamedev %mklibname -d plist
%define libnamecxx %mklibname plist++ %major
%define libnamecxxdev %mklibname -d plist++

Name:           libplist
Version:        1.8
Release:        2
Summary:        Library for manipulating Apple Binary and XML Property Lists

Group:          System/Libraries
License:        LGPLv2+
URL:            http://www.libimobiledevice.org/

Source0:        http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.bz2

BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: python-cython
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
rm -rf %{buildroot}
%makeinstall_std -C build
# Fix bogus pkgconfig file
sed -i -e 's,/usr//,/,g;s,-L/usr/%_lib ,,g;/Cflags:/d' %buildroot%_libdir/pkgconfig/*.pc
# Apparently not seen by automatic stripping
strip %buildroot%_libdir/python*/site-packages/plist/_plist.so \
	%buildroot%_libdir/python*/site-packages/plist.so

%clean
rm -rf %{buildroot}

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
%{python_sitearch}/plist.so

