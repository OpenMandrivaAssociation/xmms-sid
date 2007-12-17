%define pre beta17
Summary: XMMS input plugin for C64 SID files
Name: xmms-sid
Version: 0.8.0
Release: %mkrel 0.%pre.1
Source: %{name}-%{version}%pre.tar.bz2
License: GPL
Group: Sound
URL: http://www.tnsp.org/xmms-sid.php
Requires: xmms 
BuildRequires: sidplay-devel
BuildRequires: sidplay2-devel
BuildRequires: libxmms-devel

%description
XMMS-SID is a plugin for XMMS (X MultiMedia System) which provides
support for playing the so-called "SID tunes", which are music
from old Commodore computer programs like games, demos, etc.

For the actual playing, XMMS-SID uses the excellent libsidplay (1|2)
emulator engine that emulates 6510 CPU and 6581/8580 Sound Interface
Device (SID) chip.

%prep
%setup -q -n %name-%version%pre

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%_libdir/xmms/Input/libxmmssid.la
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README* TODO
%{_libdir}/xmms/Input/libxmmssid.so


