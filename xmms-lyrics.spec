Summary:	XMMS plugin for song lyrics displaying
Summary(pl):	Wtyczka do XMMS wy¶wietlaj±ca teksty piosenek
Name:		xmms-lyrics
Version:	cvs20000821
Release:	5
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-fixes.patch
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
XMMS plugin for song lyrics displaying. It has built-in tool for
inserting time-tags into lyrics.

%description -l pl
Wtyczka do XMMS wy¶wietlaj±ca teksty piosenek. Ma wbudowane narzêdzie
pozwalaj±ce wstawiaæ oznaczenia czasu do tekstów.

%prep
%setup  -q
%patch0 -p1

%build
autoheader
%{__autoconf}
automake -i

%configure
%{__make} "EXTRA_CFLAGS=%{rpmcflags} -DLOCALEDIR=\\\"%{_datadir}/locale\\\""

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README ChangeLog
%attr(755,root,root) %{_libdir}/xmms/General/*so
