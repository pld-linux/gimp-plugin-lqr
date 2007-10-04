Summary:	Liquid Rescale GIMP Plug-In
Name:		gimp-plugin-lqr
Version:	0.2.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://liquidrescale.wikidot.com/local--files/en:download-page/gimp-lqr-plugin-%{version}.tar.gz
# Source0-md5:	574ed430b552a34bc832a4760d35965c
URL:		http://liquidrescale.wikidot.com/
BuildRequires:	gettext-devel
BuildRequires:	gimp-devel >= 1:2.3.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	rpmbuild(macros) >= 1.198
Requires:	gimp >= 1:2.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin aims at resizing pictures non uniformly while preserving
their features, i.e. avoiding distortion of the important parts.
It supports manual feature selection, and can also be used to
remove portions of the picture in a consistent way.

%prep
%setup -q -n gimp-lqr-plugin-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang gimp22-lqr-plugin

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gimp22-lqr-plugin.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog BUGS README TODO
%attr(755,root,root) %(gimptool --gimpplugindir)/plug-ins/gimp-lqr-plugin
%{_datadir}/gimp-lqr-plugin
