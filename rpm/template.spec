%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-rosout
Version:        1.15.6
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rosout package

License:        BSD
URL:            http://ros.org/wiki/rosout
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-roscpp
Requires:       ros-noetic-rosgraph-msgs
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-rosgraph-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
System-wide logging mechanism for messages sent to the /rosout topic.

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
* Thu May 21 2020 Dirk Thomas <dthomas@osrfoundation.org> - 1.15.6-1
- Autogenerated by Bloom

* Fri May 15 2020 Dirk Thomas <dthomas@osrfoundation.org> - 1.15.5-1
- Autogenerated by Bloom

* Thu Mar 19 2020 Dirk Thomas <dthomas@osrfoundation.org> - 1.15.4-1
- Autogenerated by Bloom

* Fri Feb 28 2020 Dirk Thomas <dthomas@osrfoundation.org> - 1.15.3-1
- Autogenerated by Bloom

* Tue Feb 25 2020 Dirk Thomas <dthomas@osrfoundation.org> - 1.15.2-1
- Autogenerated by Bloom

* Mon Feb 24 2020 Dirk Thomas <dthomas@osrfoundation.org> - 1.15.1-1
- Autogenerated by Bloom

* Fri Feb 21 2020 Dirk Thomas <dthomas@osrfoundation.org> - 1.15.0-1
- Autogenerated by Bloom

