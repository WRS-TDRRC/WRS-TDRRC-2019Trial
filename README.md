# WRS-TDRRC-2019Trial
The material storage of World Robot Summit(Competition) Tunnel Disaster Response and Recovery Challenge 2019 Trial 

## Requirements  

  1. [Choreonoid version 1.7](https://choreonoid.org/en/manuals/1.7/index.html)  
  2. [AGX for Choreonoid](https://choreonoid.org/en/manuals/latest/agxdynamics/index.html), [Downloading AGX](https://www.algoryx.se/download/?id=1887)  

## How to use this repository  

  1. Download WRS2019.zip  
  2. Unzip WRS2019.zip under ~/choreonoid/ext (After extracting, you can see ~/choreonoid/ext/WRS2019)  
  3. Re-configuring CMakeLists.txt under ~/choreonoid/build.  
      cd ~/choreonoid/build && cmake .  
  4. Rebuild:  
      cd ~/choreonoid/build && make  

Please find field images and run scripts in the [wiki page](https://github.com/WRS-TDRRC/WRS-TDRRC-2019Trial/wiki).  

## The location of the simulation log files  
After running a simulation, you can find a simulation log file under ~/choreonoid/ext/WRS2019/project.  

Edited: 9th Jan. 2020
