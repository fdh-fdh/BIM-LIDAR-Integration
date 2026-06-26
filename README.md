<img width="700" alt="pic2" src="https://github.com/RicoGoOne/Negative_diff/assets/77194729/43670ac0-6a0e-4541-972a-349e6f74b3f4">

# BIM-LIDAR Integration

## Description
2024.03-2024.10 HIWI@Chair of [CCBE](https://www.cee.ed.tum.de/ccbe/home/)
This Python project involves the identification of negative differences between LIDAR point cloud data and Building Information Models (BIM), along with feature extraction from the point cloud using various perception steps. The goal is to facilitate updates to the current BIM model by detecting conflicts and inconsistencies.

## Installation
To get started, follow these steps:
1. Clone this repository.
```shell
$ git clone https://github.com/RicoGoOne/Negative_diff.git
```
2. Create a Conda environment using the provided `requirements.txt` file.
```shell
$ conda create --name <env> --file requirements.txt
```





## Features and Usage
This repository is organized into two directories:

1. [**Clustering**:](https://github.com/RicoGoOne/Negative_diff/blob/main/Clustering/README.md) Utilizes octree-based clustering to discover negative conflicts between LIDAR scans and the BIM model. It includes further perception steps such as downsampling, outlier removal, and clustering of conflict point clouds.

2. [**BIM Update**:](https://github.com/RicoGoOne/Negative_diff/blob/main/BIM_update/README.md) Creates new instances in the IFC (Industry Foundation Classes) structure for updating purposes.

## Data

Lidar scans

[Data](https://www.dropbox.com/scl/fo/pa0vyz2x2mhag687yn96u/h?rlkey=u8k34suf70qvp2tnwciruijiu&dl=0)


## libraries and softwares
[Octomap](https://github.com/wkentaro/octomap-python) Python binding of the OctoMap library.

[Open3d](https://github.com/isl-org/Open3D) an open-source library that supports rapid development of software that deals with 3D data.

[FME](https://hub.safe.com/?page=1&page_size=10&order=updated_at_desc) FME is a purpose data integration platform for visualizing and transforming data with custom workflows.



## Known Issues
1. If this project will be extented, pls recheck if all instancies in requirment.txt necessary. Significant redudancies exists. 

2. A Function to read the unit of input ifc and change the corresponding pos calculation factor could be improved.

3. BIMupdate-Toolbox-find_containing_wall: both version could not find for all voids with the right wall. There is two version in the Toolbox, V1@Miguel vega.

4. Unitest might need be updated and improved
   
## Credits
Donghao Fang
