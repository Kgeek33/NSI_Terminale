import serial

serial_port = serial.Serial(port="COM13", baudrate=9600)

for i in range(10):
    octetsRecus = serial_port.readline()  
    print("trame: ", octetsRecus)
    chaine_recu = octetsRecus.decode()
    print(chaine_recu)

serial_port.close()
