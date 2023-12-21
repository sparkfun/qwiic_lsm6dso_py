#-------------------------------------------------------------------------------
# qwiic_lsm6dso.py
#
# Python library for the SparkFun Qwiic 6-DoF LSM6DSO, available here:
# https://www.sparkfun.com/products/18020
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
# This code was generated in part with ChatGPT, created by OpenAI. The code was
# reviewed and edited by the following human(s):
#
# Dryw Wade
#===============================================================================

"""
qwiic_lsm6dso
============
Python module for the [SparkFun Qwiic 6-DoF LSM6DSO](https://www.sparkfun.com/products/18020)
This is a port of the existing [Arduino Library](https://github.com/sparkfun/SparkFun_Qwiic_6DoF_LSM6DSO_Arduino_Library)
This package can be used with the overall [SparkFun Qwiic Python Package](https://github.com/sparkfun/Qwiic_Py)
New to Qwiic? Take a look at the entire [SparkFun Qwiic ecosystem](https://www.sparkfun.com/qwiic).
"""

# The Qwiic_I2C_Py platform driver is designed to work on almost any Python
# platform, check it out here: https://github.com/sparkfun/Qwiic_I2C_Py
import qwiic_i2c

# Define the device name and I2C addresses. These are set in the class defintion
# as class variables, making them avilable without having to create a class
# instance. This allows higher level logic to rapidly create a index of Qwiic
# devices at runtine
_DEFAULT_NAME = "Qwiic LSM6DSO"

# Some devices have multiple available addresses - this is a list of these
# addresses. NOTE: The first address in this list is considered the default I2C
# address for the device.
_AVAILABLE_I2C_ADDRESS = [0x6B, 0x6A]

