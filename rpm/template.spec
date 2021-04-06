%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-roswtf
Version:        1.15.11
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS roswtf package

License:        BSD
URL:            http://wiki.ros.org/roswtf
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python3-paramiko
Requires:       python3-rospkg
Requires:       ros-noetic-rosbuild
Requires:       ros-noetic-rosgraph
Requires:       ros-noetic-roslaunch
Requires:       ros-noetic-roslib
Requires:       ros-noetic-rosnode
Requires:       ros-noetic-rosservice
BuildRequires:  ros-noetic-catkin >= 0.5.68
BuildRequires:  ros-noetic-cmake-modules
BuildRequires:  ros-noetic-rosbag
BuildRequires:  ros-noetic-roslang
BuildRequires:  ros-noetic-rostest
BuildRequires:  ros-noetic-std-srvs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
roswtf is a tool for diagnosing issues with a running ROS system. Think of it as
a FAQ implemented in code.

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
* Tue Apr 06 2021 Jacob Perron <jacob@openrobotics.org> - 1.15.11-1
- Autogenerated by Bloom

* Thu Mar 18 2021 Jacob Perron <jacob@openrobotics.org> - 1.15.10-1
- Autogenerated by Bloom

* Fri Oct 16 2020 Jacob Perron <jacob@openrobotics.org> - 1.15.9-1
- Autogenerated by Bloom

* Thu Jul 23 2020 Dirk Thomas <dthomas@osrfoundation.org> - 1.15.8-1
- Autogenerated by Bloom

* Thu May 28 2020 Dirk Thomas <dthomas@osrfoundation.org> - 1.15.7-1
- Autogenerated by Bloom

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

