Summary:	INN spam filter
Summary(pl):    Filtr spamu dla INN
Name:		cleanfeed
Version:	0.95.7b
Release:	2
Copyright:	distributable
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Source:		ftp://ftp.exit109.com/users/jeremy/%{name}-%{version}.tar.gz
Patch:		cleanfeed-conf.patch
Buildroot:	/tmp/%{name}-%{version}-root
Requires:	perl-MD5
Buildarch:	noarch

%description
Cleanfeed is an automatic filter for INN that removes spam from incoming
newsfeeds.

%description -l pl
Automatyczny filtr spamu dla serwer�w news.

%prep
%setup -q
%patch -p1 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{etc/news,usr/{man/man8,lib/news/bin/control}}

install cleanfeed.conf $RPM_BUILD_ROOT/etc/news/
install cleanfeed.8 $RPM_BUILD_ROOT%{_mandir}/man8/
install cleanfeed $RPM_BUILD_ROOT/usr/lib/news/bin/control/filter_innd.pl

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/* \
	README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(640,news,news) %config(noreplace) %verify(not size mtime md5) /etc/news/*
%attr(750,news,news) /usr/lib/news/bin/control/filter_innd.pl
%{_mandir}/man8/*

%changelog
* Wed Dec 09 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [0.95.7b-2]
- build for PLD Tornado,
- rewrote spec file.

* Thu Sep 03 1998 Cristian Gafton <gafton@redhat.com>
- update to 0.95.7b

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- spec file cleanups
- patch to get rod of /usr/local/bin/perl

* Mon Apr 13 1998 Bryan C. Andregg <bandregg@redhat.com>
- first package
