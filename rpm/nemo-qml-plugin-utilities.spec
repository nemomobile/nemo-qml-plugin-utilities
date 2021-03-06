# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.26
# 

Name:       nemo-qml-plugin-utilities

# >> macros
# << macros

Summary:    Utilities plugin for Nemo Mobile
Version:    0.0.0
Release:    1
Group:      System/Libraries
License:    LGPLv2.1
URL:        https://github.com/nemomobile/nemo-qml-plugin-utilities
Source0:    %{name}-%{version}.tar.bz2
Source100:  nemo-qml-plugin-utilities.yaml
BuildRequires:  pkgconfig(QtCore) >= 4.7.0
BuildRequires:  pkgconfig(QtDeclarative)
BuildRequires:  pkgconfig(x11)
Provides:   nemo-qml-plugins-utilities > 0.3.21
Obsoletes:   nemo-qml-plugins-utilities <= 0.3.21

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake 

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake_install

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_libdir}/qt4/imports/org/nemomobile/utilities/libnemoutilities.so
%{_libdir}/qt4/imports/org/nemomobile/utilities/qmldir
# >> files
# << files
