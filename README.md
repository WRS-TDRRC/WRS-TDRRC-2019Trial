# WRS-TDRRC-2019Trial
The material storage of World Robot Summit(Competition) Tunnel Disaster Response and Recovery Challenge 2019 Trial  

### ABOUT Robotic middle-ware  
 * Recommend using ROS1  
We have got information that the choreonoid developer will support the connection between choreonoid and ROS1.  
TO GET MORE DETAILS, STRONGLY RECOMMEND TO VISIT THE FOLLOWING CHOREONOID SITES:

    * [Cooperation with ROS](https://choreonoid.org/en/documents/latest/ros/index.html)  
    * [World Robot Summit 2018](https://choreonoid.org/en/documents/latest/wrs2018/index.html)  

 * Not recommend using OpenRTM  
We got information that the choreonoid developer does not have any plan to support the connection between choreonoid and RTM.  
There is information that the RTM version 1.1.2 and 1.2.0 were used with older choreonoid. But there is no information on whether the choreonoid developer will support.  

### ABOUT AGX Dynamics  
We are considering the suitable version of AGX.  
Currently, Version 2.30.4.0 (the former version was 2.29.4.0) is recommended by the committee.  
To install version 2.30.4.0, use the command "gdebi" instead of "dpkg".  
TO GET MORE DETAILS, STRONGLY RECOMMEND TO VISIT THE FOLLOWING CHOREONOID SITE:

  * [Installation of AGX Dynamics](https://translate.google.com/translate?sl=auto&tl=en&u=https://choreonoid.org/ja/documents/latest/agxdynamics/install/install-agx-ubuntu.html%23id5)  

## Requirements  

  1. OS  
    * Ubuntu 18.04 LTS  
  2. Choreonoid  
    * Using choreonoid with ROS1:  
      [Building Choreonoid related packages(with ROS)](https://choreonoid.org/en/documents/latest/ros/build-choreonoid.html)  
    * [Choreonoid Operation Manual](https://choreonoid.org/en/manuals/latest/index.html)  
    * [Building Choreonoid](https://choreonoid.org/en/manuals/latest/install/build-ubuntu.html#development-version)  
  3. AGX  
    * [AGX for Choreonoid](https://choreonoid.org/en/manuals/latest/agxdynamics/index.html)  
    * [Downloading AGX](https://www.algoryx.se/download/?id=2592)  
    * [Installation of AGX Dynamics(in the Choreonoid site)](https://translate.google.com/translate?sl=auto&tl=en&u=https://choreonoid.org/ja/documents/latest/agxdynamics/install/install-agx-ubuntu.html%23id5)  
    * [Installing AGX(in the Algoryx site)](https://www.algoryx.se/documentation/complete/agx/tags/latest/UserManual/source/installation.html#install-on-ubuntu-16-04)  
  4. Other elementally packages for using choreonoid with ROS1  
    * [Installing ROS](https://choreonoid.org/en/documents/latest/ros/install-ros.html)  
 
## How to use this repository WITH ROS  
If you have to install choreonoid now, please follow below commands:  

    $ sudo apt-get install python-catkin-tools qt5-default libqt5x11extras5-dev qt5-style-plugins  
    $ cd ~  
    $ mkdir -p catkin_ws/src  
    $ cd catkin_ws  
    $ catkin init  
    $ cd src  
    $ git clone https://github.com/choreonoid/choreonoid.git  
    $ git clone https://github.com/choreonoid/choreonoid_ros.git  
    $ git clone https://github.com/choreonoid/choreonoid_ros_samples.git  
    $ git clone https://github.com/choreonoid/choreonoid_joy.git  
    $ git clone https://github.com/WRS-TDRRC/WRS-TDRRC-2019Trial choreonoid/ext/WRS2019  
    $ choreonoid/misc/script/install-requisites-ubuntu-18.04.sh  
    $ cd ..    
    $ catkin config --cmake-args -DBUILD_COMPETITION_PLUGIN=ON -DBUILD_AGX_DYNAMICS_PLUGIN=ON -DBUILD_AGX_BODYEXTENSION_PLUGIN=ON -DBUILD_SCENE_EFFECTS_PLUGIN=ON -DBUILD_MULTICOPTER_PLUGIN=ON -DBUILD_MULTICOPTER_SAMPLES=ON -DBUILD_CHOREONOID_EXECUTABLE=OFF -DUSE_PYTHON3=OFF -DCMAKE_BUILD_TYPE=Release -DENABLE_INSTALL_RPATH_USE_LINK_PATH=ON -DBUILD_WRS2018=ON  
    $ catkin build   

Before run, you have to add "source /opt/Algoryx/AgX-VERSION-NUMBER/setup_env.bash" at the end of ~/.bashrc , and reopen the terminal.  
Please find field images and run scripts in the [wiki page](https://github.com/WRS-TDRRC/WRS-TDRRC-2019Trial/wiki).  

* TERMINAL 1:  
    $ roscore  

* TERMINAL 2:  
    $ cd ~/catkin_ws  
    $ source devel/setup.bash  
    $ rosrun choreonoid_joy node  

* TERMINAL 3:  
    $ cd ~/catkin_ws  
    $ source devel/setup.bash  
    $ rosrun choreonoid_ros choreonoid devel/share/choreonoid-1.8/WRS2019/script/TS1-DoubleArmV7A-ROS.py  

* TERMINAL 4:  
    $ rqt_image_view  

## How to use this repository WITHOUT ROS 
If you have to install choreonoid now, please follow below commands:  

    $ cd ~  
    $ git clone https://github.com/choreonoid/choreonoid.git  
    $ ~/choreonoid/misc/script/install-requisites-ubuntu-18.04.sh  
    $ sudo apt-get install qt5-default libqt5x11extras5-dev qt5-style-plugins  
    $ cd ~/choreonoid/ext  
    $ git clone https://github.com/WRS-TDRRC/WRS-TDRRC-2019Trial WRS2019  
    $ cd ~/choreonoid && mkdir build && cd build  
    $ cmake .. --cmake-args -DBUILD_COMPETITION_PLUGIN=ON -DBUILD_AGX_DYNAMICS_PLUGIN=ON -DBUILD_AGX_BODYEXTENSION_PLUGIN=ON -DBUILD_SCENE_EFFECTS_PLUGIN=ON -DBUILD_MULTICOPTER_PLUGIN=ON -DBUILD_MULTICOPTER_SAMPLES=ON -DBUILD_CHOREONOID_EXECUTABLE=OFF -DUSE_PYTHON3=OFF -DCMAKE_BUILD_TYPE=Release -DENABLE_INSTALL_RPATH_USE_LINK_PATH=ON -DBUILD_WRS2018=ON  
    $ make -j8  
  
Or you are already using choreonoid, please follow below commands:  
(When your choreonoid is under ~/choreonoid)  

    $ cd ~/choreonoid/ext  
    $ git clone https://github.com/WRS-TDRRC/WRS-TDRRC-2019Trial WRS2019  
    $ cd ~/choreonoid/build  
    $ cmake .. --cmake-args -DBUILD_COMPETITION_PLUGIN=ON -DBUILD_AGX_DYNAMICS_PLUGIN=ON -DBUILD_AGX_BODYEXTENSION_PLUGIN=ON -DBUILD_SCENE_EFFECTS_PLUGIN=ON -DBUILD_MULTICOPTER_PLUGIN=ON -DBUILD_MULTICOPTER_SAMPLES=ON -DBUILD_CHOREONOID_EXECUTABLE=OFF -DUSE_PYTHON3=OFF -DCMAKE_BUILD_TYPE=Release -DENABLE_INSTALL_RPATH_USE_LINK_PATH=ON -DBUILD_WRS2018=ON  
    $ make -j8  

Before run, you have to add "source /opt/Algoryx/AgX-VERSION-NUMBER/setup_env.bash" at the end of ~/.bashrc , and reopen the terminal.  
Please find field images and run scripts in the [wiki page](https://github.com/WRS-TDRRC/WRS-TDRRC-2019Trial/wiki).  

## The location of the simulation log files  
After running a simulation, you can find a simulation log file under ~/choreonoid/ext/WRS2019/project.  
Please see also [Choreonoid documentation](https://choreonoid.org/en/manuals/1.7/simulation/execution-and-playback.html).  

Edited: 3rd Sep. 2021
