Name:           ros-melodic-rosbag-storage
Version:        1.14.2
Release:        0%{?dist}
Summary:        ROS rosbag_storage package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       bzip2-devel
Requires:       console-bridge-devel
Requires:       gpgme-devel
Requires:       openssl-devel
Requires:       ros-melodic-cpp-common >= 0.3.17
Requires:       ros-melodic-pluginlib
Requires:       ros-melodic-roscpp-serialization
Requires:       ros-melodic-roscpp-traits >= 0.3.17
Requires:       ros-melodic-roslz4
Requires:       ros-melodic-rostime
BuildRequires:  boost-devel
BuildRequires:  bzip2-devel
BuildRequires:  console-bridge-devel
BuildRequires:  gpgme-devel
BuildRequires:  openssl-devel
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cpp-common >= 0.3.17
BuildRequires:  ros-melodic-pluginlib
BuildRequires:  ros-melodic-roscpp-serialization
BuildRequires:  ros-melodic-roscpp-traits >= 0.3.17
BuildRequires:  ros-melodic-roslz4
BuildRequires:  ros-melodic-rostest
BuildRequires:  ros-melodic-rostime

%description
This is a set of tools for recording from and playing back ROS message without
relying on the ROS client library.

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

