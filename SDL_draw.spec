Summary:	Library to draw basic shapes on SDL surfaces
Summary(pl.UTF-8):	Biblioteka do rysowania podstawowych figur na powierzchniach SDL
Name:		SDL_draw
Version:	1.2.13
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://dl.sourceforge.net/project/sdl-draw/SDL_draw/1.2.13/%{name}-%{version}.tar.gz
# Source0-md5:	3f3e6985217e98d92cf5900a5d9f6444
URL:		http://sdl-draw.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SDL_draw is a simple library to draw basic elements, like points,
lines and circles, on SDL surfaces.

%description -l es.UTF-8
SDL_draw es una sencilla librería para representar primitivas básicas de
dibujo, como puntos, rectas y circunferencias, sobre una superficie SDL.

%description -l pl.UTF-8
SDL_draw jest prostą biblioteką do rysowania podstawowych figur
geometrycznych takich jak punkty, linie czy koła na powierzchniach
SDL.

%description -l pt.UTF-8
SDL_draw é uma biblioteca simples para desenhar elementos básicos, como
pontos, linhas e círculos, sobre uma superfície SDL.

%package devel
Summary:	Header files and more to develop SDL_draw applications
Summary(pl.UTF-8):	Pliki nagłówkowe do rozwijania aplikacji używających SDL_draw
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL-devel >= 1.2.0

%description devel
Header files and more to develop SDL_draw applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe do rozwijania aplikacji używających SDL_draw.

%package static
Summary:	Static SDL_draw libraries
Summary(pl.UTF-8):	Statyczne biblioteki SDL_draw
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Statis SDL_draw libraries.

%description static -l pl.UTF-8
Statyczne biblioteki SDL_draw.

%prep
%setup -q

rm -f acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/SDL}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install include/SDL_draw.h $RPM_BUILD_ROOT%{_includedir}/SDL

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libSDL_draw-*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libSDL_draw-1.2.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libSDL_draw.so
%{_libdir}/libSDL_draw.la
%{_includedir}/SDL/SDL_draw.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libSDL_draw.a
