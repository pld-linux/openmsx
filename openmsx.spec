# TODO
# - cc, optflags, %{__make} usage
Summary:	Open source MSX emulator
Summary(pl.UTF-8):	Emulator MSX o otwartych źródłach
Name:		openmsx
Version:	0.6.2
Release:	0.3
License:	GPL
Group:		Applications/Emulators
Source0:	http://dl.sourceforge.net/openmsx/%{name}-%{version}.tar.gz
# Source0-md5:	282acf2ea7bf67e15a7b8d961c9556a5
Patch0:		%{name}-optflags.patch
Patch1:		%{name}-config.patch
URL:		http://openmsx.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	libpng-devel
BuildRequires:	libxml2-devel
BuildRequires:	tcl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The open source MSX emulator that tries to achieve near-perfect
emulation by using a novel emulation model.

%description -l pl.UTF-8
Mający otwarte źródła emulator MSX próbujący osiągnąć prawie doskonałą
emulację poprzeez użycie nowego modelu emulacji.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

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
cp -r Contrib/cbios/C-BIOS_MSX1 $RPM_BUILD_ROOT%{_datadir}/openMSX/share/machines
cp -r Contrib/cbios/C-BIOS_MSX2 $RPM_BUILD_ROOT%{_datadir}/openMSX/share/machines
cp -r Contrib/cbios/C-BIOS_MSX2+ $RPM_BUILD_ROOT%{_datadir}/openMSX/share/machines

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README doc/*
%attr(755,root,root) %{_bindir}/openmsx
%{_datadir}/openMSX
