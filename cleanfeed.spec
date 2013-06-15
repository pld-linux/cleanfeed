%include	/usr/lib/rpm/macros.perl
Summary:	INN spam filter
Summary(pl.UTF-8):	Filtr spamu dla INN-a
Name:		cleanfeed
%define		src_ver	20020501
Version:	20080809
Release:	3
License:	Artistic License 2.0
Group:		Networking/Daemons
Source0:	http://www.bofh.it/~md/cleanfeed/%{name}-%{src_ver}.tgz
# Source0-md5:	8535cc55d63a1932a447d09829b6aa97
Source1:	%{name}.8
# http://groups.google.pl/group/news.software.nntp/msg/e652742ab7ff0f0a
# http://www.mixmin.net/cleanfeed.diff
Patch0:		%{name}-%{version}.diff
Patch1:		%{name}-conf.patch
URL:		http://www.bofh.it/~md/cleanfeed/
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
%setup -q -n %{name}-%{src_ver}
%patch0 -p7
%patch1 -p1

%build
# INN 2.3.x hack
sed -i -e "s|\$lines = \$hdr{'__BODY__'} =~ tr/\\\n/\\\n/;|\$lines = \$hdr{'__LINES__'};|g" cleanfeed

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_mandir}/man8,%{_datadir}/news/filter}

install bad_adult_paths bad_hosts bad_cancel_paths bad_paths $RPM_BUILD_ROOT%{_sysconfdir}
install cleanfeed.local.sample $RPM_BUILD_ROOT%{_sysconfdir}/cleanfeed.local

install cleanfeed $RPM_BUILD_ROOT%{_datadir}/news/filter/filter_innd.pl
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES HACKING README TODO cleanfeed.local.sample-it highwind.pl tools
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bad_adult_paths
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bad_cancel_paths
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bad_hosts
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bad_paths
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/cleanfeed.local
%{_datadir}/news/filter/filter_innd.pl
%{_mandir}/man8/cleanfeed.8*
