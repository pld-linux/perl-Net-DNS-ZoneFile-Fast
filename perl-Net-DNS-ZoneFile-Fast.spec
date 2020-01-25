#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Net
%define	pnam	DNS-ZoneFile-Fast
Summary:	Net::DNS::ZoneFile::Fast - parse BIND8/9 zone files
Summary(pl.UTF-8):	Net::DNS::ZoneFile::Fast - analiza plików stref BIND-a 8/9
Name:		perl-Net-DNS-ZoneFile-Fast
Version:	1.11
Release:	1
License:	Beer-ware, distributable
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ad21b01a5a60fab79c18e55ae5a0406a
URL:		http://search.cpan.org/dist/Net-DNS-ZoneFile-Fast/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Net::DNS::SEC) >= 0.15
BuildRequires:	perl-Net-DNS >= 0.65
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Net::DNS::ZoneFile::Fast module provides an ability to parse zone
files that BIND8 and BIND9 use, fast. Currently it provides a single
function, parse(), which returns a reference to an array of
traditional Net::DNS::RR objects, so that no new API has to be learned
in order to manipulate zone records.

Great care was taken to ensure that parse() does its job as fast as
possible, so it is interesting to use this module to parse huge zones.
As an example datapoint, it takes less than 5 seconds to parse a 2.2
MB zone with about 72000 records on an Athlon XP 2600+ box.

%description -l pl.UTF-8
Moduł Net::DNS::ZoneFile::Fast daje możliwość szybkiego przetwarzania
plików w formacie używanym przez BIND-a 8 i 9. Aktualnie moduł
udostępnia jedną funkcję - parse(), zwracającą referencję do tablicy
tradycyjnych obiektów Net::DNS::RR, dzięki czemu nie trzeba uczyć się
nowego API, aby obrabiać rekordy stref.

Duży nacisk został położony na jak największą szybkość wykonywania
parse(), więc szczególnie interesujące jest używanie tego modułu do
przetwarzania dużych stref. Jako przykładowe dane można podać, że
przetworzenie strefy o rozmiarze 2.2 MB, zawierającej około 72000
rekordów na Athlonie XP 2600+ zajęło poniżej 5 sekund.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Net/DNS/ZoneFile
%{perl_vendorlib}/Net/DNS/ZoneFile/*.pm
%{_mandir}/man3/*