# Define the class that encapsulates the device being created. All information
# associated with this device is encapsulated by this class. The device class
# should be the only value exported from this module.
class QwiicLSM6DSO(object):
    # Set default name and I2C address(es)
    device_name         = _DEFAULT_NAME
    available_addresses = _AVAILABLE_I2C_ADDRESS

    # Register addresses
    FUNC_CFG_ACCESS        = 0x01
    LSM6DO_PIN_CTRL        = 0x02
    FIFO_CTRL1             = 0x07
    FIFO_CTRL2             = 0x08
    FIFO_CTRL3             = 0x09
    FIFO_CTRL4             = 0x0A
    COUNTER_BDR_REG1       = 0x0B
    COUNTER_BDR_REG2       = 0x0C
    INT1_CTRL              = 0x0D
    INT2_CTRL              = 0x0E
    WHO_AM_I_REG           = 0x0F
    CTRL1_XL               = 0x10
    CTRL2_G                = 0x11
    CTRL3_C                = 0x12
    CTRL4_C                = 0x13
    CTRL5_C                = 0x14
    CTRL6_C                = 0x15
    CTRL7_G                = 0x16
    CTRL8_XL               = 0x17
    CTRL9_XL               = 0x18
    CTRL10_C               = 0x19
    ALL_INT_SRC            = 0x1A
    WAKE_UP_SRC            = 0x1B
    TAP_SRC                = 0x1C
    D6D_SRC                = 0x1D
    STATUS_REG             = 0x1E
    OUT_TEMP_L             = 0x20
    OUT_TEMP_H             = 0x21
    OUTX_L_G               = 0x22
    OUTX_H_G               = 0x23
    OUTY_L_G               = 0x24
    OUTY_H_G               = 0x25
    OUTZ_L_G               = 0x26
    OUTZ_H_G               = 0x27
    OUTX_L_A               = 0x28
    OUTX_H_A               = 0x29
    OUTY_L_A               = 0x2A
    OUTY_H_A               = 0x2B
    OUTZ_L_A               = 0x2C
    OUTZ_H_A               = 0x2D
    EMB_FUNC_STATUS_MP     = 0x35
    FSM_FUNC_STATUS_A_MP   = 0x36
    FSM_FUNC_STATUS_B_MP   = 0x37
    STATUS_MASTER_MAINPAGE = 0x39
    FIFO_STATUS1           = 0x3A
    FIFO_STATUS2           = 0x3B
    TIMESTAMP0_REG         = 0x40
    TIMESTAMP1_REG         = 0x41
    TIMESTAMP2_REG         = 0x42
    TIMESTAMP3_REG         = 0x43
    TAP_CFG0               = 0x56
    TAP_CFG1               = 0x57
    TAP_CFG2               = 0x58
    TAP_THS_6D             = 0x59
    INT_DUR2               = 0x5A
    WAKE_UP_THS            = 0x5B
    WAKE_UP_DUR            = 0x5C
    FREE_FALL              = 0x5D
    MD1_CFG                = 0x5E
    MD2_CFG                = 0x5F
    I3C_BUS_AVB            = 0x62
    INTERNAL_FREQ_FINE     = 0x63
    INT_OIS                = 0x6F
    CTRL1_OIS              = 0x70
    CTRL2_OIS              = 0x71
    CTRL3_OIS              = 0x72
    X_OFS_USR              = 0x73
    Y_OFS_USR              = 0x74
    Z_OFS_USR              = 0x75
    FIFO_DATA_OUT_TAG      = 0x78
    FIFO_DATA_OUT_X_L      = 0x79
    FIFO_DATA_OUT_X_H      = 0x7A
    FIFO_DATA_OUT_Y_L      = 0x7B
    FIFO_DATA_OUT_Y_H      = 0x7C
    FIFO_DATA_OUT_Z_L      = 0x7D
    FIFO_DATA_OUT_Z_H      = 0x7E

    # Expected Who Am I value
    WHO_AM_I_VALUE = 0x6C
    
    # Default settings
    BASIC_SETTINGS = 0x00
    SOFT_INT_SETTINGS = 0x01
    HARD_INT_SETTINGS = 0x02
    FIFO_SETTINGS = 0x03
    PEDOMETER_SETTINGS = 0x04
    TAP_SETTINGS = 0x05
    FREE_FALL_SETTINGS = 0x06

    FS_XL_2g = 0x00
    FS_XL_16g = 0x04
    FS_XL_4g = 0x08
    FS_XL_8g = 0x0C
    FS_XL_MASK = 0xF3

    IF_INC_ENABLED = 0x04

    ODR_XL_DISABLE   = 0x00 
    ODR_XL_1_6Hz     = 0xB0 # Low Power only
    ODR_XL_12_5Hz    = 0x10 # Low Power only
    ODR_XL_26Hz      = 0x20 # Low Power only
    ODR_XL_52Hz      = 0x30 # Low Power only 
    ODR_XL_104Hz     = 0x40 # Normal Mode
    ODR_XL_208Hz     = 0x50 # Normal Mode
    ODR_XL_416Hz     = 0x60 # High performance
    ODR_XL_833Hz     = 0x70 # High Performance 
    ODR_XL_1660Hz    = 0x80 # High Performance
    ODR_XL_3330Hz    = 0x90 # High Performance
    ODR_XL_6660Hz    = 0xA0 # High Performance
    ODR_XL_MASK      = 0x0F

    FS_G_125dps   	= 0x02
    FS_G_250dps 	= 0x00
    FS_G_500dps 	= 0x04
    FS_G_1000dps 	= 0x08
    FS_G_2000dps 	= 0x0C
    FS_G_MASK       = 0xF0

    ODR_GYRO_DISABLE = 0x00
    ODR_GYRO_12_5Hz  = 0x10 # Low Power only
    ODR_GYRO_26Hz    = 0x20 # Low Power only
    ODR_GYRO_52Hz    = 0x30 # Low Power only
    ODR_GYRO_104Hz   = 0x40 # Normal Mode
    ODR_GYRO_208Hz   = 0x50 # Normal Mode
    ODR_GYRO_416Hz   = 0x60 # High performance
    ODR_GYRO_833Hz   = 0x70 # High Performance
    ODR_GYRO_1660Hz  = 0x80 # High Performance
    ODR_GYRO_3330Hz  = 0x90 # High Performance
    ODR_GYRO_6660Hz  = 0xA0 # High Performance
    ODR_GYRO_MASK    = 0x0F

    BDU_CONTINUOS 	 = 0x00
    BDU_BLOCK_UPDATE = 0x40
    BDU_MASK         = 0xBF 

    def __init__(self, address=None, i2c_driver=None):
        """
        Constructor

        :param address: The I2C address to use for the device
            If not provided, the default address is used
        :type address: int, optional
        :param i2c_driver: An existing i2c driver object
            If not provided, a driver object is created
        :type i2c_driver: I2CDriver, optional
        """

        # Use address if provided, otherwise pick the default
        self.address = self.available_addresses[0] if address is None else address

        # Load the I2C driver if one isn't provided
        if i2c_driver is None:
            self._i2c = qwiic_i2c.getI2CDriver()
            if self._i2c is None:
                print("Unable to load I2C driver for this platform.")
                return
        else:
            self._i2c = i2c_driver

        # Construct with these default imuSettings

        self.gyroEnabled = True  # Can be 0 or 1
        self.gyroRange = 500   # Max deg/s.  Can be: 125, 250, 500, 1000, 2000
        self.gyroSampleRate = 416   # Hz.  Can be: 13, 26, 52, 104, 208, 416, 833, 1666
        self.gyroBandWidth = 400  # Hz.  Can be: 50, 100, 200, 400
        self.gyroFifoEnabled = 1  # Set to include gyro in FIFO
        self.gyroAccelDecimation = 1  # Set to include gyro in FIFO

        self.accelEnabled = True
        self.accelRange = 8      # Max G force readable.  Can be: 2, 4, 8, 16
        self.accelSampleRate = 416  # Hz.  Can be: 1.6 (16), 12.5 (125), 26, 52, 104, 208, 416, 833, 1660, 3330, 6660
        self.accelFifoEnabled = 1  # Set to include accelerometer in the FIFO

        self.fifoEnabled = True
        self.fifoThreshold = 3000  # Can be 0 to 4096 (16 bit bytes)
        self.fifoSampleRate = 416 
        self.fifoModeWord = 0  # Default off

        self.allOnesCounter = 0
        self.nonSuccessCounter = 0

    def is_connected(self):
        """
        Determines if this device is connected

        :return: `True` if connected, otherwise `False`
        :rtype: bool
        """
        # Check if connected by seeing if an ACK is received
        if not self._i2c.isDeviceConnected(self.address):
            return False
        
        # Check the Who Am I register to see if it's correct
        return self._i2c.readByte(self.address, self.WHO_AM_I_REG) == self.WHO_AM_I_VALUE

    connected = property(is_connected)

    def begin(self):
        """
        Initializes this device with default parameters

        :return: Returns `True` if successful, otherwise `False`
        :rtype: bool
        """
        # Confirm device is connected before doing anything
        if not self.is_connected():
            return False

        # TODO Perform a reset of the device if possible. This reverts all
        # registers to a known state in case the device was reconfigured before

        # TODO: Configure device as needed. Once complete, the device should be
        # fully ready to use to make it very simple for the user

        # TODO: Return True once successful. Template defaults to False!
        return False

    def initialize(self, settings):
        self.set_increment()

        if settings == self.BASIC_SETTINGS:
            self.set_accel_range(8)
            self.set_accel_data_rate(416)
            self.set_gyro_range(500)
            self.set_gyro_data_rate(416)
            self.set_block_data_update(True)
        elif settings == self.SOFT_INT_SETTINGS:
            self.set_accel_range(8)
            self.set_accel_data_rate(416)
            self.set_gyro_range(500)
            self.set_gyro_data_rate(416)
        elif settings == self.HARD_INT_SETTINGS:
            self.set_interrupt_one(self.INT1_DRDY_XL_ENABLED)
            self.set_interrupt_two(self.INT2_DRDY_G_ENABLED) 
            self.set_accel_range(8)
            self.set_accel_data_rate(416)
            self.set_gyro_range(500)
            self.set_gyro_data_rate(416)
        elif settings == self.FIFO_SETTINGS:
            self.set_fifo_depth(500)  # bytes
            # set_ts_decimation()  # FIFO_CTRL4
            # get_samples_stored()  # FIFO_STATUS1 and STATUS2
            self.set_accel_batch_data_rate(417)
            self.set_gyro_batch_data_rate(417)
            self.set_fifo_mode(self.FIFO_MODE_STOP_WHEN_FULL)  
            self.set_accel_range(8)
            self.set_accel_data_rate(833)
            self.set_gyro_range(500)
            self.set_gyro_data_rate(833)
        elif settings == self.PEDOMETER_SETTINGS:
            self.enable_embedded_functions(True)
            self.set_accel_data_rate(52)
            self.enable_pedometer(True)
        elif settings == self.TAP_SETTINGS:
            self.set_accel_range(2)
            self.set_accel_data_rate(417)  # Must be at least 417
            self.enable_tap(True, True, True, True)
            self.set_tap_dir_prior(self.TAP_PRIORITY_YXZ)
            self.set_x_threshold(9)
            self.configure_tap(0x06)
            self.route_hard_inter_one(self.INT1_SINGLE_TAP_ENABLED)
            # set_tap_clear_on_read(True)  # TAP_CFG0
        elif settings == self.FREE_FALL_SETTINGS:
            self.enable_embedded_functions(True)
            # set_free_fall(True)
            # get_free_fall()

        return True

    def set_accel_range(self, range):
        if range < 0 or range > 16:
            return False

        reg_val = 0
        full_scale = 0
        reg_val = self._i2c.readByte(self.address, self.CTRL1_XL)

        full_scale = self.get_accel_full_scale()

        # Can't have 16g with XL_FS_MODE == 1
        if full_scale == 1 and range == 16:
            range = 8

        reg_val &= self.FS_XL_MASK

        if range == 2:
            reg_val |= self.FS_XL_2g
        elif range == 4:
            reg_val |= self.FS_XL_4g
        elif range == 8:
            reg_val |= self.FS_XL_8g
        elif range == 16:
            reg_val |= self.FS_XL_16g

        self._i2c.writeByte(self.address, self.CTRL1_XL, reg_val)

    def set_accel_data_rate(self, rate):
        if rate < 16 or rate > 6660:
            return False

        reg_val = 0
        high_perf = 0
        reg_val = self._i2c.readByte(self.address, self.CTRL1_XL)

        high_perf = self.get_accel_high_perf()

        if high_perf == 0 and rate == 16:
            rate = 125

        reg_val &= self.ODR_XL_MASK

        if rate == 0:
            reg_val |= self.ODR_XL_DISABLE
        elif rate == 16:
            reg_val |= self.ODR_XL_1_6Hz
        elif rate == 125:
            reg_val |= self.ODR_XL_12_5Hz
        elif rate == 26:
            reg_val |= self.ODR_XL_26Hz
        elif rate == 52:
            reg_val |= self.ODR_XL_52Hz
        elif rate == 104:
            reg_val |= self.ODR_XL_104Hz
        elif rate == 208:
            reg_val |= self.ODR_XL_208Hz
        elif rate == 416:
            reg_val |= self.ODR_XL_416Hz
        elif rate == 833:
            reg_val |= self.ODR_XL_833Hz
        elif rate == 1660:
            reg_val |= self.ODR_XL_1660Hz
        elif rate == 3330:
            reg_val |= self.ODR_XL_3330Hz
        elif rate == 6660:
            reg_val |= self.ODR_XL_6660Hz

        self._i2c.writeByte(self.address, self.CTRL1_XL, reg_val)

    def get_accel_full_scale(self):
        reg_val = self._i2c.readByte(self.address, self.CTRL8_XL)
        return (reg_val & 0x02) >> 1

    def get_accel_high_perf(self):
        reg_val = self._i2c.readByte(self.address, self.CTRL6_C)
        return (reg_val & 0x10) >> 4

    def set_gyro_data_rate(self, rate):
        if rate < 0 or rate > 6660:
            return False

        reg_val = self._i2c.readByte(self.address, self.CTRL2_G)

        reg_val &= self.ODR_GYRO_MASK

        if rate == 0:
            reg_val |= self.ODR_GYRO_DISABLE
        elif rate == 125:
            reg_val |= self.ODR_GYRO_12_5Hz
        elif rate == 26:
            reg_val |= self.ODR_GYRO_26Hz
        elif rate == 52:
            reg_val |= self.ODR_GYRO_52Hz
        elif rate == 104:
            reg_val |= self.ODR_GYRO_104Hz
        elif rate == 208:
            reg_val |= self.ODR_GYRO_208Hz
        elif rate == 416:
            reg_val |= self.ODR_GYRO_416Hz
        elif rate == 833:
            reg_val |= self.ODR_GYRO_833Hz
        elif rate == 1660:
            reg_val |= self.ODR_GYRO_1660Hz
        elif rate == 3330:
            reg_val |= self.ODR_GYRO_3330Hz
        elif rate == 6660:
            reg_val |= self.ODR_GYRO_6660Hz

        self._i2c.writeByte(self.address, self.CTRL2_G, reg_val)

    def set_gyro_range(self, range):
        if range < 250 or range > 2000:
            return False

        reg_val = self._i2c.readByte(self.address, self.CTRL2_G)

        reg_val &= self.FS_G_MASK

        if range == 125:
            reg_val |= self.FS_G_125dps
        elif range == 250:
            reg_val |= self.FS_G_250dps
        elif range == 500:
            reg_val |= self.FS_G_500dps
        elif range == 1000:
            reg_val |= self.FS_G_1000dps
        elif range == 2000:
            reg_val |= self.FS_G_2000dps

        self._i2c.writeByte(self.address, self.CTRL2_G, reg_val)

    def set_block_data_update(self, enable):
        reg_val = self._i2c.readByte(self.address, self.CTRL3_C)
        
        reg_val &= 0xBF
        reg_val |= self.BDU_BLOCK_UPDATE
        
        self._i2c.writeByte(self.address, self.CTRL3_C, reg_val)
        
    def set_increment(self, enable = True):
        reg_val = self._i2c.readByte(self.address, self.CTRL3_C)

        reg_val &= 0xFD
        reg_val |= self.IF_INC_ENABLED

        self._i2c.writeByte(self.address, self.CTRL3_C, reg_val)

    def read_raw_accel_x(self):
        output = self._i2c.readWord(self.address, self.OUTX_L_A)
        return output

    def read_float_accel_x(self):
        output = self.calc_accel(self.read_raw_accel_x())
        return output

    def read_raw_accel_y(self):
        output = self._i2c.readWord(self.address, self.OUTY_L_A)
        return output

    def read_float_accel_y(self):
        output = self.calc_accel(self.read_raw_accel_y())
        return output

    def read_raw_accel_z(self):
        output = self._i2c.readWord(self.address, self.OUTZ_L_A)
        return output

    def read_float_accel_z(self):
        output = self.calc_accel(self.read_raw_accel_z())
        return output

    def calc_accel(self, input):
        accel_range = 0
        scale = 0
        output = 0.0

        accel_range = self._i2c.readByte(self.address, self.CTRL1_XL)
        scale = (accel_range >> 1) & 0x01
        accel_range = (accel_range >> 2) & (0x03)

        # Convert input to signed 16-bit
        if input >= 2**15:
            input -= 2**16

        if scale == 0:
            if accel_range == 0:  # Register value 0: 2g
                output = (float(input) * 0.061) / 1000
            elif accel_range == 1:  # Register value 1: 16g
                output = (float(input) * 0.488) / 1000
            elif accel_range == 2:  # Register value 2: 4g
                output = (float(input) * 0.122) / 1000
            elif accel_range == 3:  # Register value 3: 8g
                output = (float(input) * 0.244) / 1000

        if scale == 1:
            if accel_range == 0:  # Register value 0: 2g
                output = (float(input) * 0.061) / 1000
            elif accel_range == 1:  # Register value 1: 2g
                output = (float(input) * 0.061) / 1000
            elif accel_range == 2:  # Register value 2: 4g
                output = (float(input) * 0.122) / 1000
            elif accel_range == 3:  # Register value 3: 8g
                output = (float(input) * 0.244) / 1000

        return output

    def read_raw_gyro_x(self):
        output = self._i2c.readWord(self.address, self.OUTX_L_G)
        return output

    def read_float_gyro_x(self):
        output = self.calc_gyro(self.read_raw_gyro_x())
        return output

    def read_raw_gyro_y(self):
        output = self._i2c.readWord(self.address, self.OUTY_L_G)
        return output

    def read_float_gyro_y(self):
        output = self.calc_gyro(self.read_raw_gyro_y())
        return output

    def read_raw_gyro_z(self):
        output = self._i2c.readWord(self.address, self.OUTZ_L_G)
        return output

    def read_float_gyro_z(self):
        output = self.calc_gyro(self.read_raw_gyro_z())
        return output

    def calc_gyro(self, input):
        gyro_range = 0
        full_scale = 0
        output = 0

        gyro_range = self._i2c.readByte(self.address, self.CTRL2_G)
        full_scale = (gyro_range >> 1) & 0x01
        gyro_range = (gyro_range >> 2) & 0x03

        # Convert input to signed 16-bit
        if input >= 2**15:
            input -= 2**16

        if full_scale:
            output = (float(input) * 4.375) / 1000
        else:
            if gyro_range == 0:
                output = (float(input) * 8.75) / 1000
            elif gyro_range == 1:
                output = (float(input) * 17.50) / 1000
            elif gyro_range == 2:
                output = (float(input) * 35) / 1000
            elif gyro_range == 3:
                output = (float(input) * 70) / 1000

        return output

    def read_raw_temp(self):
        output = self._i2c.readWord(self.address, self.OUT_TEMP_L)
        return output

    def read_temp_c(self):
        temp = self.read_raw_temp()
        msb_temp = (temp & 0xFF00) >> 8
        temp_float = float(msb_temp)
        lsb_temp = temp & 0x00FF
        lsb_temp /= 256
        temp_float += lsb_temp
        temp_float += 25  # Add 25 degrees to remove offset
        return temp_float

    def read_temp_f(self):
        output = self.read_temp_c()
        output = (output * 9) / 5 + 32
        return output