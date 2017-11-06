Name:           ros-kinetic-rosbag
Version:        1.12.9
Release:        0%{?dist}
Summary:        ROS rosbag package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rosbag
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       python-rospkg
Requires:       ros-kinetic-genmsg
Requires:       ros-kinetic-genpy
Requires:       ros-kinetic-rosbag-storage
Requires:       ros-kinetic-rosconsole
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-roslib
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-std-srvs
Requires:       ros-kinetic-topic-tools
Requires:       ros-kinetic-xmlrpcpp
BuildRequires:  boost-devel
BuildRequires:  python-pillow
BuildRequires:  python-pillow-qt
BuildRequires:  ros-kinetic-catkin >= 0.5.78
BuildRequires:  ros-kinetic-cpp-common
BuildRequires:  ros-kinetic-rosbag-storage
BuildRequires:  ros-kinetic-rosconsole
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-roscpp-serialization
BuildRequires:  ros-kinetic-std-srvs
BuildRequires:  ros-kinetic-topic-tools
BuildRequires:  ros-kinetic-xmlrpcpp

%description
This is a set of tools for recording from and playing back to ROS topics. It is
intended to be high performance and avoids deserialization and reserialization
of the messages.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Nov 06 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.9-0
- Autogenerated by Bloom

* Mon Nov 06 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.8-0
- Autogenerated by Bloom

* Fri Feb 17 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.7-0
- Autogenerated by Bloom

* Wed Oct 26 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.6-0
- Autogenerated by Bloom

* Fri Sep 30 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.5-0
- Autogenerated by Bloom

* Mon Sep 19 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.4-0
- Autogenerated by Bloom

* Fri Jun 03 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.2-0
- Autogenerated by Bloom

* Fri Mar 18 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.0-0
- Autogenerated by Bloom

* Fri Mar 11 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.17-0
- Autogenerated by Bloom

