Summary:	Ping test plugin for GKrellM
Summary(pl.UTF-8):	Wtyczka ping dla GKrellM
Name:		gkrellm-amiconnected
Version:	0.7.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://chrisk.homelinux.net/amiconnected/%{name}-%{version}.tar.bz2
# Source0-md5	2ac683e4c948f5c44b9fd56b485ffc7b
URL:		http://chrisk.homelinux.net/amiconnected/
BuildRequires:	gkrellm-devel >= 2.0
BuildRequires:	gtk+2-devel
BuildRequires:	pkgconfig
Requires:	gkrellm >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Amiconnected is a GKrellM plugin that uses the standard ping binary
to ping multiple IPs and display a summary of the results.

%description -l pl.UTF-8
Amiconnected jest wtyczką GKrellM, która wykonuje test na hostach
używając standardowego programu ping.

%prep
%setup -q -n %{name}-0.7

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -D amiconnected.so $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins/amiconnected.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gkrellm2/plugins/amiconnected.so
