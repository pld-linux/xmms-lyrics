Summary:	XMMS plugin for song lyrics displaying
Summary(pl.UTF-8):   Wtyczka dla XMMS-a wyświetlająca teksty piosenek
Name:		xmms-lyrics
Version:	cvs20000821
Release:	7
License:	GPL
Group:		X11/Applications/Sound
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	a60be0aafbed1b113275041c95ba127f
Patch0:		%{name}-fixes.patch
Patch1:		%{name}-ac.patch
URL:		http://www.albedo.art.pl/~kbryd/plugin/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMMS plugin for song lyrics displaying. It has built-in tool for
inserting time-tags into lyrics.

%description -l pl.UTF-8
Wtyczka dla XMMS-a wyświetlająca teksty piosenek. Ma wbudowane
narzędzie pozwalające wstawiać oznaczenia czasu do tekstów.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
rm -rf missing
%{__autoheader}
%{__aclocal}
%{__autoconf}
%{__automake}

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
%attr(755,root,root) %{xmms_general_plugindir}/*so
