%define name	ocaml-html-form
%define version	0.1
%define release	%mkrel 2

%if %mdkversion > 200900
%define ocaml_libdir %{_libdir}/ocaml
%else
%define ocaml_libdir %{ocaml_sitelib}
%endif

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
    INSTALL_LIBDIR=%{buildroot}%{ocaml_libdir}/html_form \
    install

cp html_form_types.mli %{buildroot}%{ocaml_libdir}/html_form
mv -f %{buildroot}%{_bindir}/html_form.opt %{buildroot}%{_bindir}/html_form

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/html_form
%dir %{ocaml_libdir}/html_form
%{ocaml_libdir}/html_form/*.cmi
%{ocaml_libdir}/html_form/*.cma

%files devel
%defattr(-,root,root)
%{ocaml_libdir}/html_form/*.a
%{ocaml_libdir}/html_form/*.cmxa
%{ocaml_libdir}/html_form/*.mli
