# Requirements for FT232H (USB to GPIO, SPI, I2C)
# -----------------------------------------------
# Links:
#   https://learn.adafruit.com/circuitpython-on-any-computer-with-ft232h/linux
# ----------------------------------------------------------------------------
sudo apt-get update
sudo apt-get install python3
sudo apt install python3-pip


# Requirements for FT232H (USB to GPIO, SPI, I2C)
# -----------------------------------------------
# Links:
#   https://learn.adafruit.com/circuitpython-on-any-computer-with-ft232h/linux
# ----------------------------------------------------------------------------
sudo apt-get install libusb-1.0
pip3 install pyftdi
pip3 install adafruit-blinka
export BLINKA_FT232H=1


# Requirements for TCA9548A (I2C Multiplexer Breakout)
# -------------------------------------------------------------
# Links:
#   https://learn.adafruit.com/adafruit-tca9548a-1-to-8-i2c-multiplexer-breakout/overview
# ---------------------------------------------------------------------------------------
sudo pip3 install adafruit-circuitpython-tca9548a


# Requirements for APDS9960 (Proximity, Light, Gesture, Sensor)
# -------------------------------------------------------------
# Links:
#   https://learn.adafruit.com/adafruit-apds9960-breakout/circuitpython
# -------------------------------------------------------------
sudo pip3 install adafruit-circuitpython-apds9960


# Create this U Dev Rule 
# ----------------------
# Links:
#   What is a Udev rule? https://en.wikipedia.org/wiki/Udev
# ---------------------------------------------------------
#   Copy the text below into the following file path:   /etc/udev/rules.d/11-ftdi.rules

    # # FT232AM/FT232BM/FT232R
    # SUBSYSTEM=="usb", ATTR{idVendor}=="0403", ATTR{idProduct}=="6001", GROUP="plugdev", MODE="0664"
    # # FT2232C/FT2232D/FT2232H
    # SUBSYSTEM=="usb", ATTR{idVendor}=="0403", ATTR{idProduct}=="6010", GROUP="plugdev", MODE="0664"
    # # FT4232/FT4232H
    # SUBSYSTEM=="usb", ATTR{idVendor}=="0403", ATTR{idProduct}=="6011", GROUP="plugdev", MODE="0664"
    # # FT232H
    # SUBSYSTEM=="usb", ATTR{idVendor}=="0403", ATTR{idProduct}=="6014", GROUP="plugdev", MODE="0664"
    # # FT230X/FT231X/FT234X
    # SUBSYSTEM=="usb", ATTR{idVendor}=="0403", ATTR{idProduct}=="6015", GROUP="plugdev", MODE="0664"