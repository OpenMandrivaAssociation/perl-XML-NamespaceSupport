%define module	XML-NamespaceSupport
%define version 1.09
%define release %mkrel 3

Summary:	%{module} module for perl
Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
License:	MPL
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot/
Requires:	perl
BuildArch:	noarch

%description
This module offers a simple to process namespaced XML names (unames) from
within any application that may need them. It also helps maintain a prefix
to namespace URI map, and provides a number of basic checks.

%prep
%setup -q -n %{module}-%{version}

chmod 644 Changes README

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/XML/*.pm
%{_mandir}/*/*


