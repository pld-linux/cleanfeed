%include	/usr/lib/rpm/macros.perl
Summary:	INN spam filter
Summary(pl.UTF-8):	Filtr spamu dla INN
Name:		cleanfeed
%define		_srcver	20020501
%define		_ver	20080809
Version:	%{_ver}
Release:	1
License:	Artistic License 2.0
Group:		Networking/Daemons
Source0:	http://www.bofh.it/~md/cleanfeed/%{name}-%{_srcver}.tgz
# Source0-md5:	8535cc55d63a1932a447d09829b6aa97
# http://groups.google.pl/group/news.software.nntp/msg/e652742ab7ff0f0a
# http://www.mixmin.net/cleanfeed.diff
Patch0:		%{name}-%{_ver}.diff
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
Automatyczny filtr spamu dla serwerów news.

%prep
%setup -q -n %{name}-%{_srcver}
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

install cleanfeed.8 $RPM_BUILD_ROOT%{_mandir}/man8/
install cleanfeed $RPM_BUILD_ROOT%{_datadir}/news/filter/filter_innd.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES HACKING README TODO cleanfeed.local.sample-it highwind.pl tools
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%{_datadir}/news/filter/filter_innd.pl
%{_mandir}/man8/*
