Name:           ros-lunar-roswtf
Version:        1.13.0
Release:        0%{?dist}
Summary:        ROS roswtf package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roswtf
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python-paramiko
Requires:       python-rospkg
Requires:       ros-lunar-rosbuild
Requires:       ros-lunar-rosgraph
Requires:       ros-lunar-roslaunch
Requires:       ros-lunar-roslib
Requires:       ros-lunar-rosnode
Requires:       ros-lunar-rosservice
BuildRequires:  ros-lunar-catkin >= 0.5.68
BuildRequires:  ros-lunar-cmake-modules
BuildRequires:  ros-lunar-rostest

%description
roswtf is a tool for diagnosing issues with a running ROS system. Think of it as
a FAQ implemented in code.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Wed Feb 22 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.0-0
- Autogenerated by Bloom

