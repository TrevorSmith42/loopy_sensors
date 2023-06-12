# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT



import board, time
from adafruit_apds9960.apds9960 import APDS9960

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_color = True


# Uncomment and set the rotation if depending on how your sensor is mounted.
# apds.rotation = 270 # 270 for CLUE

while True:

    print(apds.proximity)

    if (apds.color_data_ready):
        r, g, b, c = apds.color_data
        print(f"r: {r}, g: {g}, b: {b}, c: {c}")
