%define upstream_name	 XML-NamespaceSupport
%define upstream_version 1.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 5

Summary:	%{upstream_name} module for perl
License:	MPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module offers a simple to process namespaced XML names (unames) from
within any application that may need them. It also helps maintain a prefix
to namespace URI map, and provides a number of basic checks.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 644 Changes README

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps
%make

%check
%make test

%clean
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/XML/*.pm
%{_mandir}/*/*
