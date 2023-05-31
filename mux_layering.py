import time
import board
import busio
from adafruit_apds9960.apds9960 import APDS9960
import adafruit_tca9548a

i2c = busio.I2C(board.SCL, board.SDA)

mux0 = adafruit_tca9548a.TCA9548A(i2c)

mux1 = adafruit_tca9548a.TCA9548A(i2c)

TOP_MUX_OUTPUTS = 4
BOT_MUX_OUTPUTS = 1

sensor_list = []

for mux_mux_out in range(TOP_MUX_OUTPUTS):
    
    for mux_out in range(BOT_MUX_OUTPUTS):
        
        curr_sens = APDS9960(i2c)
        curr_sens.enable_proximity = True
        sensor_list.append(curr_sens)
        
while True:
    
    for mux_mux_out in range(TOP_MUX_OUTPUTS):
        mux0.address = mux_mux_out
    
        for mux_out in range(BOT_MUX_OUTPUTS):
            mux1.address = mux_out
        
        new_sensor_vals = []
        for sensor in sensor_list:
            new_sensor_vals.append(sensor.proximity)
            
        print(new_sensor_vals)
        time.sleep(0.001)




# import time
# import numpy as np
# import board
# from adafruit_apds9960.apds9960 import APDS9960
# import adafruit_tca9548a

# i2c = board.I2C()

# mux0 = adafruit_tca9548a.PCA9546A(i2c)

# mux1 = adafruit_tca9548a.PCA9546A(i2c)


# TOP_MUX_OUTPUTS = 4
# BOT_MUX_OUTPUTS = 1


# sensor_list = []

# for mux_mux_out in range(TOP_MUX_OUTPUTS):
    
    
#     for mux_out in range(BOT_MUX_OUTPUTS):
        
#         curr_sens = APDS9960(mux1[mux_out])
#         curr_sens.enable_proximity = True
#         sensor_list.append(curr_sens)
        
#     while True:
#         new_sensor_vals = []
#         for sensor in sensor_list:
#             new_sensor_vals.append(sensor.proximity)
        
#         print(new_sensor_vals)
#         time.sleep(0.001)









# import time
# import board
# from adafruit_apds9960.apds9960 import APDS9960
# import adafruit_tca9548a

# i2c = board.I2C()

# mux = adafruit_tca9548a.PCA9546A(i2c)



# sens0 = APDS9960(mux[0])
# sens1 = APDS9960(mux[1])

# sens0.enable_proximity = True
# sens1.enable_proximity = True


# # After initial setup, can just use sensors as normal.
# while True:
#     print(str(sens0.proximity) + " " + str(sens1.proximity))
#     time.sleep(0.001)