Summary:	X Terminal Emulator
Summary(pl):	Emulator terminala dla X
Name:		Terminal
Version:	0.2.0
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.bz2
# Source0-md5:	ddeffad55dd20d9ef77ef148d02cecb1
URL:		http://www.os-cillation.com/
BuildRequires:	dbus-glib-devel >= 0.22
BuildRequires:	gcc-c++
BuildRequires:	gettext-devel
BuildRequires:	libexo-devel >= 0.2.0
BuildRequires:	libxfcegui4-devel >= 4.1.90
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	vte-devel >= 0.11.0
Obsoletes:	xfce4-terminal
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Advanced lightweight Terminal Emulator for the X windowing system.

%description -l pl
Zaawansowany emulator terminala dla systemu X Window.

%prep
%setup -q

%build
%{__sed} -i 's@System;TerminalEmulator;@TerminalEmulator;@' Terminal.desktop
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/TerminalHelp
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_docdir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}*
%{_mandir}/man1/%{name}*
%{_pixmapsdir}/*
