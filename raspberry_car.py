import socket  # Import socket module
import codecs
import time
import subprocess


import pigpio
from numpy import interp
## initilazing sensor
echoPin = 12
trigPin = 17
rpi = pigpio.pi()
#camera servo
camPin = 11
pw_cam = 1550
rpi.set_servo_pulsewidth(camPin, pw_cam)
#sensor_servo

servo_sensor = 23
pw_sensor = 2400
rpi.set_servo_pulsewidth(servo_sensor, pw_sensor)
## ruka
servoPIN1 = 27  ##left
servoPIN2 = 6    ##right
servoPIN3 = 5  ## base
servoPIN4 = 22 ##finger



pw1 = 1500
pw2 = 1500
pw3 = 1500
pw4 = 1700
rpi.set_servo_pulsewidth(servoPIN1, pw1)
rpi.set_servo_pulsewidth(servoPIN2,pw2)
rpi.set_servo_pulsewidth(servoPIN3, pw3)
rpi.set_servo_pulsewidth(servoPIN4,pw4)
time.sleep(.1)




# MOTOR1 (FRONT RIGHT)
forward1 =26
backward1 = 19
pwm1 = 13
# MOTOR2 (FRONT LEFT)
forward2 =21
backward2 = 20
pwm2 = 16
# MOTOR3 (BACK RIGHT)
forward3 = 3
backward3 = 2
pwm3 = 4
# MOTOR4 (BACK LEFT)
forward4 =15
backward4 = 14
pwm4 = 18
# set up GPIO pins

rpi.set_mode(pwm1, pigpio.OUTPUT) # Connected to PWMA
rpi.set_mode(forward1, pigpio.OUTPUT) # Connected to AIN2
rpi.set_mode(backward1, pigpio.OUTPUT) # Connected to AIN1

rpi.set_mode(pwm2, pigpio.OUTPUT) # Connected to PWMA
rpi.set_mode(forward2, pigpio.OUTPUT) # Connected to AIN2
rpi.set_mode(backward2, pigpio.OUTPUT) # Connected to AIN1

rpi.set_mode(pwm3, pigpio.OUTPUT) # Connected to PWMA
rpi.set_mode(forward3, pigpio.OUTPUT) # Connected to AIN2
rpi.set_mode(backward3, pigpio.OUTPUT) # Connected to AIN1

rpi.set_mode(pwm4, pigpio.OUTPUT) # Connected to PWMA
rpi.set_mode(forward4, pigpio.OUTPUT) # Connected to AIN2
rpi.set_mode(backward4, pigpio.OUTPUT) # Connected to AIN1


#sensor

rpi.set_mode(echoPin, pigpio.INPUT)
rpi.set_mode(trigPin, pigpio.OUTPUT)

rpi.set_PWM_range(pwm1, 255)
rpi.set_PWM_range(pwm2, 255)
rpi.set_PWM_range(pwm3, 255)
rpi.set_PWM_range(pwm4, 255)

def forward_direction():
    rpi.write(forward1, 1)
    rpi.write(backward1, 0)
    rpi.write(pwm1, 1)
    rpi.write(forward2, 1)
    rpi.write(backward2, 0)
    rpi.write(pwm2, 1)
    rpi.write(forward3, 1)
    rpi.write(backward3, 0)
    rpi.write(pwm3, 1)
    rpi.write(forward4, 1)
    rpi.write(backward4, 0)
    rpi.write(pwm4, 1)

def backward_direction():
    rpi.write(forward1, 0)
    rpi.write(backward1, 1)
    rpi.write(pwm1, 1)
    rpi.write(forward2, 0)
    rpi.write(backward2, 1)
    rpi.write(pwm2, 1)
    rpi.write(forward3, 0)
    rpi.write(backward3, 1)
    rpi.write(pwm3, 1)
    rpi.write(forward4, 0)
    rpi.write(backward4, 1)
    rpi.write(pwm4, 1)

def backward():
    backward_direction()
    rpi.set_PWM_dutycycle(pwm1, 255)
    rpi.set_PWM_dutycycle(pwm2, 255)
    rpi.set_PWM_dutycycle(pwm3, 255)
    rpi.set_PWM_dutycycle(pwm4, 255)

def backward_right():
    backward_direction()
    rpi.set_PWM_dutycycle(pwm1, 80)
    rpi.set_PWM_dutycycle(pwm2, 255)
    rpi.set_PWM_dutycycle(pwm3, 80)
    rpi.set_PWM_dutycycle(pwm4, 255)

def backward_left():
    backward_direction()
    rpi.set_PWM_dutycycle(pwm1, 255)
    rpi.set_PWM_dutycycle(pwm2, 80)
    rpi.set_PWM_dutycycle(pwm3, 255)
    rpi.set_PWM_dutycycle(pwm4, 80)

def forward():
    forward_direction()
    rpi.set_PWM_dutycycle(pwm1, 255)
    rpi.set_PWM_dutycycle(pwm2, 255)
    rpi.set_PWM_dutycycle(pwm3, 255)
    rpi.set_PWM_dutycycle(pwm4, 255)

def forward_left():
    forward_direction()
    rpi.set_PWM_dutycycle(pwm1, 255)
    rpi.set_PWM_dutycycle(pwm2, 80)
    rpi.set_PWM_dutycycle(pwm3, 255)
    rpi.set_PWM_dutycycle(pwm4, 100)

