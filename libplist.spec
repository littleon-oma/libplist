%define major 1
%define libname %mklibname plist %{major}
%define libnamedev %mklibname -d plist
%define libnamecxx %mklibname plist++ %{major}
%define libnamecxxdev %mklibname -d plist++

Name:		libplist
Version:	1.10
Release:	4
Summary:	Library for manipulating Apple Binary and XML Property Lists

Group:		System/Libraries
License:	LGPLv2+
URL:		http://www.libimobiledevice.org/

Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	python-cython
BuildRequires:	cmake

%description
libplist is a library for manipulating Apple Binary and XML Property Lists

%package -n %{libname}
Group:		System/Libraries
Summary:	Library for manipulating Apple Binary and XML Property Lists
Requires:	%{name} >= %{version}

%description -n %{libname}
libplist is a library for manipulating Apple Binary and XML Property Lists

%package -n %{libnamedev}
Summary:	Development package for libplist
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{libnamedev}
%{name}, development headers and libraries.

%package -n %{libnamecxx}
Summary:	C++ binding for libplist
Group:		Development/C++
Requires:	%{name} >= %{version}

%description -n %{libnamecxx}
C++ bindings for %{name}

%package -n %{libnamecxxdev}
Summary:	Development package for libplist++
Group:		Development/C++
Requires:	%{libnamecxx} = %{version}-%{release}
Provides:	%{name}++-devel = %{version}-%{release}
Conflicts:	%{mklibname plist++ 0} < 1.0

%description -n %{libnamecxxdev}
%name, C++ development headers and libraries.


%package -n python-plist
Summary:	Python package for libplist
Group:		Development/Python
%py_requires -d
Requires:	python
BuildRequires:	python-devel
BuildRequires:	swig

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
sed -i -e 's,/usr//,/,g;s,-L/usr/%{_lib} ,,g;/Cflags:/d' %{buildroot}%{_libdir}/pkgconfig/*.pc
# Apparently not seen by automatic stripping
strip %{buildroot}%{_libdir}/python*/site-packages/plist/_plist.so \
	%{buildroot}%{_libdir}/python*/site-packages/plist.so

%files
%doc AUTHORS COPYING.LESSER README
%{_bindir}/plistutil
%{_bindir}/plistutil-%{version}

%files -n %{libname}
%{_libdir}/libplist.so.%{major}*

%files -n %{libnamedev}
%{_includedir}/plist
%exclude %{_includedir}/plist/swig
%{_libdir}/pkgconfig/libplist.pc
%{_libdir}/libplist.so

%files -n %{libnamecxx}
%{_libdir}/libplist++.so.%{major}*

%files -n %{libnamecxxdev}
%{_includedir}/plist/swig
%exclude %{_includedir}/plist/plist.h
%{_libdir}/pkgconfig/libplist++.pc
%{_libdir}/libplist++.so

%files -n python-plist
%{python_sitearch}/plist
%{python_sitearch}/plist.so

%changelog
* Fri Mar 23 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.8-3
+ Revision: 786465
- Add python-cython build requirement

* Fri Mar 23 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.8-2
+ Revision: 786356
- Fix broken pkgconfig files

* Thu Feb 23 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.8-1
+ Revision: 779664
- Update to 1.8
- Remove some legacy constructs from spec file
- Update URLs

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4-2
+ Revision: 662404
- mass rebuild

* Tue Apr 05 2011 Funda Wang <fwang@mandriva.org> 1.4-1
+ Revision: 650568
- new version 1.4

* Wed Apr 28 2010 Christophe Fergeau <cfergeau@mandriva.com> 1.3-2mdv2011.0
+ Revision: 540035
- rebuild so that shared libraries are properly stripped again

* Tue Apr 20 2010 Christophe Fergeau <cfergeau@mandriva.com> 1.3-1mdv2010.1
+ Revision: 536948
- libplist 1.3

* Fri Feb 12 2010 Christophe Fergeau <cfergeau@mandriva.com> 1.2-1mdv2010.1
+ Revision: 504510
- libplist 1.2

* Mon Jan 11 2010 Christophe Fergeau <cfergeau@mandriva.com> 1.1-4mdv2010.1
+ Revision: 489608
- fix again Conflicts: between libplist++ and libplists++-devel

* Tue Dec 29 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.1-3mdv2010.1
+ Revision: 483261
- fix library name in Conflicts:

* Tue Dec 15 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.1-2mdv2010.1
+ Revision: 479034
- add Conflicts in libplist++-devel on older libplist++ since the latter used to ship the .so file

* Tue Dec 15 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.1-1mdv2010.1
+ Revision: 478857
- libplist 1.1

* Mon Dec 07 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0-1mdv2010.1
+ Revision: 474466
- libplist 1.0.0

* Fri Nov 06 2009 Colin Guthrie <cguthrie@mandriva.org> 0.16-1mdv2010.1
+ Revision: 460535
- New version: 0.16 (work by teuf)

* Thu Aug 06 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.13-2mdv2010.0
+ Revision: 410904
- fix name of python package

* Thu Aug 06 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.13-1mdv2010.0
+ Revision: 410622
- fix rpm groups
- import libplist


* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 11 2009 Peter Robinson <pbrobinson@gmail.com> 0.13-1
- New upstream 0.13 release

* Mon May 11 2009 Peter Robinson <pbrobinson@gmail.com> 0.12-2
- Further review updates

* Sun May 10 2009 Peter Robinson <pbrobinson@gmail.com> 0.12-1
- Update to official tarball release, some review fixes

* Sun May 10 2009 Peter Robinson <pbrobinson@gmail.com> 0.12.0-0.1
- Initial package
