#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	File
%define		pnam	Listing
%include	/usr/lib/rpm/macros.perl
Summary:	File::Listing - parse directory listing
Summary(pl.UTF-8):	File::Listing - analiza listingu katalogu
Name:		perl-File-Listing
Version:	6.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ad56d06a719503198c02188995f32c9e
URL:		http://search.cpan.org/dist/File-Listing/
BuildRequires:	perl-devel >= 1:5.8.8
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTTP-Date >= 6
%endif
Requires:	perl-HTTP-Date >= 6
Conflicts:	perl-libwww < 6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module exports a single function called parse_dir(), which can be
used to parse directory listings.

%description -l pl.UTF-8
Ten moduł eksportuje jedną funkcję: parse_dir(), służącą do analizy
listingów katalogów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/File/Listing.pm
%{_mandir}/man3/File::Listing.3pm*
