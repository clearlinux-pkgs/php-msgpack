#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
# autospec version: v21
# autospec commit: f4a13a5
#
Name     : php-msgpack
Version  : 3.0.0
Release  : 81
URL      : https://pecl.php.net/get/msgpack-3.0.0.tgz
Source0  : https://pecl.php.net/get/msgpack-3.0.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: php-msgpack-lib = %{version}-%{release}
Requires: php-msgpack-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : file
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Msgpack for PHP
[![Build Status](https://github.com/msgpack/msgpack-php/workflows/ci/badge.svg?branch=master)](https://github.com/msgpack/msgpack-php/actions?query=workflow%3Aci+branch%3Amaster)

%package dev
Summary: dev components for the php-msgpack package.
Group: Development
Requires: php-msgpack-lib = %{version}-%{release}
Provides: php-msgpack-devel = %{version}-%{release}
Requires: php-msgpack = %{version}-%{release}

%description dev
dev components for the php-msgpack package.


%package lib
Summary: lib components for the php-msgpack package.
Group: Libraries
Requires: php-msgpack-license = %{version}-%{release}

%description lib
lib components for the php-msgpack package.


%package license
Summary: license components for the php-msgpack package.
Group: Default

%description license
license components for the php-msgpack package.


%prep
%setup -q -n msgpack-3.0.0
cd %{_builddir}/msgpack-3.0.0
pushd ..
cp -a msgpack-3.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-msgpack
cp %{_builddir}/msgpack-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-msgpack/d2477c1ca8dc3fee03d19df14fa92bbc2da7a1fa || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/php/ext/msgpack/php_msgpack.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20240924/msgpack.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-msgpack/d2477c1ca8dc3fee03d19df14fa92bbc2da7a1fa
