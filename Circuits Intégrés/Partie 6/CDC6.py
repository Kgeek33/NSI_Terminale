import serial
serial_port = serial.Serial(port = 'COM8', baudrate = 9600)

for i in range(10):
    octetsRecus = serial_port.readline()
    print("trame:" , octetsRecus)
    chaineRecue = octetsRecus.decode()
    print(chaineRecue)

serial_port.close()