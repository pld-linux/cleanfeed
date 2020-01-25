Summary:	INN spam filter
Summary(pl.UTF-8):	Filtr spamu dla INN-a
Name:		cleanfeed
Version:	20100602
Release:	1
License:	Artistic v2.0
Group:		Networking/Daemons
#originally:	http://www.bofh.it/~md/cleanfeed/%{name}-%{src_ver}.tgz
# later maintained version:
#Source0Download: http://www.mixmin.net/cleanfeed/install.html
Source0:	http://www.mixmin.net/cleanfeed/%{name}.tar.gz
# Source0-md5:	8e14b5e306a9f875b8fcd6488584675a
Source1:	%{name}.8
Patch0:		%{name}-conf.patch
URL:		http://www.mixmin.net/cleanfeed/
BuildRequires:	rpm-perlprov
Requires:	perl-Digest-MD5
Conflicts:	inn < 2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/news

%description
Cleanfeed is an automatic filter for INN that removes spam from
incoming newsfeeds.

%description -l pl.UTF-8
Automatyczny filtr spamu dla serwera news INN. Usuwa spam z
przychodzących "feedów".

%prep
%setup -q -n %{name}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_mandir}/man8,%{_datadir}/news/filter}

install -p etc/bad_* etc/cleanfeed.local $RPM_BUILD_ROOT%{_sysconfdir}

install -p cleanfeed $RPM_BUILD_ROOT%{_datadir}/news/filter/filter_innd.pl
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bad_adult_paths
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bad_body
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bad_cancel_paths
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bad_from
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bad_groups
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bad_hosts
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bad_paths
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bad_subject
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bad_url
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/cleanfeed.local
%{_datadir}/news/filter/filter_innd.pl
%{_mandir}/man8/cleanfeed.8*
