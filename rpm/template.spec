Name:           ros-kinetic-roslaunch
Version:        1.12.12
Release:        0%{?dist}
Summary:        ROS roslaunch package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roslaunch
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       PyYAML
Requires:       python-paramiko
Requires:       python-rospkg >= 1.0.37
Requires:       ros-kinetic-rosclean
Requires:       ros-kinetic-rosgraph-msgs
Requires:       ros-kinetic-roslib
Requires:       ros-kinetic-rosmaster >= 1.11.16
Requires:       ros-kinetic-rosout
Requires:       ros-kinetic-rosparam
Requires:       ros-kinetic-rosunit >= 1.13.3
BuildRequires:  ros-kinetic-catkin >= 0.5.78
BuildRequires:  ros-kinetic-rosbuild

%description
roslaunch is a tool for easily launching multiple ROS nodes locally and remotely
via SSH, as well as setting parameters on the Parameter Server. It includes
options to automatically respawn processes that have already died. roslaunch
takes in one or more XML configuration files (with the .launch extension) that
specify the parameters to set and nodes to launch, as well as the machines that
they should be run on.

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
* Thu Nov 16 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.12-0
- Autogenerated by Bloom

* Tue Nov 07 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.11-0
- Autogenerated by Bloom

* Mon Nov 06 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.10-0
- Autogenerated by Bloom

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

