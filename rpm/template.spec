Name:           ros-melodic-pilz-industrial-motion
Version:        0.2.0
Release:        0%{?dist}
Summary:        ROS pilz_industrial_motion package

Group:          Development/Libraries
License:        Apache 2.0
URL:            https://wiki.ros.org/pilz_industrial_motion
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-melodic-pilz-extensions
Requires:       ros-melodic-pilz-msgs
Requires:       ros-melodic-pilz-trajectory-generation
BuildRequires:  ros-melodic-catkin

%description
The pilz_industrial_motion package

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
* Fri Sep 14 2018 Pilz GmbH and Co. KG <ros@pilz.de> - 0.2.0-0
- Autogenerated by Bloom

