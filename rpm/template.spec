Name:           ros-melodic-roscpp
Version:        1.13.6
Release:        1%{?dist}
Summary:        ROS roscpp package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roscpp
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-cpp-common >= 0.3.17
Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-rosconsole
Requires:       ros-melodic-roscpp-serialization
Requires:       ros-melodic-roscpp-traits >= 0.3.17
Requires:       ros-melodic-rosgraph-msgs >= 1.10.3
Requires:       ros-melodic-rostime >= 0.6.4
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-xmlrpcpp
BuildRequires:  pkgconfig
BuildRequires:  ros-melodic-catkin >= 0.5.78
BuildRequires:  ros-melodic-cpp-common >= 0.3.17
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-rosconsole
BuildRequires:  ros-melodic-roscpp-serialization
BuildRequires:  ros-melodic-roscpp-traits >= 0.3.17
BuildRequires:  ros-melodic-rosgraph-msgs >= 1.10.3
BuildRequires:  ros-melodic-roslang
BuildRequires:  ros-melodic-rostime >= 0.6.4
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-xmlrpcpp

%description
roscpp is a C++ implementation of ROS. It provides a client library that enables
C++ programmers to quickly interface with ROS Topics, Services, and Parameters.
roscpp is the most widely used ROS client library and is designed to be the
high-performance library for ROS.

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
* Fri Mar 16 2018 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.6-1
- Autogenerated by Bloom

* Mon Feb 05 2018 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.6-0
- Autogenerated by Bloom

