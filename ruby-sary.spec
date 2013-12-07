%define rname sary

Summary:	Ruby Binding of Sary
Name:		ruby-%{rname}
Version:	1.2.0
Release:	15
License:	LGPL
Group:		Development/Ruby
URL:		http://prime.sourceforge.jp/src/
Source0:	%{rname}-ruby-%{version}.tar.bz2
Patch0:		sary-ruby-1.2.0-ruby19.patch
Patch1:		sary-ruby-1.2.0-sfmt.patch
BuildRequires:	ruby-devel
BuildRequires:	sary-devel

%description
Ruby Binding of Sary

%prep
%setup -q -n %{rname}-ruby-%{version}
%patch0 -p1
%patch1 -p1

%build
ruby extconf.rb
make

%install
%makeinstall_std

%files
%{ruby_sitearchdir}/%{rname}.so
%doc ChangeLog README.en.rd README.ja.rd
%doc Reference.en.rd Reference.ja.rd



%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-11mdv2011.0
+ Revision: 669462
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-10mdv2011.0
+ Revision: 607382
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-9mdv2010.1
+ Revision: 523935
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.2.0-8mdv2010.0
+ Revision: 426967
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.2.0-7mdv2009.0
+ Revision: 222061
- fix installing
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Apr 21 2007 Pascal Terjan <pterjan@mandriva.org> 1.2.0-6mdv2008.0
+ Revision: 16664
- Use mkrel
- Use Development/Ruby group
- Use std macros


* Sun May 07 2006 Stefan van der Eijk <stefan@eijk.nu> 1.2.0-5mdk
- rebuild for sparc

* Fri Aug 19 2005 Pascal Terjan <pterjan@mandriva.org> 1.2.0-4mdk
- rebuild for new sary on x86_64...

* Tue Jul 19 2005 Pascal Terjan <pterjan@mandriva.org> 1.2.0-3mdk
- fix buildrequires (sary-devel provide is not versionned)

* Sat Apr 16 2005 Giuseppe Ghibò <ghibo@mandriva.com> 1.2.0-2mdk
- Fixes %%files for for X86-64.

* Wed Mar 30 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.2.0-1mdk
- new release

* Mon Feb 21 2005 Pascal Terjan <pterjan@mandrake.org> 1.1.0.1-2mdk
- rewrite like other ruby packages
- don't own /usr/lib/ruby/site_ruby/1.8
- drop explict requires
- rename ro ruby-sary

* Fri Feb 18 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.1.0.1-1mdk
- initial spec for mdk

