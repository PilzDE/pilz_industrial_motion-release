Name:           ros-melodic-pilz-robot-programming
Version:        0.4.7
Release:        1%{?dist}
Summary:        ROS pilz_robot_programming package

Group:          Development/Libraries
License:        LGPLv3
Source0:        %{name}-%{version}.tar.gz

Requires:       python-psutil
Requires:       ros-melodic-moveit-commander
Requires:       ros-melodic-pilz-msgs
Requires:       ros-melodic-pilz-trajectory-generation
Requires:       ros-melodic-rospy
Requires:       ros-melodic-tf
Requires:       ros-melodic-tf-conversions
BuildRequires:  python-coverage
BuildRequires:  python-docopt
BuildRequires:  python-mock
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-pilz-industrial-motion-testutils
BuildRequires:  ros-melodic-prbt-moveit-config
BuildRequires:  ros-melodic-prbt-pg70-support
BuildRequires:  ros-melodic-roslint
BuildRequires:  ros-melodic-rospy
BuildRequires:  ros-melodic-rostest

%description
An Easy to use API to execute standard industrial robot commands like Ptp, Lin,
Circ and Sequence using Moveit.

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
* Tue Sep 10 2019 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.4.7-1
- Autogenerated by Bloom

* Wed Sep 04 2019 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.4.6-1
- Autogenerated by Bloom

* Tue Sep 03 2019 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.4.5-1
- Autogenerated by Bloom

* Wed Jun 19 2019 Pilz GmbH and Co. KG <ros@pilz.de> - 0.4.4-1
- Autogenerated by Bloom

* Mon Apr 08 2019 Pilz GmbH and Co. KG <ros@pilz.de> - 0.4.3-0
- Autogenerated by Bloom

* Wed Mar 13 2019 Pilz GmbH and Co. KG <ros@pilz.de> - 0.4.2-0
- Autogenerated by Bloom

* Sat Mar 02 2019 Pilz GmbH and Co. KG <ros@pilz.de> - 0.4.1-1
- Autogenerated by Bloom

* Wed Feb 27 2019 Pilz GmbH and Co. KG <ros@pilz.de> - 0.4.1-0
- Autogenerated by Bloom

* Tue Dec 18 2018 Pilz GmbH and Co. KG <ros@pilz.de> - 0.4.0-0
- Autogenerated by Bloom

