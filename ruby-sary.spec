%define rname sary
%define name ruby-%{rname}
%define version 1.2.0
%define release 5mdk

Summary: Ruby Binding of Sary
Name: %{name}
Version: %{version}
Release: %{release}
URL: http://prime.sourceforge.jp/src/
Source0: %{rname}-ruby-%{version}.tar.bz2
License: LGPL
Group: Development/Other
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: ruby-devel
BuildRequires: sary-devel
Obsoletes: sary-ruby
Provides: sary-ruby

%define ruby_archdir %(ruby -rrbconfig -e 'puts Config::CONFIG["sitearchdir"]')

%description
Ruby Binding of Sary

%prep
%setup -q -n %{rname}-ruby-%{version}

%build
ruby extconf.rb
make

%install
rm -rf %buildroot
%makeinstall

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{ruby_archdir}/%{rname}.so
%doc ChangeLog README.en.rd README.ja.rd
%doc Reference.en.rd Reference.ja.rd

