import board
from adafruit_tca9548a import TCA9548A
from adafruit_apds9960.apds9960 import APDS9960

VALID_MUX_ADDRESSES = [0x70, 0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77]

class LoopySensors():


    def __init__(self, addresses: list):

        self.i2c = board.I2C() 

        self.multiplexer_addresses: list[int]= addresses
        self.multiplexer_objects: list[TCA9548A] = [] 

        self.light_sensors: list[list[APDS9960]] = []

        for current_address in self.multiplexer_addresses:
            self.multiplexer_objects: list[TCA9548A] = [(TCA9548A(i2c=self.i2c, address= current_address))]
        
        mux_number = 0 
        for current_multiplexer in self.multiplexer_objects:
            new_light_sensors: list[APDS9960]= [] 
            mux_channel_number = 0 

            for multiplexer_output in current_multiplexer:
                try:
                    new_light_sensors.append(APDS9960(multiplexer_output))
                except Exception:
                    print("Skipping output " + str(mux_channel_number) + " on mux " + str(mux_number))
                mux_channel_number += 1 
            mux_number += 1 

            self.light_sensors.append([new_light_sensors])



loopy = LoopySensors(VALID_MUX_ADDRESSES[0:4])

print(str(loopy.light_sensors))
print(str(len(loopy.light_sensors)))

