%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/melodic/.*$
%global __requires_exclude_from ^/opt/ros/melodic/.*$

Name:           ros-melodic-pilz-industrial-motion
Version:        0.4.8
Release:        1%{?dist}
Summary:        ROS pilz_industrial_motion package

License:        Apache 2.0
URL:            https://wiki.ros.org/pilz_industrial_motion
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-melodic-pilz-extensions
Requires:       ros-melodic-pilz-msgs
Requires:       ros-melodic-pilz-robot-programming
Requires:       ros-melodic-pilz-trajectory-generation
BuildRequires:  ros-melodic-catkin

%description
The pilz_industrial_motion package

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
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
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/melodic

%changelog
* Fri Nov 22 2019 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.4.8-1
- Autogenerated by Bloom

* Tue Sep 10 2019 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.4.7-1
- Autogenerated by Bloom

* Wed Sep 04 2019 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.4.6-1
- Autogenerated by Bloom

* Tue Sep 03 2019 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.4.5-1
- Autogenerated by Bloom

* Wed Jun 19 2019 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.4.4-1
- Autogenerated by Bloom

* Mon Apr 08 2019 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.4.3-0
- Autogenerated by Bloom

* Wed Mar 13 2019 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.4.2-0
- Autogenerated by Bloom

* Sat Mar 02 2019 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.4.1-1
- Autogenerated by Bloom

* Wed Feb 27 2019 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.4.1-0
- Autogenerated by Bloom

* Tue Dec 18 2018 Pilz GmbH and Co. KG <ros@pilz.de> - 0.4.0-0
- Autogenerated by Bloom

* Wed Sep 26 2018 Pilz GmbH and Co. KG <ros@pilz.de> - 0.2.2-0
- Autogenerated by Bloom

* Tue Sep 25 2018 Pilz GmbH and Co. KG <ros@pilz.de> - 0.2.1-0
- Autogenerated by Bloom

* Fri Sep 14 2018 Pilz GmbH and Co. KG <ros@pilz.de> - 0.2.0-0
- Autogenerated by Bloom

