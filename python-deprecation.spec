%global pypi_name deprecation

Name:           python-%{pypi_name}
Version:        2.1.0
Release:        %mkrel 2
Summary:        A library to handle automated deprecations
License:        ASL 2.0
Group:          Development/Python
URL:            https://pypi.org/project/deprecation
Source0:        %{pypi_source}
BuildArch:      noarch

%description
The deprecation library provides a deprecated decorator and a
fail_if_not_removed decorator for your tests. 

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Group:          Development/Python
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The deprecation library provides a deprecated decorator and a
fail_if_not_removed decorator for your tests. 

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
