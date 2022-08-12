# install on windows

## 1. Introduction

CARLA has been developed from the ground up to support development, training, and validation of autonomous driving systems. In addition to open-source code and protocols, CARLA provides open digital assets (urban layouts, buildings, vehicles) that were created for this purpose and can be used freely. The simulation platform supports flexible specification of sensor suites, environmental conditions, full control of all static and dynamic actors, maps generation and much more.

## 2. Installation

This guide shows how to download and install the packaged version of CARLA. The package includes the CARLA server and two options for the client library. There are additional assets that can be downloaded and imported into the package.

### 2.1 Before you begin

The following requirements should be fulfilled before installing CARLA:

#### 2.1.1 Attention

- **System requirements.** CARLA is built for Windows and Linux systems.

- **An adequate GPU.** CARLA aims for realistic simulations, so the server needs at least a 6 GB GPU although we would recommend 8 GB. A dedicated GPU is highly recommended for machine learning.

- **Disk space.** CARLA will use about 20 GB of space.

- **Python.** [Python](https://carla.readthedocs.io/en/latest/start_quickstart/(https://www.python.org/downloads/)) is the main scripting language in CARLA. CARLA supports Python 2.7 and Python 3 on Linux, and Python 3 on Windows.

- **Pip.** Some installation methods of the CARLA client library require **pip** or **pip3** (depending on your Python version) version 20.3 or higher. 

- **Two TCP ports and good internet connection.** 2000 and 2001 by default. Make sure that these ports are not blocked by firewalls or any other applications.

- **Other requirements.** CARLA requires some Python dependencies. Install the dependencies according to your operating system.

  #### 2.1.2 Tips

   To check your **pip** version:

  ```
   # For Python 3
   pip3 -V
   # For Python 3, If you need to upgrade:
   pip3 install --upgrade pip
  ```

   Install the dependencies according to your operating system:

  ```
  # Windows
  pip3 install --user pygame numpy
  
  # Linux
  pip install --user pygame numpy &&
  pip3 install --user pygame numpy
  ```

  ### 2.2 CARLA installation

  There are two methods to download and install CARLA as a package:

  **A)** [Download the Debian package.](https://carla.readthedocs.io/en/latest/start_quickstart/#a-debian-carla-installation)

  **B)** [Download the package from GitHub.](https://carla.readthedocs.io/en/latest/start_quickstart/#b-package-installation)



## Reference

1. [https://carla.org/](https://carla.org/)
2. [https://carla.readthedocs.io/en/latest/start_quickstart/](https://carla.readthedocs.io/en/latest/start_quickstart/)
