%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-ros-comm
Version:        1.15.2
Release:        1%{?dist}
Summary:        ROS ros_comm package

License:        BSD
URL:            http://wiki.ros.org/ros_comm
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-noetic-message-filters
Requires:       ros-noetic-ros
Requires:       ros-noetic-rosbag
Requires:       ros-noetic-rosconsole
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-rosgraph
Requires:       ros-noetic-rosgraph-msgs
Requires:       ros-noetic-roslaunch
Requires:       ros-noetic-roslisp
Requires:       ros-noetic-rosmaster
Requires:       ros-noetic-rosmsg
Requires:       ros-noetic-rosnode
Requires:       ros-noetic-rosout
Requires:       ros-noetic-rosparam
Requires:       ros-noetic-rospy
Requires:       ros-noetic-rosservice
Requires:       ros-noetic-rostest
Requires:       ros-noetic-rostopic
Requires:       ros-noetic-roswtf
Requires:       ros-noetic-std-srvs
Requires:       ros-noetic-topic-tools
Requires:       ros-noetic-xmlrpcpp
BuildRequires:  ros-noetic-catkin

%description
ROS communications-related packages, including core client libraries (roscpp,
rospy) and graph introspection tools (rostopic, rosnode, rosservice, rosparam).

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

