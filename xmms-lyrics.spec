Summary:	XMMS plugin for song lyrics displaying
Summary(pl):	Wtyczka do XMMS wy¶wietlaj±ca teksty piosenek
Name:		xmms-lyrics
Version:	cvs20000821
Release:	2
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
License:	GPL
Source0:	%{name}-%{version}.tar.gz
URL:		http://www.albedo.art.pl/~kbryd/plugin/
Requires:	xmms
BuildRequires:	xmms-devel
BuildRequires:	gtk+-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
XMMS plugin for song lyrics displaying. It has built-in too for
insering time-tags into lyrics.

%description -l pl
Wtyczka do XMMS wy¶wietlaj±ca teksty piosenek. Ma wbudowane narzêdzie
pozwalaj±ce wstawiaæ oznaczenia czasu do tekstów.

%prep
%setup  -q

%build
autoheader; autoconf; automake

%configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

gzip -9nf AUTHORS NEWS README ChangeLog 

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/xmms/General/*so
