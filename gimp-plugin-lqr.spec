Summary:	Liquid Rescale GIMP Plug-In
Summary(pl.UTF-8):	Wtyczka Liquid Rescale (ciekłego skalowania) dla GIMP-a
Name:		gimp-plugin-lqr
Version:	0.5.0
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://liquidrescale.wikidot.com/local--files/en:download-page/gimp-lqr-plugin-%{version}.tar.bz2
# Source0-md5:	a627d56c6622a3e3bb4a2ce41d7002dd
Patch0:		%{name}-locale_names.patch
URL:		http://liquidrescale.wikidot.com/
BuildRequires:	gettext-devel
BuildRequires:	gimp-devel >= 1:2.3.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	intltool
BuildRequires:	liblqr-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
Requires:	gimp >= 1:2.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin aims at resizing pictures non uniformly while preserving
their features, i.e. avoiding distortion of the important parts. It
supports manual feature selection, and can also be used to remove
portions of the picture in a consistent way.

%description -l pl.UTF-8
Ta wtyczka jest przeznaczona do niejednostajnego skalowania obrazów z
zachowaniem ich cech, tzn. unikając zniekształcania ważnych elementów.
Obsługuje ręczny wybór cech i może być używana do usuwania części
obrazu w sposób spójny.

%prep
%setup -q -n gimp-lqr-plugin-%{version}
%patch0 -p1
mv -f po/{eu_ES,eu}.po
mv -f po/{es_ES,es}.po
mv -f po/{ro_RO,ro}.po

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
