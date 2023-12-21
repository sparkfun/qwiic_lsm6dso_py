#!/usr/bin/env python
#-------------------------------------------------------------------------------
# SparkFun_Qwiic_6DoF_LSM6DSO_Arduino_Library.py
#
# Demonstrates how to get basic measurements from the LSM6DSO 6DoF IMU
#-------------------------------------------------------------------------------
# Written by SparkFun Electronics, December 2023
#
# This python library supports the SparkFun Electroncis Qwiic ecosystem
#
# More information on Qwiic is at https://www.sparkfun.com/qwiic
#
# Do you like this library? Help support SparkFun. Buy a board!
#===============================================================================
# Copyright (c) 2023 SparkFun Electronics
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.
#===============================================================================

import qwiic_lsm6dso
import sys
import time

def runExample():
	print("\nQwiic LSM6DSO Example 1 - Basic Readings\n")

	# Create instance of device
	my_imu = qwiic_lsm6dso.QwiicLSM6DSO()

	# Check if it's connected
	if my_imu.is_connected() == False:
		print("The device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	# Initialize the device
	my_imu.begin()
	my_imu.initialize(my_imu.BASIC_SETTINGS)

	while True:
		print("Accelerometer: X:%.2f, Y:%.2f, Z:%.2f g" % \
			(my_imu.read_float_accel_x(), my_imu.read_float_accel_y(), my_imu.read_float_accel_z()))
		
		print("Gyroscope:     X:%.2f, Y:%.2f, Z:%.2f dps" % \
			(my_imu.read_float_gyro_x(), my_imu.read_float_gyro_y(), my_imu.read_float_gyro_z()))

		print("Temperature:   %.2f C" % my_imu.read_temp_c())

		time.sleep(1)

if __name__ == '__main__':
	try:
		runExample()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Example")
		sys.exit(0)