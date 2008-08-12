%include	/usr/lib/rpm/macros.perl
Summary:	INN spam filter
Summary(pl.UTF-8):	Filtr spamu dla INN
Name:		cleanfeed
Version:	0.95.7b
Release:	15
License:	distributable
Group:		Networking/Daemons
Source0:	http://www.exit109.com/~jeremy/news/cleanfeed/%{name}-%{version}.tar.gz
# Source0-md5:	a715445b9fb13382a3d97bbbb64d638f
Patch0:		%{name}-conf.patch
URL:		http://www.exit109.com/~jeremy/news/cleanfeed/
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
%setup -q
%patch0 -p1

%build
# INN 2.3.x hack
sed -e "s|\$lines = \$hdr{'__BODY__'} =~ tr/\\\n/\\\n/;|\$lines = \$hdr{'__LINES__'};|g" \
	cleanfeed > cleanfeed.new

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_mandir}/man8,%{_datadir}/news/filter}

install cleanfeed.conf $RPM_BUILD_ROOT%{_sysconfdir}
install cleanfeed.8 $RPM_BUILD_ROOT%{_mandir}/man8/
install cleanfeed.new $RPM_BUILD_ROOT%{_datadir}/news/filter/filter_innd.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%{_datadir}/news/filter/filter_innd.pl
%{_mandir}/man8/*
