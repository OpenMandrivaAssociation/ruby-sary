%define rname sary
%define name ruby-%{rname}
%define version 1.2.0
%define release %mkrel 10

Summary: Ruby Binding of Sary
Name: %{name}
Version: %{version}
Release: %{release}
URL: http://prime.sourceforge.jp/src/
Source0: %{rname}-ruby-%{version}.tar.bz2
License: LGPL
Group: Development/Ruby
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: ruby-devel
BuildRequires: sary-devel
Obsoletes: sary-ruby
Provides: sary-ruby

%description
Ruby Binding of Sary

%prep
%setup -q -n %{rname}-ruby-%{version}

%build
ruby extconf.rb
make

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{ruby_sitearchdir}/%{rname}.so
%doc ChangeLog README.en.rd README.ja.rd
%doc Reference.en.rd Reference.ja.rd

