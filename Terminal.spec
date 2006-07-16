#
%define		pre		beta2
%define		xfce_version	4.3.90.2
#
Summary:	X Terminal Emulator
Summary(pl):	Emulator terminala dla X
Name:		Terminal
Version:	0.2.5.4
Release:	0.%{pre}.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce-%{xfce_version}/src/%{name}-%{version}%{pre}.tar.bz2
# Source0-md5:	9f129b5d143a707394aa7aa139a67afa
URL:		http://www.os-cillation.com/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.62
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	intltool >= 0.35
BuildRequires:	libexo-devel >= 0.3.1.8
BuildRequires:	libtool
BuildRequires:	libxfcegui4-devel >= %{xfce_version}
BuildRequires:	ncurses-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	vte-devel >= 0.13.3
BuildRequires:	xfce4-dev-tools >= %{xfce_version}
Requires(post,postun):	gtk+2 >= 2:2.10.0
Obsoletes:	xfce4-terminal
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Advanced lightweight Terminal Emulator for the X windowing system.

%description -l pl
Zaawansowany emulator terminala dla systemu X Window.

%prep
%setup -q -n %{name}-%{version}%{pre}

%build
%{__sed} -i 's,Categories.*,Categories=GTK;TerminalEmulator;,' Terminal.desktop.in
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
LDFLAGS="%{rpmldflags} -Wl,--as-needed"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor

%postun
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/TerminalHelp
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}*
%{_iconsdir}/hicolor/*/stock/navigation/*
%{_pixmapsdir}/*

%dir %{_docdir}/%{name}
%{_docdir}/%{name}/C
%{_docdir}/%{name}/*.css
%lang(ja) %{_docdir}/%{name}/ja
%{_mandir}/man1/%{name}*
