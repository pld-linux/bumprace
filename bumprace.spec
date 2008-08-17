#
# Conditional build:
%bcond_without	SDL_mixer	# build without SDL_mixer
#
Summary:	A funny action game written with SDL
Summary(pl.UTF-8):	Zabawna gra oparta o SDL
Name:		bumprace
Version:	1.5.3
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://user.cs.tu-berlin.de/~karlb/bumprace/%{name}-%{version}.tar.gz
# Source0-md5:	a72733718ee6eed8cd1657db89bf8e0d
Source1:	%{name}.desktop
Source2:	%{name}.xpm
URL:		http://www.linux-games.com/bumprace/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_image-devel >= 1.2.0
%{?with_SDL_mixer:BuildRequires:	SDL_mixer-devel >= 1.2.0}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BumpRace is a simple 1 or 2 player game where players choose among
four vehicles and race through a multi-level maze.

%description -l pl.UTF-8
BumpRace jest prostą grą dla 1 lub 2 osób, w której gracze wybierają
spośród czterech pojazdów i ścigają się w wielopoziomowym labiryncie.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ README 
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
