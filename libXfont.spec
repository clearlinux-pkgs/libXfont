#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libXfont
Version  : 1.5.1
Release  : 5
URL      : http://xorg.freedesktop.org/releases/individual/lib/libXfont-1.5.1.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libXfont-1.5.1.tar.gz
Summary  : X font Library
Group    : Development/Tools
License  : MIT
Requires: libXfont-lib
BuildRequires : pkgconfig(fontenc)
BuildRequires : pkgconfig(fontsproto)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)
BuildRequires : pkgconfig(xtrans)
BuildRequires : xmlto

%description
libXfont provides the core of the legacy X11 font system, handling the
index files (fonts.dir, fonts.alias, fonts.scale), the various font file
formats, and rasterizing them.   It is used by the X servers, the
X Font Server (xfs), and some font utilities (bdftopcf for instance),
but should not be used by normal X11 clients.  X11 clients access fonts
via either the new API's in libXft, or the legacy API's in libX11.

%package dev
Summary: dev components for the libXfont package.
Group: Development
Requires: libXfont-lib

%description dev
dev components for the libXfont package.


%package lib
Summary: lib components for the libXfont package.
Group: Libraries

%description lib
lib components for the libXfont package.


%prep
%setup -q -n libXfont-1.5.1

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/fonts/bdfint.h
/usr/include/X11/fonts/bitmap.h
/usr/include/X11/fonts/bufio.h
/usr/include/X11/fonts/fntfil.h
/usr/include/X11/fonts/fntfilio.h
/usr/include/X11/fonts/fntfilst.h
/usr/include/X11/fonts/fontconf.h
/usr/include/X11/fonts/fontencc.h
/usr/include/X11/fonts/fontmisc.h
/usr/include/X11/fonts/fontshow.h
/usr/include/X11/fonts/fontutil.h
/usr/include/X11/fonts/fontxlfd.h
/usr/include/X11/fonts/ft.h
/usr/include/X11/fonts/ftfuncs.h
/usr/include/X11/fonts/pcf.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
