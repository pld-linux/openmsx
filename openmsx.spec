Summary:	Open source MSX emulator
Name:		openmsx
Version:	0.6.2
Release:	0.1
Source0:	http://dl.sourceforge.net/openmsx/%{name}-%{version}.tar.gz
# Source0-md5:	282acf2ea7bf67e15a7b8d961c9556a5
Patch0:		%{name}-optflags.patch
License:	GPL
Group:		Applications/Emulators
URL:		http://openmsx.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	XFree86-OpenGL-devel
BuildRequires:	libpng-devel
BuildRequires:	libxml2-devel
BuildRequires:	tcl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The open source MSX emulator that tries to achieve near-perfect
emulation by using a novel emulation model.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

# install bin files
install -d $RPM_BUILD_ROOT%{_bindir}
cp derived/*/bin/openmsx $RPM_BUILD_ROOT%{_bindir}/openmsx

# install c-bios
install -d $RPM_BUILD_ROOT%{_datadir}/openMSX/share/machines
cp -r share $RPM_BUILD_ROOT%{_datadir}/openMSX
cp -r Contrib/cbios/C-BIOS_MSX1/ $RPM_BUILD_ROOT%{_datadir}/openMSX/share/machines
cp -r Contrib/cbios/C-BIOS_MSX2/ $RPM_BUILD_ROOT%{_datadir}/openMSX/share/machines
cp -r Contrib/cbios/C-BIOS_MSX2+/ $RPM_BUILD_ROOT%{_datadir}/openMSX/share/machines

# menu
install -d $RPM_BUILD_ROOT%{_menudir}
cat > $RPM_BUILD_ROOT%{_menudir}/%{name} <<EOF
?package(%{name}): \
   command="%{_bindir}/openmsx" \
   icon="emulators_section.png" \
   title="Openmsx" \
   longtitle="%{summary}" \
   needs="x11" \
   section="More Applications/Emulators"
EOF

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog GPL README TODO doc/*
%attr(755,root,root) %{_bindir}/openmsx
%{_datadir}/openMSX/share/*
%_menudir/%{name}
