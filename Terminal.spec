%define		_name	Terminal
Summary:	X Terminal Emulator
Summary(pl):	Emulator terminala dla X
Name:		xfce4-terminal
Version:	0.2.0
Release:	0.1
License:	GPL v2
Group:		Applications/X11
Source:		http://download.berlios.de/xfce-goodies/%{_name}-%{version}.tar.bz2
URL:		http://www.os-cillation.com/
BuildRequires:	vte-devel >= 0.11.0
BuildRequires:	libexo-devel >= 0.2.0
BuildRequires:	sed >= 4.0
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
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
