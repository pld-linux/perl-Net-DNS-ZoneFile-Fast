#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	DNS-ZoneFile-Fast
Summary:	Net::DNS::ZoneFile::Fast - parse BIND8/9 zone files
Summary(pl):	Net::DNS::ZoneFile::Fast - analiza plików stref BIND-a 8/9
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
Modu³ Net::DNS::ZoneFile::Fast daje mo¿liwo¶æ szybkiego przetwarzania
plików w formacie u¿ywanym przez BIND-a 8 i 9. Aktualnie modu³
udostêpnia jedn± funkcjê - parse(), zwracaj±c± referencjê do tablicy
tradycyjnych obiektów Net::DNS::RR, dziêki czemu nie trzeba uczyæ siê
nowego API, aby obrabiaæ rekordy stref.

Du¿y nacisk zosta³ po³o¿ony na jak najwiêksz± szybko¶æ wykonywania
parse(), wiêc szczególnie interesuj±ce jest u¿ywanie tego modu³u do
przetwarzania du¿ych stref. Jako przyk³adowe dane mo¿na podaæ, ¿e
przetworzenie strefy o rozmiarze 2.2 MB, zawieraj±cej oko³o 72000
rekordów na Athlonie XP 2600+ zajê³o poni¿ej 5 sekund.

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
