# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-idna-ssl
Epoch: 100
Version: 1.1.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Patch ssl.match_hostname for Unicode(idna) domains support
License: MIT
URL: https://github.com/aio-libs/idna-ssl/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Patch ssl.match_hostname for Unicode(idna) domains support.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-idna-ssl
Summary: Patch ssl.match_hostname for Unicode(idna) domains support
Requires: python3
Provides: python3-idna-ssl = %{epoch}:%{version}-%{release}
Provides: python3dist(idna-ssl) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-idna-ssl = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(idna-ssl) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-idna-ssl = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(idna-ssl) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-idna-ssl
Patch ssl.match_hostname for Unicode(idna) domains support.

%files -n python%{python3_version_nodots}-idna-ssl
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-idna-ssl
Summary: Patch ssl.match_hostname for Unicode(idna) domains support
Requires: python3
Provides: python3-idna-ssl = %{epoch}:%{version}-%{release}
Provides: python3dist(idna-ssl) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-idna-ssl = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(idna-ssl) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-idna-ssl = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(idna-ssl) = %{epoch}:%{version}-%{release}

%description -n python3-idna-ssl
Patch ssl.match_hostname for Unicode(idna) domains support.

%files -n python3-idna-ssl
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
