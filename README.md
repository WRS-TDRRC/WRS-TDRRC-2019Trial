# WRS-TDRRC-2019Trial
The material storage of World Robot Summit(Competition) Tunnel Disaster Response and Recovery Challenge 2019 Trial 

## Requirements  

  1. [Choreonoid](https://choreonoid.org/en/manuals/latest/index.html), [Installing Choreonoid](https://choreonoid.org/en/manuals/latest/install/build-ubuntu.html#development-version). If you use ROS melodic, see also [Teleoperation Sample using ROS](https://choreonoid.org/en/manuals/latest/wrs2018/teleoperation-ros.html)  
  2. [AGX for Choreonoid](https://choreonoid.org/en/manuals/latest/agxdynamics/index.html), [Downloading AGX](https://www.algoryx.se/download/?id=1887), [Installing AGX](https://www.algoryx.se/documentation/complete/agx/tags/latest/UserManual/source/installation.html#install-on-ubuntu-16-04). The last AGX version can be used.
  3. ROS catkin tools  
 
## How to use this repository WITH ROS  
If you have to install choreonoid now, please follow below commands:  

    $ sudo apt-get install python-catkin-tools qt5-default libqt5x11extras5-dev qt5-style-plugins  
    $ cd ~  
    $ mkdir -p catkin_ws/src  
    $ cd catkin_ws  
    $ catkin_init  
    $ cd src  
    $ git clone https://github.com/choreonoid/choreonoid.git  
    $ git clone https://github.com/choreonoid/choreonoid_ros.git  
    $ git clone https://github.com/choreonoid/choreonoid_ros_samples.git  
    $ git clone https://github.com/choreonoid/choreonoid_joy.git  
    $ git clone https://github.com/WRS-TDRRC/WRS-TDRRC-2019Trial choreonoid/ext/WRS2019  
    $ choreonoid/misc/script/install-requisites-ubuntu-18.04.sh  
    $ cd ..  
    $ cd ~/choreonoid && mkdir build && cd build  
    $ catkin config --cmake-args -DBUILD_CHOREONOID_EXECUTABLE=OFF -DCMAKE_BUILD_TYPE=Release -DBUILD_AGX_DYNAMICS_PLUGIN=ON -DBUILD_AGX_BODYEXTENSION_PLUGIN=ON -DBUILD_COMPETITION_PLUGIN=ON -DENABLE_CORBA=ON -DBUILD_CORBA_PLUGIN=ON -DBUILD_MULTICOPTER_PLUGIN=ON -DBUILD_MULTICOPTER_SAMPLES=ON -DBUILD_SCENE_EFFECTS_PLUGIN=ON -DBUILD_WRS2018=ON  
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
    $ cmake .. -DBUILD_AGX_DYNAMICS_PLUGIN=ON -DBUILD_AGX_BODYEXTENSION_PLUGIN=ON -DBUILD_COMPETITION_PLUGIN=ON -DENABLE_CORBA=ON -DBUILD_CORBA_PLUGIN=ON -DBUILD_MULTICOPTER_PLUGIN=ON -DBUILD_MULTICOPTER_SAMPLES=ON -DBUILD_SCENE_EFFECTS_PLUGIN=ON -DBUILD_WRS2018=ON  
    $ make -j8  
  
Or you are already using choreonoid, please follow below commands:  
(When your choreonoid is under ~/choreonoid)  

    $ cd ~/choreonoid/ext  
    $ git clone https://github.com/WRS-TDRRC/WRS-TDRRC-2019Trial WRS2019  
    $ cd ~/choreonoid/build  
    $ cmake .. -DBUILD_AGX_DYNAMICS_PLUGIN=ON -DBUILD_AGX_BODYEXTENSION_PLUGIN=ON -DBUILD_COMPETITION_PLUGIN=ON -DENABLE_CORBA=ON -DBUILD_CORBA_PLUGIN=ON -DBUILD_MULTICOPTER_PLUGIN=ON -DBUILD_MULTICOPTER_SAMPLES=ON -DBUILD_SCENE_EFFECTS_PLUGIN=ON -DBUILD_WRS2018=ON  
    $ make -j8  

Before run, you have to add "source /opt/Algoryx/AgX-VERSION-NUMBER/setup_env.bash" at the end of ~/.bashrc , and reopen the terminal.  
Please find field images and run scripts in the [wiki page](https://github.com/WRS-TDRRC/WRS-TDRRC-2019Trial/wiki).  

## The location of the simulation log files  
After running a simulation, you can find a simulation log file under ~/choreonoid/ext/WRS2019/project.  
Please see also [Choreonoid documentation](https://choreonoid.org/en/manuals/1.7/simulation/execution-and-playback.html).  

Edited: 7th Oct. 2020
