Summary:	INN spam filter
Summary(pl):	Filtr spamu dla INN
Name:		cleanfeed
Version:	0.95.7b
Release:	3
Copyright:	distributable
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Source0:	ftp://ftp.exit109.com/users/jeremy/%{name}-%{version}.tar.gz
Patch0:		cleanfeed-conf.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	perl-Digest-MD5
Buildarch:	noarch

%define		_sysconfdir	/etc/news

%description
Cleanfeed is an automatic filter for INN that removes spam from
incoming newsfeeds.

%description -l pl
Automatyczny filtr spamu dla serwerów news.

%prep
%setup -q
%patch -p1 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{%{_sysconfdir},%{_mandir}/man8,%{_datadir}/news/filter}

install cleanfeed.conf $RPM_BUILD_ROOT%{_sysconfdir}
install cleanfeed.8 $RPM_BUILD_ROOT%{_mandir}/man8/
install cleanfeed $RPM_BUILD_ROOT%{_datadir}/news/filter/filter_innd.pl

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/* \
	README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(640,root,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
%{_datadir}/news/filter/filter_innd.pl
%{_mandir}/man8/*
