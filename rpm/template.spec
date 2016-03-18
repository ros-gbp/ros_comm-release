Name:           ros-kinetic-rosmsg
Version:        1.12.0
Release:        0%{?dist}
Summary:        ROS rosmsg package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rosmsg
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python-rospkg
Requires:       ros-kinetic-catkin >= 0.6.4
Requires:       ros-kinetic-genmsg
Requires:       ros-kinetic-rosbag
Requires:       ros-kinetic-roslib
BuildRequires:  ros-kinetic-catkin

%description
rosmsg contains two command-line tools: rosmsg and rossrv. rosmsg is a command-
line tool for displaying information about ROS Message types. rossrv is a
command-line tool for displaying information about ROS Service types.

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
* Fri Mar 18 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.0-0
- Autogenerated by Bloom

* Fri Mar 11 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.17-0
- Autogenerated by Bloom

