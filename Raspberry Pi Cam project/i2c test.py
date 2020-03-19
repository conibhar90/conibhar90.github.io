import smbus
import time
from time import sleep
import binascii


arduino_address = 0x08;     #Arduino I2C address
I2C_bus = smbus.SMBus(1);     #I2C bus setup

cmd_str = str(input("input commands: "))          


def I2C_write(commands):
    #This function converts string user input into bytes.
    #Then sends the data via I2C protocol to Arduino.
    
    mov_cmd = []
    for b in commands:      
        mov_cmd.append(ord(b))
    I2C_bus.write_i2c_block_data(arduino_address, 0x00, mov_cmd)
    print(str(mov_cmd))
    
def listen_I2C():
    #wait and listen for a reply from Arduino
    
    ack_results = I2C_bus.read_byte(arduino_address)
    return ack_results


I2C_write(cmd_str)

