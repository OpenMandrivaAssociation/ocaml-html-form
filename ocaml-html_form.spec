%define name	ocaml-html-form
%define version	0.1
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    OCaml HTML forms
Group:      Development/Other
License:    MIT
URL:        http://pauillac.inria.fr/~guesdon/Tools/Tars/
Source0:    http://pauillac.inria.fr/~guesdon/Tools/Tars/html-form_snapshot.tar.gz
BuildRequires:  ocaml >= 3.10.0
BuildRequires:  glibc-static-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
OWS is a library to easily create HTML forms.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n html-form-snapshot

%build
./configure
make all

%install
rm -rf %{buildroot}
make \
    INSTALL_BINDIR=%{buildroot}%{_bindir} \
    INSTALL_LIBDIR=%{buildroot}%{ocaml_sitelib}/html_form \
    install

cp html_form_types.mli %{buildroot}%{ocaml_sitelib}/html_form
mv -f %{buildroot}%{_bindir}/html_form.opt %{buildroot}%{_bindir}/html_form

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/html_form
%dir %{ocaml_sitelib}/html_form
%{ocaml_sitelib}/html_form/*.cmi

%files devel
%defattr(-,root,root)
%{ocaml_sitelib}/html_form/*
%exclude %{ocaml_sitelib}/html_form/*.cmi

