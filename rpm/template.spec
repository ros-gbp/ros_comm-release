%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-roscpp
Version:        1.15.2
Release:        1%{?dist}
Summary:        ROS roscpp package

License:        BSD
URL:            http://ros.org/wiki/roscpp
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-noetic-cpp-common >= 0.3.17
Requires:       ros-noetic-message-runtime
Requires:       ros-noetic-rosconsole
Requires:       ros-noetic-roscpp-serialization
Requires:       ros-noetic-roscpp-traits >= 0.3.17
Requires:       ros-noetic-rosgraph-msgs >= 1.10.3
Requires:       ros-noetic-rostime >= 0.6.4
Requires:       ros-noetic-std-msgs
Requires:       ros-noetic-xmlrpcpp
BuildRequires:  boost-devel
BuildRequires:  pkgconfig
BuildRequires:  ros-noetic-catkin >= 0.5.78
BuildRequires:  ros-noetic-cpp-common >= 0.3.17
BuildRequires:  ros-noetic-message-generation
BuildRequires:  ros-noetic-rosconsole
BuildRequires:  ros-noetic-roscpp-serialization
BuildRequires:  ros-noetic-roscpp-traits >= 0.3.17
BuildRequires:  ros-noetic-rosgraph-msgs >= 1.10.3
BuildRequires:  ros-noetic-roslang
BuildRequires:  ros-noetic-rostime >= 0.6.4
BuildRequires:  ros-noetic-std-msgs
BuildRequires:  ros-noetic-xmlrpcpp

%description
roscpp is a C++ implementation of ROS. It provides a client library that enables
C++ programmers to quickly interface with ROS Topics, Services, and Parameters.
roscpp is the most widely used ROS client library and is designed to be the
high-performance library for ROS.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Tue Feb 25 2020 Dirk Thomas <dthomas@osrfoundation.org> - 1.15.2-1
- Autogenerated by Bloom

* Mon Feb 24 2020 Dirk Thomas <dthomas@osrfoundation.org> - 1.15.1-1
- Autogenerated by Bloom

* Fri Feb 21 2020 Dirk Thomas <dthomas@osrfoundation.org> - 1.15.0-1
- Autogenerated by Bloom