def forward_rigth():
    forward_direction()
    rpi.set_PWM_dutycycle(pwm1, 80)
    rpi.set_PWM_dutycycle(pwm2, 255)
    rpi.set_PWM_dutycycle(pwm3, 80)
    rpi.set_PWM_dutycycle(pwm4, 255)

def right():
    forward_direction()
    rpi.set_PWM_dutycycle(pwm1, 0)
    rpi.set_PWM_dutycycle(pwm2, 255)
    rpi.set_PWM_dutycycle(pwm3, 0)
    rpi.set_PWM_dutycycle(pwm4, 255)

def left():
    forward_direction()
    rpi.set_PWM_dutycycle(pwm1, 255)
    rpi.set_PWM_dutycycle(pwm2, 0)
    rpi.set_PWM_dutycycle(pwm3, 255)
    rpi.set_PWM_dutycycle(pwm4, 0)


def stop():
    rpi.set_PWM_dutycycle(pwm1, 0)
    rpi.set_PWM_dutycycle(pwm2, 0)
    rpi.set_PWM_dutycycle(pwm3, 0)
    rpi.set_PWM_dutycycle(pwm4, 0)





port = 50002 # Reserve a port for your service every new transfer wants a new port or you must wait.
s = socket.socket()  # Create a socket object
host = '192.168.0.25'  # Get local machine name
s.bind((host, port))  # Bind to the port
s.listen(5)  # Now wait for client connection.

print('Server listening....')






def ultrasonic():
    pulse_start = 0
    pulse_end = 0
    rpi.write(trigPin, 0)
    time.sleep(0.0001)
    rpi.write(trigPin, 1)
    time.sleep(0.00001)
    rpi.write(trigPin, 0)
    count = 0
    while rpi.read(echoPin) == 0:
        pulse_start = time.time()
        count += 1
        if count > 100:
            break
    while rpi.read(echoPin) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150 * 2
    distance = distance / 2
    distance =int(round(distance))

    return distance





change_direction = 1
def sensor_move(pw_sensor,change_direction):
    if pw_sensor == 2300:
        change_direction = -1
    if pw_sensor == 700:
        change_direction = 1

    pw_sensor += 50 * change_direction

    rpi.set_servo_pulsewidth(servo_sensor, pw_sensor)



subprocess.Popen(["python3", "distance.py"])
subprocess.Popen(["python3","rasp_cam.py"])
subprocess.Popen(["python3","wheel.py"])

first = True
while True:
    conn, address = s.accept()  # Establish connection with client.
    time.sleep(.1)
    # count = 0
    # radar_direction = 1
    # change_direction = 1
    while True:
        try:
            data = conn.recv(1024)
            data = codecs.decode(data)

            x_y = data.split(" ")
            # distance = ultrasonic()
            print(x_y)
            # keys for moving direction
            try:

                if int(x_y[0]) == 1 and int(x_y[2]) == 1:
                    forward_left()
                    time.sleep(0.2)

                elif int(x_y[0]) == 1 and int(x_y[3]) == 1:
                    forward_rigth()

                elif int(x_y[0]) == 1:
                    forward()
                    time.sleep(0.2)

                elif int(x_y[1]) == 1 and int(x_y[2]) == 1:
                    backward_left()
                    time.sleep(0.2)
                elif int(x_y[1]) == 1 and int(x_y[3]) == 1:
                    backward_right()
                    time.sleep(0.2)
                elif int(x_y[1]) == 1:
                    backward()

                elif int(x_y[2]) == 1:
                    left()
                    time.sleep(0.2)

                elif int(x_y[3]) == 1:
                    right()
                    time.sleep(0.2)

                else:
                    stop()



                if int(x_y[4]) == 1:
                    if pw1 < 2500:
                        pw1 += 20
                        rpi.set_servo_pulsewidth(servoPIN1, pw1)

                if int(x_y[5]) == 1:
                    if pw1 > 500:
                        pw1 -= 20
                        rpi.set_servo_pulsewidth(servoPIN1, pw1)

                if int(x_y[6]) ==1:
                    if pw2 < 2500:
                        pw2 += 20
                        rpi.set_servo_pulsewidth(servoPIN2, pw2)

                if int(x_y[7]) == 1:
                    if pw2 > 500:
                        pw2 -= 20
                        rpi.set_servo_pulsewidth(servoPIN2, pw2)

                if int(x_y[10]) == 1:
                    if pw3 < 2500:
                        pw3 += 20
                        rpi.set_servo_pulsewidth(servoPIN3, pw3)

                if int(x_y[11]) == 1:
                    if pw3 > 500:
                        pw3 -= 20
                        rpi.set_servo_pulsewidth(servoPIN3, pw3)

                if int(x_y[8]) == 1:
                    if pw4 < 1700:
                        pw4 += 20
                        rpi.set_servo_pulsewidth(servoPIN4, pw4)

                if int(x_y[9]) == 1:
                    if pw4 > 1300:
                        pw4 -= 20
                        rpi.set_servo_pulsewidth(servoPIN4, pw4)

                ##moving camera

                if int(x_y[12]) == 1:
                    if pw_cam < 2200:
                        pw_cam += 20
                        rpi.set_servo_pulsewidth(camPin, pw_cam)

                if int(x_y[13]) == 1:
                    if pw_cam > 800:
                        pw_cam -= 20
                        rpi.set_servo_pulsewidth(camPin, pw_cam)
            except:
                continue
            # sending data about camera

            camera_pw = str(pw_cam)
            final = codecs.encode(camera_pw)
            conn.send(final)

            first = False
        except Exception as e:
            print(e)
            break

    conn.close()