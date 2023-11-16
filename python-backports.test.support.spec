#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (useful for <3.7 only)

Summary:	Backport of Python 3's test.support package
Summary(pl.UTF-8):	Backport pakietu test.support z Pythona 3
Name:		python-backports.test.support
Version:	0.1.1
Release:	1
License:	PSF
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/backports.test.support/
Source0:	https://files.pythonhosted.org/packages/source/b/backports.test.support/backports.test.support-%{version}.tar.gz
# Source0-md5:	9ef16a189becb8c0aebe34339329d08a
URL:		https://pypi.org/project/backports.test.support/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
%if %{with tests}
BuildRequires:	python-backports.os
BuildRequires:	python-future
BuildRequires:	python-mock
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This backports Python 3's test.support package under the "backports"
namespace.

This is probably only interesting if you're backporting standard
library test code.

%description -l pl.UTF-8
Ten moduł jest backportem pakietu test.support z Pythona 3 do
przestrzeni nazw "backports".

Jest to interesujące prawdopodobnie tylko przy backportowaniu kodu
testującego biblioteki standardowej.

%package -n python3-backports.test.support
Summary:	Backport of Python 3's test.support package
Summary(pl.UTF-8):	Backport pakietu test.support z Pythona 3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-backports.test.support
This backports Python 3's test.support package under the "backports"
namespace.

This is probably only interesting if you're backporting standard
library test code.

%description -n python3-backports.test.support -l pl.UTF-8
Ten moduł jest backportem pakietu test.support z Pythona 3 do
przestrzeni nazw "backports".

Jest to interesujące prawdopodobnie tylko przy backportowaniu kodu
testującego biblioteki standardowej.

%prep
%setup -q -n backports.test.support-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python} -m unittest discover tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python3} -m unittest discover tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

# packaged in python-backports
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/backports/__init__.py*
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%dir %{py_sitescriptdir}/backports/test
%{py_sitescriptdir}/backports/test/__init__.py[co]
%{py_sitescriptdir}/backports/test/support
%{py_sitescriptdir}/backports.test.support-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-backports.test.support
%defattr(644,root,root,755)
%doc README.rst
%dir %{py3_sitescriptdir}/backports/test
%{py3_sitescriptdir}/backports/test/__init__.py
%{py3_sitescriptdir}/backports/test/__pycache__
%{py3_sitescriptdir}/backports/test/support
%{py3_sitescriptdir}/backports.test.support-%{version}-py*.egg-info
%endif
