Name:           ros-melodic-rosservice
Version:        1.14.3
Release:        0%{?dist}
Summary:        ROS rosservice package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rosservice
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-melodic-genpy
Requires:       ros-melodic-rosgraph
Requires:       ros-melodic-roslib
Requires:       ros-melodic-rosmsg
Requires:       ros-melodic-rospy
BuildRequires:  ros-melodic-catkin >= 0.5.78

%description
rosservice contains the rosservice command-line tool for listing and querying
ROS Services. It also contains a Python library for retrieving information about
Services and dynamically invoking them. The Python library is experimental and
is for internal-use only.

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
* Mon Aug 06 2018 Dirk Thomas <dthomas@osrfoundation.org> - 1.14.3-0
- Autogenerated by Bloom

* Wed Jun 06 2018 Dirk Thomas <dthomas@osrfoundation.org> - 1.14.2-0
- Autogenerated by Bloom

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

