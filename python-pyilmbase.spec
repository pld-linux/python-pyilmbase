Summary:	Python bindings for the IlmBase libraries
Summary(pl.UTF-8):	Wiązania Pythona do bibliotek IlmBase
Name:		python-pyilmbase
Version:	2.0.0
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	http://download.savannah.gnu.org/releases/openexr/pyilmbase-%{version}.tar.gz
# Source0-md5:	4585eba94a82f0b0916445990a47d143
URL:		http://www.openexr.com/
BuildRequires:	boost-python-devel
BuildRequires:	ilmbase-devel >= 2.0.0
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

%description devel
Header files for IlmBase Python bindings.

%description devel -l pl.UTF-8
Pliki nagłówkowe wiązań Pyhona do bibliotek IlmBase.

%prep
%setup -q -n pyilmbase-%{version}

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
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
