#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	DNS-ZoneFile-Fast
Summary:	Net::DNS::ZoneFile::Fast - parse BIND8/9 zone files
Summary(pl):	Net::DNS::ZoneFile::Fast - analiza plik�w stref BIND-a 8/9
Name:		perl-Net-DNS-ZoneFile-Fast
Version:	0.5
Release:	1
License:	Beer-ware, distributable
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bf5071c30f2605e60bd5c519aa27920f
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Net-DNS
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

%description -l pl
Modu� Net::DNS::ZoneFile::Fast daje mo�liwo�� szybkiego przetwarzania
plik�w w formacie u�ywanym przez BIND-a 8 i 9. Aktualnie modu�
udost�pnia jedn� funkcj� - parse(), zwracaj�c� referencj� do tablicy
tradycyjnych obiekt�w Net::DNS::RR, dzi�ki czemu nie trzeba uczy� si�
nowego API, aby obrabia� rekordy stref.

Du�y nacisk zosta� po�o�ony na jak najwi�ksz� szybko�� wykonywania
parse(), wi�c szczeg�lnie interesuj�ce jest u�ywanie tego modu�u do
przetwarzania du�ych stref. Jako przyk�adowe dane mo�na poda�, �e
przetworzenie strefy o rozmiarze 2.2 MB, zawieraj�cej oko�o 72000
rekord�w na Athlonie XP 2600+ zaj�o poni�ej 5 sekund.

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
%doc Changes
%{perl_vendorlib}/Net/DNS/ZoneFile/*.pm
%{_mandir}/man3/*
