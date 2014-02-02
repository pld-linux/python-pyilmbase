Summary:	Python bindings for the IlmBase libraries
Summary(pl.UTF-8):	Wiązania Pythona do bibliotek IlmBase
Name:		python-pyilmbase
Version:	2.0.1
Release:	2
License:	BSD
Group:		Libraries/Python
Source0:	http://download.savannah.gnu.org/releases/openexr/pyilmbase-%{version}.tar.gz
# Source0-md5:	b2e3154df90014e30fd5fb89d00de111
Patch0:		%{name}-link.patch
Patch1:		%{name}-am.patch
URL:		http://www.openexr.com/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.6.3
BuildRequires:	boost-python-devel
BuildRequires:	ilmbase-devel >= 2.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	python-numpy-devel
BuildRequires:	rpm-pythonprov
Requires:	ilmbase >= 2.0.0
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PyIlmBase package provides python bindings for the IlmBase
libraries.

%description -l pl.UTF-8
Pakiet PyIlmBase dostarcza wiązania Pythona do bibliotek IlmBase.

%package devel
Summary:	Header files for IlmBase Python bindings
Summary(pl.UTF-8):	Pliki nagłówkowe wiązań Pyhona do bibliotek IlmBase
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	boost-python-devel
Requires:	ilmbase-devel >= 2.0.0
Requires:	libstdc++-devel

%description devel
Header files for IlmBase Python bindings.

%description devel -l pl.UTF-8
Pliki nagłówkowe wiązań Pyhona do bibliotek IlmBase.

%prep
%setup -q -n pyilmbase-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure

# g++ eats a lot of memory, don't run many in parallel
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

# parallel build fails at libPyImath/imathmodule install
%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libPy*.la \
	$RPM_BUILD_ROOT%{py_sitedir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libPyIex.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libPyIex.so.2
%attr(755,root,root) %{_libdir}/libPyImath.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libPyImath.so.2
%attr(755,root,root) %{py_sitedir}/iexmodule.so
%attr(755,root,root) %{py_sitedir}/imathmodule.so
%attr(755,root,root) %{py_sitedir}/imathnumpymodule.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libPyIex.so
%attr(755,root,root) %{_libdir}/libPyImath.so
%{_includedir}/OpenEXR/PyIex*.h
%{_includedir}/OpenEXR/PyIlmBaseConfig.h
%{_includedir}/OpenEXR/PyImath*.h
%{_pkgconfigdir}/PyIlmBase.pc
%{_aclocaldir}/pyilmbase.m4
