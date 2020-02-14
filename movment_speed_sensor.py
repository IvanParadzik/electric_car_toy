import pigpio
import time
import socket
import codecs

rpi= pigpio.pi()
speed_sensor = 24

rpi.set_mode(speed_sensor, pigpio.INPUT)



port = 50001 # Reserve a port for your service every new transfer wants a new port or you must wait.
s = socket.socket()  # Create a socket object
host = '192.168.0.25'  # Get local machine name
s.bind((host, port))  # Bind to the port
s.listen(5)  # Now wait for client connection.
print('Server listening....')

RotationCount = 0
last = 1
value = 1
end_time = 0
start_time = 0
speed = 0

while True:
    conn, address = s.accept()  # Establish connection with client.
    time.sleep(.1)

    while True:
        measure = False
        value = rpi.read(speed_sensor)
        if last == 0 and value == 1:
            if RotationCount == 0:
                start_time = time.time()
        if value == 0 and last == 1:
            RotationCount += 1

            if RotationCount == 20:
                end_time = time.time()
                RotationCount = 0
                measure = True
        last = rpi.read(speed_sensor)
        if measure:
            final_time = end_time - start_time
            speed = round(20.5 /final_time)
            speed = str(speed)
            final = codecs.encode(speed)
            conn.send(final)


