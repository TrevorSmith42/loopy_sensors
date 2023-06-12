# loopy_sensors.py
# By: Nathan Adkins
# email: npa00003@mix.wvu.edu
# WVU IRL 

import board, time
from adafruit_tca9548a import TCA9548A
from adafruit_apds9960.apds9960 import APDS9960
'''
**Note**:
    Run this in a terminal before running this script:

    export BLINKA_FT232H=1

'''

VALID_MUX_ADDRESSES = [0x70, 0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77]

class LoopySensors():


    def __init__(self, addresses: list, collect_color: bool = True, collect_gesture: bool = False, collect_proximity: bool = False):

        self._i2c = board.I2C() 

        self._multiplexer_addresses: list[int]= addresses
        self._multiplexer_objects: list[TCA9548A] = [] 
        self._collect_color = collect_color
        self._collect_gesture = collect_gesture
        self._collect_proximity = collect_proximity

        self.light_sensors: list[list[APDS9960]] = []

        for current_address in self._multiplexer_addresses:
            self._multiplexer_objects.append(TCA9548A(i2c=self._i2c, address= current_address))
        print(str(self._multiplexer_objects))
        
        mux_number = 0 
        for current_multiplexer in self._multiplexer_objects:
            print("Iterating through multiplexer objects " + str(current_multiplexer))
            new_light_sensors: list[APDS9960]= [] 
            mux_channel_number = 0 

            for multiplexer_output in current_multiplexer:
                try:
                    new_light_sensor = APDS9960(multiplexer_output)
                    new_light_sensor.enable_color = self._collect_color
                    new_light_sensor.enable_gesture = self._collect_gesture
                    new_light_sensor.enable_proximity = self._collect_proximity
                    new_light_sensors.append(new_light_sensor)
                except Exception:
                    print("Skipping output " + str(mux_channel_number) + " on mux " + str(mux_number))
                mux_channel_number += 1 
            mux_number += 1 

            self.light_sensors.append(new_light_sensors)


    def collect_color_readings(self):
        color_list: list[tuple[int,int,int,int]] = []
        for sensor_list in self.light_sensors:
            for sensor in sensor_list:
                while not sensor.color_data_ready:
                    pass
                color_list.append(sensor.color_data)
        return color_list
    

loopy = LoopySensors(VALID_MUX_ADDRESSES[0:4])


def main():
    while True:
        time.sleep(0.050)
        print(str(loopy.collect_color_readings()))

if __name__ == '__main__':
    main()
