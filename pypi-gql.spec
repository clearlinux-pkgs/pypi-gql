#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-gql
Version  : 3.4.0
Release  : 3
URL      : https://files.pythonhosted.org/packages/f6/1e/e7f0231f05127466a1fc63c4a9e69a95676f4729a80f1c3b5106e5c42cf9/gql-3.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/f6/1e/e7f0231f05127466a1fc63c4a9e69a95676f4729a80f1c3b5106e5c42cf9/gql-3.4.0.tar.gz
Summary  : GraphQL client for Python
Group    : Development/Tools
License  : MIT
Requires: pypi-gql-bin = %{version}-%{release}
Requires: pypi-gql-license = %{version}-%{release}
Requires: pypi-gql-python = %{version}-%{release}
Requires: pypi-gql-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(backoff)
BuildRequires : pypi(graphql_core)
BuildRequires : pypi(py)
BuildRequires : pypi(yarl)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
This is a GraphQL client for Python 3.6+.
        Plays nicely with `graphene`, `graphql-core`, `graphql-js` and any other GraphQL implementation compatible with the spec.
        
        GQL architecture is inspired by `React-Relay` and `Apollo-Client`.
        
        [![GitHub-Actions][gh-image]][gh-url]
        [![pyversion][pyversion-image]][pyversion-url]
        [![pypi][pypi-image]][pypi-url]
        [![Anaconda-Server Badge][conda-image]][conda-url]
        [![codecov][codecov-image]][codecov-url]

%package bin
Summary: bin components for the pypi-gql package.
Group: Binaries
Requires: pypi-gql-license = %{version}-%{release}

%description bin
bin components for the pypi-gql package.


%package license
Summary: license components for the pypi-gql package.
Group: Default

%description license
license components for the pypi-gql package.


%package python
Summary: python components for the pypi-gql package.
Group: Default
Requires: pypi-gql-python3 = %{version}-%{release}

%description python
python components for the pypi-gql package.


%package python3
Summary: python3 components for the pypi-gql package.
Group: Default
Requires: python3-core
Provides: pypi(gql)
Requires: pypi(backoff)
Requires: pypi(graphql_core)
Requires: pypi(yarl)

%description python3
python3 components for the pypi-gql package.


%prep
%setup -q -n gql-3.4.0
cd %{_builddir}/gql-3.4.0
pushd ..
cp -a gql-3.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1661523000
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-gql
cp %{_builddir}/gql-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-gql/5fc4bc923b03ed1a6b3cbdcd3be10b4335fa3687 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gql-cli

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-gql/5fc4bc923b03ed1a6b3cbdcd3be10b4335fa3687

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
