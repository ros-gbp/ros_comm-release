Name:           ros-indigo-rosgraph
Version:        1.11.14
Release:        0%{?dist}
Summary:        ROS rosgraph package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rosgraph
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python-netifaces
Requires:       python-rospkg
BuildRequires:  python-mock
BuildRequires:  ros-indigo-catkin >= 0.5.78

%description
rosgraph contains the rosgraph command-line tool, which prints information about
the ROS Computation Graph. It also provides an internal library that can be used
by graphical tools.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Sep 20 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.14-0
- Autogenerated by Bloom

* Tue Apr 28 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.13-0
- Autogenerated by Bloom

* Mon Apr 27 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.12-0
- Autogenerated by Bloom

* Thu Apr 16 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.11-0
- Autogenerated by Bloom

* Mon Dec 22 2014 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.10-0
- Autogenerated by Bloom

* Mon Aug 18 2014 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.9-0
- Autogenerated by Bloom

* Mon Aug 04 2014 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.8-0
- Autogenerated by Bloom

