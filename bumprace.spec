Summary:	A game
Summary(pl):	Gra
Name:		bumprace
Version:	1.45
Release:	1
License:	GPL
Group:		X11/Applications/Games
Group(cs):	X11/Aplikace/Hry
Group(da):	X11/Programmer/Spil
Group(de):	X11/Applikationen/Spiele
Group(es):	X11/Aplicaciones/Juegos
Group(fr):	X11/Applications/Jeux
Group(is):	X11/Forrit/Leikir
Group(it):	X11/Applicazioni/Giochi
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó/¥²¡¼¥à
Group(no):	X11/Applikasjoner/Spill
Group(pl):	X11/Aplikacje/Gry
Group(pt):	X11/Aplicações/Jogos
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ/éÇÒÙ
Group(sl):	X11/Programi/Igre
Group(sv):	X11/Tillämpningar/Spel
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ/¶ÇÒÉ
Source0:	http://www.linux-games.com/%{name}/%{name}-%{version}.tar.gz
#Source1:	%{name}.desktop
#Source2:	%{name}.png
URL:		http://www.linux-games.com/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This is a clone of the classic "Black Box" Game, but it has better
graphics and music.

%description -l pl
To jest klon klasycznej gry "Black Box", lecz ma lepsz± grafikê i
muzykê.

%prep
%setup -q

%build
rm -f missing
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Games}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#%{__install} %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
#%{__install} %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

gzip -9nf NEWS README AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
#%{_mandir}/man6/*
%{_datadir}/%{name}
#%{_pixmapsdir}/*
#%{_applnkdir}/Games/*
