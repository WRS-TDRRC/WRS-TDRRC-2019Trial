# WRS-TDRRC-2019Trial
The material storage of World Robot Summit(Competition) Tunnel Disaster Response and Recovery Challenge 2019 Trial 

## Requirements  

  1. [Choreonoid (tag=wrs2019)](https://choreonoid.org/en/manuals/latest/index.html), [Installing Choreonoid](https://choreonoid.org/en/manuals/latest/install/build-ubuntu.html#development-version). If you use ROS melodic, see also [Teleoperation Sample using ROS](https://choreonoid.org/en/manuals/latest/wrs2018/teleoperation-ros.html)  
  2. [AGX for Choreonoid](https://choreonoid.org/en/manuals/latest/agxdynamics/index.html), [Downloading AGX](https://www.algoryx.se/download/?id=1887), [Installing AGX](https://www.algoryx.se/documentation/complete/agx/tags/latest/UserManual/source/installation.html#install-on-ubuntu-16-04). The AGX version is 2.21.3.1 which was used in WRS2018. There are capability that higher version which can be used will be found.  
 
## How to use this repository  
If you have to install choreonoid now, please follow below commands:  

    $ cd ~  
    $ git clone -b "wrs2019" https://github.com/choreonoid/choreonoid.git  
    $ ~/choreonoid/misc/script/install-requisites-ubuntu-16.04.sh  
    $ sudo apt-get install qt5-default libqt5x11extras5-dev qt5-style-plugins  
    $ cd ~/choreonoid/ext  
    $ wget https://github.com/WRS-TDRRC/WRS-TDRRC-2019Trial/blob/master/WRS2019.zip  
    $ unzip WRS2019.zip  
    $ cd ~/choreonoid && mkdir build && cd build  
    $ cmake .. -DBUILD_AGX_DYNAMICS_PLUGIN=ON -DBUILD_AGX_BODYEXTENSION_PLUGIN=ON -DBUILD_COMPETITION_PLUGIN=ON -DENABLE_CORBA=ON -DBUILD_CORBA_PLUGIN=ON -DBUILD_MULTICOPTER_PLUGIN=ON -DBUILD_MULTICOPTER_SAMPLES=ON -DBUILD_SCENE_EFFECTS_PLUGIN=ON -DBUILD_WRS2018=ON  
    $ make -j8  
  
Or you are already using choreonoid wrs2019, please follow below commands:  
(When your choreonoid is under ~/choreonoid)  

    $ cd ~/choreonoid && git checkout "wrs2019"  
    $ cd ~/choreonoid/ext  
    $ wget https://github.com/WRS-TDRRC/WRS-TDRRC-2019Trial/blob/master/WRS2019.zip  
    $ unzip WRS2019.zip  
    $ cd ~/choreonoid/build  
    $ cmake .. -DBUILD_AGX_DYNAMICS_PLUGIN=ON -DBUILD_AGX_BODYEXTENSION_PLUGIN=ON -DBUILD_COMPETITION_PLUGIN=ON -DENABLE_CORBA=ON -DBUILD_CORBA_PLUGIN=ON -DBUILD_MULTICOPTER_PLUGIN=ON -DBUILD_MULTICOPTER_SAMPLES=ON -DBUILD_SCENE_EFFECTS_PLUGIN=ON -DBUILD_WRS2018=ON  
    $ make -j8  

Please find field images and run scripts in the [wiki page](https://github.com/WRS-TDRRC/WRS-TDRRC-2019Trial/wiki).  

## The location of the simulation log files  
After running a simulation, you can find a simulation log file under ~/choreonoid/ext/WRS2019/project.  
Please see also [Choreonoid documentation](https://choreonoid.org/en/manuals/1.7/simulation/execution-and-playback.html).  

Edited: 7th feb. 2020
