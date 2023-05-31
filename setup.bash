sudo apt-get install libusb-1.0
sudo pip3 install adafruit-circuitpython-apds9960

pip3 install pyftdi
pip3 install adafruit-blinka
export BLINKA_FT232H=1



pip3 install pyftdi
# # Change this later to run and exit python check 

# python3 

# from pyftdi.ftdi import Ftdi
# Ftdi().open_from_url('ftdi:///?')



# # /etc/udev/rules.d/11-ftdi.rules

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