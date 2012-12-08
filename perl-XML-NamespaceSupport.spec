%define upstream_name	 XML-NamespaceSupport
%define upstream_version 1.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    6

Summary:	%{upstream_name} module for perl
License:	MPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires: perl-devel
BuildArch:	noarch


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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.110.0-5mdv2012.0
+ Revision: 765847
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.110.0-4
+ Revision: 764371
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 1.110.0-3
+ Revision: 763116
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.110.0-2
+ Revision: 667449
- mass rebuild

* Wed Mar 17 2010 Jérôme Quelin <jquelin@mandriva.org> 1.110.0-1mdv2011.0
+ Revision: 523959
- update to 1.11

* Wed Jan 06 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-2mdv2010.1
+ Revision: 486739
- rebuild
- prevent module::install to try to be smart

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-1mdv2010.0
+ Revision: 408242
- rebuild using %%perl_convert_version

* Thu Jun 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-1mdv2010.0
+ Revision: 387039
- update to new version 1.10

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.09-6mdv2009.1
+ Revision: 351684
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.09-5mdv2009.0
+ Revision: 224637
- rebuild

* Fri Jan 11 2008 Pixel <pixel@mandriva.com> 1.09-4mdv2008.1
+ Revision: 147990
- do not require perl, perl-base is enough (esp. for urpmi now using perl-XML-LibXML)

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 16 2007 Thierry Vignaud <tv@mandriva.org> 1.09-3mdv2008.0
+ Revision: 64203
- rebuild


* Sat Jan 13 2007 Olivier Thauvin <nanardon@mandriva.org> 1.09-2mdv2007.0
+ Revision: 108396
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-XML-NamespaceSupport

* Fri Jun 10 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.09-1mdk
- 1.09
- misc spec fixes

* Tue Jan 18 2005 Abel Cheung <deaddog@mandrake.org> 1.08-4mdk
- rebuild

