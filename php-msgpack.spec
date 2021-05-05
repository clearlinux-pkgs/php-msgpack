#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-msgpack
Version  : 2.1.2
Release  : 10
URL      : https://pecl.php.net/get/msgpack-2.1.2.tgz
Source0  : https://pecl.php.net/get/msgpack-2.1.2.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: php-msgpack-lib = %{version}-%{release}
BuildRequires : buildreq-php

%description
# Msgpack for PHP
[![Build Status](https://secure.travis-ci.org/msgpack/msgpack-php.png)](https://travis-ci.org/msgpack/msgpack-php)

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

%description lib
lib components for the php-msgpack package.


%prep
%setup -q -n msgpack-2.1.2
cd %{_builddir}/msgpack-2.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
autoupdate
%configure
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/php/ext/msgpack/php_msgpack.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20200930/msgpack.so
