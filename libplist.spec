%define name libplist
%define version 0.13
%define release %mkrel 1
%define major 0
%define libname %mklibname plist %major
%define libnamedev %mklibname -d plist

Name:           %{name}
Version:        %{version}
Release:        %mkrel 1
Summary:        Library for manipulating Apple Binary and XML Property Lists

Group:          System Environment/Libraries
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
Group: Development/Libraries
Requires: %libname = %version
Provides: %name-devel = %version-%release

%description -n %libnamedev
%{name}, development headers and libraries.

%package python
Summary: Python package for libplist
Group: Development/Libraries
%py_requires -d
Requires: python
BuildRequires: python-devel
BuildRequires: swig

%description python
%{name}, python libraries and support

%prep
%setup -q

%build
export CMAKE_PREFIX_PATH=/usr
%cmake

%make

%install
export CMAKE_PREFIX_PATH=/usr
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

# move python bindings to proper location
%{__mkdir} -pm 755 $RPM_BUILD_ROOT%{python_sitearch}
%{__mv} $RPM_BUILD_ROOT%{_libdir}/python/site-packages/libplist $RPM_BUILD_ROOT%{python_sitearch}

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
%{_bindir}/plutil-0.13

%files -n %libname
%defattr(-,root,root,-)
%{_libdir}/libplist.so.0
%{_libdir}/libplist.so.0.0.13

%files -n %libnamedev
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libplist.pc
%{_libdir}/libplist.so
%{_includedir}/plist

%files python
%defattr(-,root,root,-)
%{python_sitearch}/libplist

