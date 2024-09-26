import serial

SERIAL_PORT = "COM13"
SERIAL_BAUDRATE = 115200

lidarSerial = serial.Serial(SERIAL_PORT, SERIAL_BAUDRATE, timeout=0)

message = ""

while True:
    rx = lidarSerial.read(1000)

    message += rx.decode('utf-8')

    if message.find("170 0") > 0: message = message[message.find("170 0"):]

    if message.count("170 0") > 1:
        n = message[5:].find("170 0")
        data = message[:n+5]
        message = message[n+5:]

        data = data.strip().split(" ")
        # print("data:", data)

        if len(data) <= 11:
            print("zzz")
        else:
            print(data[2], len(data), data[7])