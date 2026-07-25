%define modname	XML-NamespaceSupport
%define modver	1.12

Summary:	%{modname} module for perl
Name:		perl-%{modname}
Version:	%{modver}
Release:	5
License:	MPL
Group:		Development/Perl
Url:		https://github.com/perigrin/xml-namespacesupport
Source0:	https://cpan.metacpan.org/authors/id/P/PE/PERIGRIN/XML-NamespaceSupport-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
This module offers a simple to process namespaced XML names (unames) from
within any application that may need them. It also helps maintain a prefix
to namespace URI map, and provides a number of basic checks.

%prep
%setup -qn %{modname}-%{modver}
chmod 644 Changes README

%build
%__perl Makefile.PL INSTALLDIRS=vendor --skipdeps
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/XML/*.pm
%{_mandir}/man3/*
