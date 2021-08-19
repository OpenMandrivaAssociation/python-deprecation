%global pypi_name deprecation

Name:           python-%{pypi_name}
Version:        2.1.0
Release:        1
Summary:        A library to handle automated deprecations
License:        ASL 2.0
Group:          Development/Python
URL:            https://pypi.org/project/deprecation
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)

%{?python_provide:%python_provide python3-%{pypi_name}}

%description
The deprecation library provides a deprecated decorator and a
fail_if_not_removed decorator for your tests. 

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

%install
%py_install

%files
%doc LICENSE
%doc README.rst
%{python_sitelib}/__pycache__/*
%{python_sitelib}/%{pypi_name}.py
%{python_sitelib}/%{pypi_name}-%{version}-py%{python_version}.egg-info
