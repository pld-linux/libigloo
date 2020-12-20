#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	Common C framework by the Icecast project
Summary(pl.UTF-8):	Wspólny szkielet C z projektu Icecast
Name:		libigloo
Version:	0.9.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/igloo/%{name}-%{version}.tar.gz
# Source0-md5:	b2bf1cee104f84979e7d3a41930d6632
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libigloo is a generic C framework. It is developed and used by the
Icecast project.

%description -l pl.UTF-8
libigloo to ogólny szkielet C. Jest tworzony i używany przez projekt
Icecast.

%package devel
Summary:	Header files for igloo library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki igloo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for igloo library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki igloo.

%package static
Summary:	Static igloo library
Summary(pl.UTF-8):	Statyczna biblioteka igloo
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static igloo library.

%description static -l pl.UTF-8
Statyczna biblioteka igloo.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libigloo.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libigloo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libigloo.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libigloo.so
%{_includedir}/igloo
%{_pkgconfigdir}/igloo.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libigloo.a
%endif
