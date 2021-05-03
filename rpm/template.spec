%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-pilz-robot-programming
Version:        0.5.0
Release:        2%{?dist}%{?release_suffix}
Summary:        ROS pilz_robot_programming package

License:        LGPLv3
Source0:        %{name}-%{version}.tar.gz

Requires:       python3-psutil
Requires:       ros-noetic-moveit-commander
Requires:       ros-noetic-pilz-industrial-motion-planner
Requires:       ros-noetic-pilz-msgs
Requires:       ros-noetic-rospy
Requires:       ros-noetic-tf-conversions
Requires:       ros-noetic-tf2-geometry-msgs
Requires:       ros-noetic-tf2-ros
BuildRequires:  python3-coverage
BuildRequires:  python3-docopt
BuildRequires:  python3-mock
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-code-coverage
BuildRequires:  ros-noetic-pilz-industrial-motion-testutils
BuildRequires:  ros-noetic-prbt-hardware-support
BuildRequires:  ros-noetic-prbt-moveit-config
BuildRequires:  ros-noetic-prbt-pg70-support
BuildRequires:  ros-noetic-roslint
BuildRequires:  ros-noetic-rospy
BuildRequires:  ros-noetic-rostest
BuildRequires:  ros-noetic-rosunit
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
An Easy to use API to execute standard industrial robot commands like Ptp, Lin,
Circ and Sequence using Moveit.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Mon May 03 2021 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.5.0-2
- Autogenerated by Bloom

* Mon May 03 2021 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.5.0-1
- Autogenerated by Bloom

