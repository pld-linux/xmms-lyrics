Summary:	XMMS plugin for song lyrics displaying
Summary(pl):	Wtyczka do XMMS wy¶wietlaj±ca teksty piosenek
Name:		xmms-lyrics
Version:	cvs20000803
Release:	1
Group:		X11/Applications/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
License:	GPL
Source0:	%{name}-%{version}.tar.gz
URL:		http://iwaki.ahoj.pl/~kbryd
Requires:	xmms
BuildRequires:	xmms-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
XMMS plugin for song lyrics displaying. It has built-in too for insering
time-tags into lyrics.

%description -l pl
Wtyczka do XMMS wy¶wietlaj±ca teksty piosenek. Ma wbudowane narzêdzie
pozwalaj±ce wstawiaæ oznaczenia czasu do tekstów.

%prep
%setup  -q

%build
autoheader
autoconf
# Ugly, but works ;/
automake || :

LDFLAGS="-s" ; export LDFLAGS
%configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

gzip -9nf README ChangeLog 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/xmms/General/*so
