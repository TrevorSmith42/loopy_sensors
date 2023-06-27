import serial
import numpy as np

port = '/dev/ttyUSB2'  # Replace 'X' with the actual port number or '/dev/ttyX' for Linux
baud_rate = 57600  # Should match the baud rate set in the Arduino code
ser = serial.Serial(port, baud_rate)

sensor_data = np.zeros((36,4))
sensor_id = 0
initialized = False

while True:
    if ser.inWaiting() > 0:  # Check if there is data available to be read
        data = ser.readline()  # Read a line of data from the serial port
        try:
            data_str = data.decode('utf-8', errors='ignore').strip()
            if data_str.startswith('start'):
                initialized = True
                sensor_id = 0
                print("start")
                
            elif initialized:
                red = int(data_str)
                sensor_data[sensor_id,0] = red
                
                for gbc in range(1,4):
                    data = ser.readline()
                    color = int(data.decode('utf-8', errors='ignore').strip())
                    sensor_data[sensor_id,gbc] = color
                
                sensor_id +=1

        except UnicodeDecodeError:
            print("Error decoding data:", data)




