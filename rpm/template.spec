Name:           ros-melodic-roslaunch
Version:        1.14.1
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
Requires:       ros-melodic-rosclean
Requires:       ros-melodic-rosgraph-msgs
Requires:       ros-melodic-roslib
Requires:       ros-melodic-rosmaster >= 1.11.16
Requires:       ros-melodic-rosout
Requires:       ros-melodic-rosparam
Requires:       ros-melodic-rosunit >= 1.13.3
BuildRequires:  ros-melodic-catkin >= 0.5.78
BuildRequires:  ros-melodic-rosbuild

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

