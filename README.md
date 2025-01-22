![Qwiic LSM6DSO Python Package](docs/images/lsm6dso-gh-banner-py.png "qwiic LSM6DSO Python Package" )

# SparkFun Qwiic LSM6DSO - Python Package

![PyPi Version](https://img.shields.io/pypi/v/sparkfun_qwiic_lsm6dso)
![GitHub issues](https://img.shields.io/github/issues/sparkfun/qwiic_lsm6dso_py)
![License](https://img.shields.io/github/license/sparkfun/qwiic_lsm6dso_py)
![X](https://img.shields.io/twitter/follow/sparkfun)
[![API](https://img.shields.io/badge/API%20Reference-blue)](https://docs.sparkfun.com/qwiic_lsm6dso_py/classqwiic__lsm6dso_1_1_qwiic_l_s_m6_d_s_o.html)

The SparkFun Qwiic LSM6DSO 6DoF Accelerometer Breakout provides a simple, powerful, and cost effective solution for adding accelerometer and gyroscsope measurements to your project. Implementing a SparkFun Qwiic I2C interface, these sensors can be rapidly added to any project with boards that are part of the SparkFun Qwiic ecosystem.

This repository implements a Python package for the SparkFun Qwiic LSM6DSO. This package works with Python, MicroPython and CircuitPython.

### Contents

* [About](#about-the-package)
* [Getting Started](#getting-started)
* [Installation](#installation)
* [Supported Platforms](#supported-platforms)
* [Documentation](https://docs.sparkfun.com/qwiic_lsm6dso_py/classqwiic__lsm6dso_1_1_qwiic_l_s_m6_d_s_o.html)
* [Examples](#examples)

## About the Package

This python package enables the user to access the features of the LSM6DSO via a single Qwiic cable. This includes reading the accelerometer, gyroscope, and more! The capabilities of the LSM6DSO are each demonstrated in the included examples.

New to qwiic? Take a look at the entire [SparkFun qwiic ecosystem](https://www.sparkfun.com/qwiic).

### Supported SparkFun Products

This Python package supports the following SparkFun qwiic products on Python, MicroPython and Circuit python. 

* [SparkFun 6 Degrees of Freedom Breakout - LSM6DSO (Qwiic)](https://www.sparkfun.com/sparkfun-6-degrees-of-freedom-breakout-lsm6dso-qwiic.html)

### Supported Platforms

| Python | Platform | Boards |
|--|--|--|
| Python | Linux | [Raspberry Pi](https://www.sparkfun.com/raspberry-pi-5-8gb.html) , [NVIDIA Jetson Orin Nano](https://www.sparkfun.com/nvidia-jetson-orin-nano-developer-kit.html) via the [SparkFun Qwiic SHIM](https://www.sparkfun.com/sparkfun-qwiic-shim-for-raspberry-pi.html) |
| MicroPython | Raspberry Pi - RP2, ESP32 | [SparkFun RP2040 Thing+](https://www.sparkfun.com/sparkfun-thing-plus-rp2040.html), [SparkFun RP2350 Thing+](https://www.sparkfun.com/sparkfun-thing-plus-rp2350.html), [SparkFun ESP32 Thing+](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-usb-c.html)
|CircuitPython | Raspberry Pi - RP2, ESP32 | [SparkFun RP2040 Thing+](https://www.sparkfun.com/sparkfun-thing-plus-rp2040.html), [SparkFun RP2350 Thing+](https://www.sparkfun.com/sparkfun-thing-plus-rp2350.html), [SparkFun ESP32 Thing+](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-usb-c.html)

> [!NOTE]
> The listed supported platforms and boards are the primary platform targets tested. It is fully expected that this package will work across a wide variety of Python enabled systems. 

## Installation 

The first step to using this package is installing it on your system. The install method depends on the python platform. The following sections outline installation on Python, MicroPython and CircuitPython.

### Python 

The package is primarily installed using the `pip` command, downloading the package from the Python Index - "PyPi". Note - the below instructions outline installation an Linux-based (Raspberry Pi) system.

#### PyPi Installation

The SparkFun Qwiic LSM6DSO Python package is part of the overall SparkFun Qwiic Python package which is hosted on PyPi. On systems that support PyPi installation via pip, this library is installed using the following commands

For all users (note: the user must have sudo privileges):
```sh
sudo pip install sparkfun-qwiic
```
For the current user:

```sh
pip install sparkfun-qwiic
```
---
---
> [!CAUTION]
> **TODO** Put together how this works with the new virtual environments used with the latest Python install
---
---
#### Local Installation
To install, make sure the setuptools package is installed on the system.

Direct installation at the command line:
```sh
python setup.py install
```

To build a package for use with pip:
```sh
python setup.py sdist
 ```
A package file is built and placed in a subdirectory called dist. This package file can be installed using pip.
```sh
cd dist
pip install sparkfun_qwiic_lsm6dso-<version>.tar.gz
```

### MicroPython Installation
If not already installed, follow the [instructions here](https://docs.micropython.org/en/latest/reference/mpremote.html) to install mpremote on your computer.

Connect a device with MicroPython installed to your computer and then install the package directly to your device with mpremote mip.
```sh
mpremote mip install github:sparkfun/qwiic_lsm6dso_py
```

### CircuitPython Installation
If not already installed, follow the [instructions here](https://docs.circuitpython.org/projects/circup/en/latest/#installation) to install CircUp on your computer.

Ensure that you have the latest version of the SparkFun Qwiic CircuitPython bundle. 
```sh
circup bundle-add sparkfun/Qwiic_Py
```

Finally, connect a device with CircuitPython installed to your computer and then install the package directly to your device with circup.
```sh
circup install --py qwiic_lsm6dso
```

Example Use
 ---------------
Below is a quickstart program to print acceleromter and gyro readings from the LSM6DSO.

See the examples directory for more detailed use examples and [examples/README.md](https://github.com/sparkfun/qwiic_lsm6dso_py/blob/main/examples/README.md) for a summary of the available examples.

```python
import qwiic_lsm6dso
import sys
import time

def runExample():
	print("\nQwiic LSM6DSO Example 1 - Basic Readings\n")

	my_imu = qwiic_lsm6dso.QwiicLSM6DSO()

	if my_imu.is_connected() == False:
		print("The device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	my_imu.begin()

	while True:
		accX, accY, accZ, gyrX, gyrY, gyrZ = my_imu.read_float_accel_gyro_all()
		
		print("Accelerometer: X:%.2f, Y:%.2f, Z:%.2f g" % (accX, accY, accZ))
		print("Gyroscope:     X:%.2f, Y:%.2f, Z:%.2f dps" % (gyrX, gyrY, gyrZ))

		temperature = my_imu.read_temp_c()
		print("Temperature:   %.2f C" % temperature)

		print()

		time.sleep(1)

if __name__ == '__main__':
	try:
		runExample()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Example")
		sys.exit(0)
```
<p align="center">
<img src="https://cdn.sparkfun.com/assets/custom_pages/3/3/4/dark-logo-red-flame.png" alt="SparkFun - Start Something">
</p>
