Name:           ros-melodic-xmlrpcpp
Version:        1.14.1
Release:        0%{?dist}
Summary:        ROS xmlrpcpp package

Group:          Development/Libraries
License:        LGPL-2.1
URL:            http://xmlrpcpp.sourceforge.net
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-cpp-common
Requires:       ros-melodic-rostime >= 0.6.9
BuildRequires:  boost-devel
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cpp-common
BuildRequires:  ros-melodic-rostime >= 0.6.9

%description
XmlRpc++ is a C++ implementation of the XML-RPC protocol. This version is
heavily modified from the package available on SourceForge in order to support
roscpp's threading model. As such, we are maintaining our own fork.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Mon May 21 2018 Dirk Thomas <dthomas@osrfoundation.org> - 1.14.1-0
- Autogenerated by Bloom

* Mon May 21 2018 Dirk Thomas <dthomas@osrfoundation.org> - 1.14.0-0
- Autogenerated by Bloom

* Mon Apr 09 2018 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.6-2
- Autogenerated by Bloom

* Fri Mar 16 2018 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.6-1
- Autogenerated by Bloom

* Mon Feb 05 2018 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.6-0
- Autogenerated by Bloom

