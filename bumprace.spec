Summary:	A game
Summary(pl):	Gra
Name:		bumprace
Version:	1.45
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.linux-games.com/%{name}/%{name}-%{version}.tar.gz
#Source1:	%{name}.desktop
#Source2:	%{name}.png
URL:		http://www.linux-games.com/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel >= 1.2.0
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
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
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Games}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
#install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

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
