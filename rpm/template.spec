Name:           ros-lunar-rosparam
Version:        1.13.5
Release:        0%{?dist}
Summary:        ROS rosparam package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rosparam
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       PyYAML
Requires:       ros-lunar-rosgraph
BuildRequires:  ros-lunar-catkin

%description
rosparam contains the rosparam command-line tool for getting and setting ROS
Parameters on the Parameter Server using YAML-encoded files. It also contains an
experimental library for using YAML with the Parameter Server. This library is
intended for internal use only. rosparam can be invoked within a roslaunch file.

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
* Thu Nov 09 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.5-0
- Autogenerated by Bloom

* Thu Nov 02 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.4-0
- Autogenerated by Bloom

* Wed Oct 25 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.3-0
- Autogenerated by Bloom

* Tue Aug 15 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.2-0
- Autogenerated by Bloom

* Thu Jul 27 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.1-0
- Autogenerated by Bloom

* Wed Feb 22 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.0-0
- Autogenerated by Bloom

