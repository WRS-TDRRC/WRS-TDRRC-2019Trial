# WRS-TDRRC-2019Trial
The material storage of World Robot Summit(Competition) Tunnel Disaster Response and Recovery Challenge 2019 Trial 

## Requirements  

  1. [Choreonoid version 1.7](https://choreonoid.org/en/manuals/1.7/index.html)  
  2. [AGX for Choreonoid](https://choreonoid.org/en/manuals/latest/agxdynamics/index.html), [Downloading AGX](https://www.algoryx.se/download/?id=1887)  

## How to use this repository  
If you have to install choreonoid now, please follow below commands:  

    $ cd ~  
    $ git clone -b "release-1.7" https://github.com/s-nakaoka/choreonoid.git  
    $ cd choreonoid/ext  
    $ wget https://github.com/WRS-TDRRC/WRS-TDRRC-2019Trial/blob/master/WRS2019.zip  
    $ unzip WRS2019.zip  
    $ cd ~/choreonoid && mkdir build && cd build  
    $ cmake .. -DBUILD_AGX_DYNAMICS_PLUGIN=ON -DBUILD_AGX_BODYEXTENSION_PLUGIN=ON -DBUILD_MULTICOPTER_PLUGIN=ON -DBUILD_MULTICOPTER_SAMPLES=ON -DBUILD_SCENE_EFFECTS_PLUGIN=ON -DBUILD_WRS2018=ON  
    $ make -j8  
  
Or you are already using choreonoid version 1.7, please follow below commands:  
(When your choreonoid is under ~/choreonoid)  

    $ cd ~/choreonoid/ext  
    $ wget https://github.com/WRS-TDRRC/WRS-TDRRC-2019Trial/blob/master/WRS2019.zip  
    $ unzip WRS2019.zip  
    $ cd ~/choreonoid/build  
    $ cmake . -DBUILD_AGX_DYNAMICS_PLUGIN=ON -DBUILD_AGX_BODYEXTENSION_PLUGIN=ON -DBUILD_MULTICOPTER_PLUGIN=ON -DBUILD_MULTICOPTER_SAMPLES=ON -DBUILD_SCENE_EFFECTS_PLUGIN=ON -DBUILD_WRS2018=ON  
    $ make -j8  

Please find field images and run scripts in the [wiki page](https://github.com/WRS-TDRRC/WRS-TDRRC-2019Trial/wiki).  

## The location of the simulation log files  
After running a simulation, you can find a simulation log file under ~/choreonoid/ext/WRS2019/project.  
Please see also [Choreonoid documentation](https://choreonoid.org/en/manuals/1.7/simulation/execution-and-playback.html).  

Edited: 16th Jan. 2020
