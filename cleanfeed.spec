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

install -d $RPM_BUILD_ROOT/{etc/news,%{_mandir}/man8,%{_libdir}/news/bin/control}

install cleanfeed.conf $RPM_BUILD_ROOT/etc/news/
install cleanfeed.8 $RPM_BUILD_ROOT%{_mandir}/man8/
install cleanfeed $RPM_BUILD_ROOT%{_libdir}/news/bin/control/filter_innd.pl

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/* \
	README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(640,news,news) %config(noreplace) %verify(not size mtime md5) /etc/news/*
%attr(750,news,news) %{_libdir}/news/bin/control/filter_innd.pl
%{_mandir}/man8/*
