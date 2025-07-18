
# Obsoleted by xfce4-terminal

%define		xfce_version	4.6.1
Summary:	X Terminal Emulator
Summary(pl.UTF-8):	Emulator terminala dla X
Name:		Terminal
Version:	0.4.8
Release:	4
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/apps/terminal/0.4/%{name}-%{version}.tar.bz2
# Source0-md5:	8dff62234da14e1a5e542fb56560ebe2
Patch0:		%{name}-desktop.patch
Patch1:		wordseps.patch
URL:		http://www.xfce.org/projects/terminal/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-glib-devel >= 0.62
BuildRequires:	exo-devel >= 0.3.101
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	vte0-devel >= 0.17.1
BuildRequires:	xfce4-dev-tools >= 4.6.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Obsoletes:	xfce4-terminal
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Advanced lightweight Terminal Emulator for the X windowing system.

%description -l pl.UTF-8
Zaawansowany emulator terminala dla systemu X Window.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

# already present as ur
%{__sed} -i 's,ur_PK ,,' configure.ac

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--enable-dbus

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README THANKS
%attr(755,root,root) %{_bindir}/Terminal
%attr(755,root,root) %{_bindir}/terminal
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}*
%{_iconsdir}/hicolor/*/stock/navigation/*.png
%{_pixmapsdir}/*.xpm

%dir %{_docdir}/%{name}
%{_docdir}/%{name}/C
%{_docdir}/%{name}/*.css
%lang(ca) %{_docdir}/%{name}/ca
%lang(da) %{_docdir}/%{name}/da
%lang(el) %{_docdir}/%{name}/el
%lang(es) %{_docdir}/%{name}/es
%lang(fr) %{_docdir}/%{name}/fr
%lang(gl) %{_docdir}/%{name}/gl
%lang(id) %{_docdir}/%{name}/id
%lang(it) %{_docdir}/%{name}/it
%lang(ja) %{_docdir}/%{name}/ja
%lang(pt) %{_docdir}/%{name}/pt
%lang(ru) %{_docdir}/%{name}/ru
%lang(sv) %{_docdir}/%{name}/sv
%lang(ug) %{_docdir}/%{name}/ug
%lang(zh_CN) %{_docdir}/%{name}/zh_CN
%{_mandir}/man1/%{name}*
%lang(ca) %{_mandir}/ca/man1/%{name}*
%lang(da) %{_mandir}/da/man1/%{name}*
%lang(el) %{_mandir}/el/man1/%{name}*
%lang(es) %{_mandir}/es/man1/%{name}*
%lang(fr) %{_mandir}/fr/man1/%{name}*
%lang(gl) %{_mandir}/gl/man1/%{name}*
%lang(id) %{_mandir}/id/man1/%{name}*
%lang(it) %{_mandir}/it/man1/%{name}*
%lang(ja) %{_mandir}/ja/man1/%{name}*
%lang(pt) %{_mandir}/pt/man1/%{name}*
%lang(ru) %{_mandir}/ru/man1/%{name}*
%lang(sv) %{_mandir}/sv/man1/%{name}*
#%lang(ug) %{_mandir}/ug/man1/%{name}*
%lang(zh_CN) %{_mandir}/zh_CN/man1/%{name}*
