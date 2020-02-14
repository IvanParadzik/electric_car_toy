import socket  # Import socket module
import codecs
import time
import RPi.GPIO as GPIO


import pigpio
from numpy import interp
## initilazing sensor
echoPin = 12
trigPin = 17
rpi = pigpio.pi()


servo_sensor = 23
pw_sensor = 2400
rpi.set_servo_pulsewidth(servo_sensor, pw_sensor)

def ultrasonic():
    pulse_start = 0
    pulse_end = 0
    rpi.write(trigPin, 0)
    time.sleep(0.1)
    rpi.write(trigPin, 1)
    time.sleep(0.00001)
    rpi.write(trigPin, 0)
    count = 0
    while rpi.read(echoPin) == 0:
        pulse_start = time.time()
        count += 1
        if count > 1000:
            break
    while rpi.read(echoPin) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150 * 2
    distance = distance / 2
    distance =int(round(distance))

    return distance


port = 50000 # Reserve a port for your service every new transfer wants a new port or you must wait.
s = socket.socket()  # Create a socket object
host = '192.168.0.25'  # Get local machine name
s.bind((host, port))  # Bind to the port
s.listen(5)  # Now wait for client connection.


count = print('Server listening....')
radar_direction = 1
change_direction = 1
while True:
    conn, address = s.accept()  # Establish connection with client.
    time.sleep(.1)
    while True:
        distance = ultrasonic()
        if pw_sensor == 2400:
            change_direction = -1
            radar_direction = 1
        if pw_sensor == 600:
            change_direction = 1
            radar_direction = -1

        pw_sensor += 25 * change_direction
        count += 1 * radar_direction
        rpi.set_servo_pulsewidth(servo_sensor, pw_sensor)

        # sending info about distance sensor
        sonar_value = [count, distance]
        sonar_str = str(sonar_value)
        final_value = []
        for k in sonar_str:
            if k == '[' or k == ',' or k == ']':
                pass
            else:
                final_value.append(k)
        new = ''
        for x in final_value:
            new = new + x

        final = codecs.encode(new)
        conn.send(final)
