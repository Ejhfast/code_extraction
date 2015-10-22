# Python i2c write_bus_data usage
b.write_i2c_block_data(0x31, 5, [0, 8]) # write number 8 to digit 0
b.write_i2c_block_data(0x31, 5, [4, 5]) # write number 5 to digit 4 etc etc
