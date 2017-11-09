Name:           ros-lunar-xmlrpcpp
Version:        1.13.5
Release:        0%{?dist}
Summary:        ROS xmlrpcpp package

Group:          Development/Libraries
License:        LGPL-2.1
URL:            http://xmlrpcpp.sourceforge.net
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-cpp-common
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-cpp-common

%description
XmlRpc++ is a C++ implementation of the XML-RPC protocol. This version is
heavily modified from the package available on SourceForge in order to support
roscpp's threading model. As such, we are maintaining our own fork.

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

