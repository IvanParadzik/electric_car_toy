import pygame
from settings import Settings
import socket
import pygame.locals
import codecs
import time
import os
import sys
from numpy import interp
import math
import json
import subprocess


def check_key(key):
    pressedKeys = pygame.key.get_pressed()
    return pressedKeys[key]

class Car():

    def __init__(self):
        settings = Settings()
        os.environ['SDL_VIDEO_CENTERED'] = "0,500"
        pygame.init()
        pygame.display.set_caption('CAR')
        self.new_data = 0
        self.distance = 0
        self.key_list = [0,0,0,0]
        self.first = False



    def run_sonar(self):
        # from distance_data import data_list
        # time.sleep(0.001)
        # if not self.first:
        #     self.new_data = data_list[0]
        #     self.distance = data_list[1]
        try:
            if not self.first:
                with open('data.txt', 'r') as image:
                    lines = json.load(image)
                    data = lines["distance_count"]
                    print(data)
                    self.new_data = data[0]
                    self.distance = data[1]
        except:
            print('Error')

        # if not self.first:
        #     data = s.recv(4000)
        #     data = codecs.decode(data)
        #     c_d = data.split(" ")
        #     c_d = [x.replace("\r\n", "") for x in c_d]
        #     self.new_data = int(c_d[0])
        #     self.distance = int(c_d[1])


        settings = Settings()

        screen.fill(settings.rgb_color)
        pygame.draw.circle(screen, (0, 255, 50), (int(settings.screen_width/2), settings.screen_height), 505)
        pygame.draw.circle(screen, (0, 110, 0), (int(settings.screen_width/2), settings.screen_height), 500)
        pygame.draw.circle(screen, (0, 255, 50), (int(settings.screen_width/2), settings.screen_height), round(506 * 4 / 5))
        pygame.draw.circle(screen, (0, 110, 0), (int(settings.screen_width/2), settings.screen_height), round(500 * 4 / 5))
        pygame.draw.circle(screen, (0, 255, 50), (int(settings.screen_width/2), settings.screen_height), round(509 * 3 / 5))
        pygame.draw.circle(screen, (0, 110, 0), (int(settings.screen_width/2), settings.screen_height), round(500 * 3 / 5))
        pygame.draw.circle(screen, (0, 255, 50), (int(settings.screen_width/2), settings.screen_height), round(512 * 2 / 5))
        pygame.draw.circle(screen, (0, 110, 0), (int(settings.screen_width/2), settings.screen_height), round(500 * 2 / 5))
        pygame.draw.circle(screen, (0, 255, 50), (int(settings.screen_width/2), settings.screen_height), round(527 * 1 / 5))
        pygame.draw.circle(screen, (0, 110, 0), (int(settings.screen_width/2), settings.screen_height), round(500 * 1 / 5))
        pygame.draw.line(screen, (0, 255, 50,0), (int(settings.screen_width/2), settings.screen_height), (500, 0), 4)
        if self.distance > 100:
            self.distance = 100
        if self.distance < 20:
            self.distance = 20

        print(self.distance)
        diag = interp(self.distance, [10,100], [0,500])

        green_line = [screen, (0, 255, 0), (500, settings.screen_height), (
        settings.screen_width / 2 + math.cos((math.pi / 72) * self.new_data) * settings.screen_width / 2,
        settings.screen_height - math.sin((math.pi / 72) * self.new_data) * settings.screen_width / 2), 6]
        green_shades = [ (0, 110, 0),(0, 110, 0),(0, 110, 0),(0, 110, 0),(0, 120, 0),(0, 120, 0),(0, 120, 0),(0, 120, 0), (0, 130, 0), (0, 130, 0),(0, 130, 0), (0, 130, 0), (0, 140, 0),(0, 140, 0),(0, 140, 0),(0, 140, 0), (0, 150, 0),(0, 150, 0), (0, 150, 0),(0, 150, 0),(0, 160, 0),(0, 160, 0), (0, 160, 0),(0, 160, 0),(0, 170, 0), (0, 170, 0),(0, 170, 0), (0, 170, 0),(0, 180, 0),(0, 180, 0),(0, 180, 0),(0, 180, 0), (0, 190, 0), (0, 190, 0), (0, 190, 0), (0, 190, 0),(0, 200, 0),(0, 200, 0),(0, 200, 0),(0, 200, 0),(0, 210, 0),(0, 210, 0),(0, 210, 0),(0, 210, 0),(0, 220, 0),(0, 220, 0),(0, 220, 0),(0, 220, 0),(0, 230, 0),(0, 230, 0),(0, 230, 0),(0, 230, 0),(0, 240, 0),(0, 240, 0),(0, 240, 0),(0, 240, 0),(0, 250, 0),(0, 250, 0),(0, 250, 0),(0, 250, 0) ]
        red_shades = [(110, 0 ,0 ),(110, 0 ,0 ),(110, 0 ,0 ),(110, 0 ,0 ),(120, 0 ,0 ),(120, 0 ,0 ),(120, 0 ,0 ),(120, 0 ,0 ),(130, 0 ,0 ),(130, 0 ,0 ),(130, 0 ,0 ),(130, 0 ,0 ),(140, 0 ,0 ),(140, 0 ,0 ),(140, 0 ,0 ),(140, 0 ,0 ),(150, 0 ,0 ),(150, 0 ,0 ),(150, 0 ,0 ),(150, 0 ,0 ),(160, 0 ,0 ),(160, 0 ,0 ),(160, 0 ,0 ),(160, 0 ,0 ),(170, 0 ,0 ),(170, 0 ,0 ),(170, 0 ,0 ),(170, 0 ,0 ),(180, 0 ,0 ),(180, 0 ,0 ),(180, 0 ,0 ),(180, 0 ,0 ),(190, 0 ,0 ),(190, 0 ,0 ),(190, 0 ,0 ),(190, 0 ,0 ),(200, 0 ,0 ),(200, 0 ,0 ),(200, 0 ,0 ),(200, 0 ,0 ),(210, 0 ,0 ),(210, 0 ,0 ),(210, 0 ,0 ),(210, 0 ,0 ),(220, 0 ,0 ),(220, 0 ,0 ),(220, 0 ,0 ),(220, 0 ,0 ),(230, 0 ,0 ),(230, 0 ,0 ),(230, 0 ,0 ),(230, 0 ,0 ),(240, 0 ,0 ),(240, 0 ,0 ),(240, 0 ,0 ),(240, 0 ,0 ),(250, 0 ,0 ),(250, 0 ,0 ),(250, 0 ,0 ),(250, 0 ,0 )]
        red_line = [screen, (255,0 , 0), (500 +diag* math.cos((math.pi / 72) * self.new_data), settings.screen_height- diag*math.sin((math.pi / 72) * self.new_data )), (
        settings.screen_width / 2 + math.cos((math.pi / 72) * self.new_data) * settings.screen_width / 2,
        settings.screen_height - math.sin((math.pi / 72) * self.new_data) * settings.screen_width / 2), 6]
        draw_green_line.append(green_line)
        draw_red_line.append(red_line)
        if not self.first:
            if self.new_data == 72:
                draw_green_line.clear()
                draw_red_line.clear()
            elif self.new_data == 0:
                draw_green_line.clear()
                draw_red_line.clear()
        if len(draw_green_line) < 60:
            green = -len(draw_green_line)
            for i in draw_green_line:
                pygame.draw.line(i[0],green_shades[green],i[2],i[3],i[4])
                green += 1
        elif len(draw_green_line)> 59:
            green= 0
            for i in draw_green_line:
                pygame.draw.line(i[0],green_shades[green],i[2],i[3],i[4])
                green +=1
        if len(draw_red_line) < 60:
            red = -len(draw_red_line)
            for i in draw_red_line:
                pygame.draw.line(i[0],red_shades[red],i[2],i[3],i[4])
                red += 1
        elif len(draw_red_line) > 59:
            red = 0
            for i in draw_red_line:
                pygame.draw.line(i[0],red_shades[red],i[2],i[3],i[4])
                red += 1

        if len(draw_green_line)> 59:
            del draw_green_line[0]
        if len(draw_red_line)> 59:
            del draw_red_line[0]



        pygame.display.flip()
        self.first = False




subprocess.Popen([sys.executable,"distance_data.py"])
subprocess.Popen([sys.executable,"camera.py"])
subprocess.Popen([sys.executable,"speed_car.py"])

s = socket.socket()  # Create a socket object
port = 50002 # Reserve a port for your service every new transfer wants a new port or you must wait.

s.connect(('192.168.0.25', port))

car = Car()
settings = Settings()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

key_list = [0]*15
key_bool = [False]*15






def check_buttons():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                key_bool[0] = True
            if event.key == pygame.K_s:
                key_bool[1] = True
            if event.key == pygame.K_a:
                key_bool[2] = True
            if event.key == pygame.K_d:
                key_bool[3] = True
            if event.key == pygame.K_u:
                key_bool[4] = True
            if event.key == pygame.K_j:
                key_bool[5] = True
            if event.key == pygame.K_i:
                key_bool[6] = True
            if event.key == pygame.K_k:
                key_bool[7] = True
            if event.key == pygame.K_o:
                key_bool[8] = True
            if event.key == pygame.K_p:
                key_bool[9] = True
            if event.key == pygame.K_n:
                key_bool[10] = True
            if event.key == pygame.K_m:
                key_bool[11] = True
            if event.key == pygame.K_c:
                key_bool[12] = True
            if event.key == pygame.K_v:
                key_bool[13] = True
            if event.key == pygame.K_SPACE:
                key_bool[14] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                key_bool[0] = False
            if event.key == pygame.K_s:
                key_bool[1] = False
            if event.key == pygame.K_a:
                key_bool[2] = False
            if event.key == pygame.K_d:
                key_bool[3] = False
            if event.key == pygame.K_u:
                key_bool[4] =False
            if event.key == pygame.K_j:
                key_bool[5] = False
            if event.key == pygame.K_i:
                key_bool[6] = False
            if event.key == pygame.K_k:
                key_bool[7] = False
            if event.key == pygame.K_o:
                key_bool[8] = False
            if event.key == pygame.K_p:
                key_bool[9] =False
            if event.key == pygame.K_n:
                key_bool[10] = False
            if event.key == pygame.K_m:
                key_bool[11] = False
            if event.key == pygame.K_c:
                key_bool[12] = False
            if event.key == pygame.K_v:
                key_bool[13] = False
            if event.key == pygame.K_SPACE:
                key_bool[14] = False

        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
    for x in range(15):
        if key_bool[x]:
            key_list[x] = 1
        else:
            key_list[x]= 0



first = True
def sensor_data(first):
    if not first:
        try:
            old_distance = 0
            old_data = 0
            with open('data.txt', 'r') as image:
                lines = json.load(image)
                data = lines["distance_count"]
                print(data)
                new_data = data[0]
                distance = data[1]
                old_data = new_data
                old_distance = distance
        except:
            print('Error')
            distance = old_distance
            new_data = old_data
    else:
        distance = 0
        new_data = 0


    return [new_data ,distance]

def blit_sonar(new_data ,distance):


    black = (0, 0, 0)
    green = (0, 110, 0)
    light_green = (0 , 250, 50)


    sonar_surface = pygame.Rect(0, 0, settings.screen_width, settings.screen_height)
    pygame.draw.rect(screen, settings.rgb_color, sonar_surface)
    pygame.draw.circle(screen, (0, 255, 50), (int(settings.screen_width / 2), 0), 505)
    pygame.draw.circle(screen, (0, 110, 0), (int(settings.screen_width / 2), 0), 500)
    pygame.draw.circle(screen, (0, 255, 50), (int(settings.screen_width / 2), 0),
                       round(506 * 4 / 5))
    pygame.draw.circle(screen, (0, 110, 0), (int(settings.screen_width / 2), 0),
                       round(500 * 4 / 5))
    pygame.draw.circle(screen, (0, 255, 50), (int(settings.screen_width / 2),0),
                       round(509 * 3 / 5))
    pygame.draw.circle(screen, (0, 110, 0), (int(settings.screen_width / 2), 0),
                       round(500 * 3 / 5))
    pygame.draw.circle(screen, (0, 255, 50), (int(settings.screen_width / 2), 0),
                       round(512 * 2 / 5))
    pygame.draw.circle(screen, (0, 110, 0), (int(settings.screen_width / 2), 0),
                       round(500 * 2 / 5))
    pygame.draw.circle(screen, (0, 255, 50), (int(settings.screen_width / 2),0),
                       round(527 * 1 / 5))
    pygame.draw.circle(screen, (0, 110, 0), (int(settings.screen_width / 2),0),
                       round(500 * 1 / 5))
    pygame.draw.line(screen, (0, 255, 50, 0), (int(settings.screen_width / 2), 0), (int(settings.screen_width / 2), 500), 4)
    pygame.draw.line(screen, (0, 255, 50, 0), (int(settings.screen_width / 2), 0),
                     (int(settings.screen_width / 2)- int(settings.screen_width/2) * math.cos(math.pi/4), int(settings.screen_width/2) * math.sin(math.pi/4)), 5)
    pygame.draw.line(screen, (0, 255, 50, 0), (int(settings.screen_width / 2), 0),
                     (int(settings.screen_width / 2) - int(settings.screen_width / 2) * math.cos(math.pi*3 / 4),
                      int(settings.screen_width / 2) * math.sin(math.pi*3 / 4)), 5)

    if distance > 150:
        distance = 150


    print(distance)
    diag = interp(distance, [0, 150], [0, 500])


    green_line = [screen, (0, 255, 0), (500, 0), (
        settings.screen_width / 2 - math.cos((math.pi / 72) * new_data) * settings.screen_width / 2,
        math.sin((math.pi / 72) * new_data) * settings.screen_width / 2), 6]
    green_shades = [(0, 110, 0), (0, 110, 0), (0, 120, 0),
                    (0, 120, 0), (0, 130, 0), (0, 130, 0),
                    (0, 140, 0), (0, 140, 0), (0, 150, 0), (0, 150, 0), (0, 160, 0),
                     (0, 160, 0),  (0, 170, 0), (0, 170, 0),
                     (0, 180, 0), (0, 180, 0),  (0, 190, 0),
                    (0, 190, 0),  (0, 200, 0), (0, 200, 0),
                    (0, 210, 0), (0, 210, 0),  (0, 220, 0), (0, 220, 0),  (0, 230, 0), (0, 230, 0),  (0, 240, 0), (0, 240, 0),
                    (0, 250, 0), (0, 250, 0)]
    red_shades = [(110, 0, 0), (110, 0, 0), (120, 0, 0),
                  (120, 0, 0),  (130, 0, 0), (130, 0, 0),
                  (140, 0, 0), (140, 0, 0), (150, 0, 0), (150, 0, 0), (160, 0, 0),
                  (160, 0, 0),   (170, 0, 0), (170, 0, 0),
                 (180, 0, 0), (180, 0, 0),  (190, 0, 0),
                  (190, 0, 0), (200, 0, 0), (200, 0, 0), (210, 0, 0), (210, 0, 0),
                   (220, 0, 0), (220, 0, 0), (230, 0, 0),
                  (230, 0, 0),  (240, 0, 0), (240, 0, 0),
                  (250, 0, 0), (250, 0, 0)]
    red_line = [screen, (255, 0, 0), (500 - diag * math.cos((math.pi / 72) * new_data),
                                      diag * math.sin((math.pi / 72) * new_data)), (
        settings.screen_width / 2 - math.cos((math.pi / 72) * new_data) * settings.screen_width / 2,
        math.sin((math.pi / 72) * new_data) * settings.screen_width / 2), 6]
    draw_green_line.append(green_line)
    draw_red_line.append(red_line)
    if not first:
        if new_data == 72:
            draw_green_line.clear()
            draw_red_line.clear()
        elif new_data == 0:
            draw_green_line.clear()
            draw_red_line.clear()
    if len(draw_green_line) < 30:
        green = -len(draw_green_line)
        for i in draw_green_line:
            pygame.draw.line(i[0], green_shades[green], i[2], i[3], i[4])
            green += 1
    elif len(draw_green_line) > 29:
        green = 0
        for i in draw_green_line:
            pygame.draw.line(i[0], green_shades[green], i[2], i[3], i[4])
            green += 1
    if len(draw_red_line) < 30:
        red = -len(draw_red_line)
        for i in draw_red_line:
            pygame.draw.line(i[0], red_shades[red], i[2], i[3], i[4])
            red += 1
    elif len(draw_red_line) > 29:
        red = 0
        for i in draw_red_line:
            pygame.draw.line(i[0], red_shades[red], i[2], i[3], i[4])
            red += 1

    if len(draw_green_line) > 29:
        del draw_green_line[0]
    if len(draw_red_line) > 29:
        del draw_red_line[0]


    font = pygame.font.Font('freesansbold.ttf', 25)
    font2 = pygame.font.Font('freesansbold.ttf', 20)

    sonar_45 = font.render('45˙', True, black)
    sonar_45_rect = sonar_45.get_rect()
    sonar_45_rect.center = (110, 370)
    screen.blit(sonar_45, sonar_45_rect)

    sonar_90 = font.render(' 90˙', True, black)
    sonar_90_rect = sonar_90.get_rect()
    sonar_90_rect.center = (500, 520)
    screen.blit(sonar_90, sonar_90_rect)

    sonar_135 = font.render('135˙', True, black)
    sonar_135_rect = sonar_135.get_rect()
    sonar_135_rect.center = (890, 370)
    screen.blit(sonar_135, sonar_135_rect)


    sonar_30cm = font2.render('30 Cm', True, black)
    sonar_30cm_rect = sonar_30cm       .get_rect()
    sonar_30cm_rect.center = (450, 25)
    screen.blit(sonar_30cm, sonar_30cm_rect)
    sonar_60cm = font2.render('60 Cm', True, black)
    sonar_60cm_rect = sonar_60cm.get_rect()
    sonar_60cm_rect.center = (350, 25)
    screen.blit(sonar_60cm, sonar_60cm_rect)
    sonar_90cm = font2.render('90 Cm', True, black)
    sonar_90cm_rect = sonar_90cm.get_rect()
    sonar_90cm_rect.center = (250, 25)
    screen.blit(sonar_90cm, sonar_90cm_rect)
    sonar_120cm = font2.render('120 Cm', True, black)
    sonar_120cm_rect = sonar_120cm.get_rect()
    sonar_120cm_rect.center = (150, 25)
    screen.blit(sonar_120cm, sonar_120cm_rect)
    sonar_150cm = font2.render('150 Cm', True, black)
    sonar_150cm_rect = sonar_150cm.get_rect()
    sonar_150cm_rect.center = (50, 25)
    screen.blit(sonar_150cm, sonar_150cm_rect)

def blit_camera():
    try:
        image1 = pygame.image.load('car_image1.jpg')
    except:
        image1 = pygame.image.load('car_image2.jpg')
    screen.fill(settings.rgb_color)
    screen.blit(image1, [0, 0 ])



def blit_arm_buttons():
    black = (0, 0, 0)
    green = (0, 255, 0)

    square_u = pygame.Rect(0, 0, 30, 30)
    square_u.center =(710, 260)
    square_j = pygame.Rect(0, 0, 30, 30)
    square_j.center = (710, 300)

    square_i = pygame.Rect(0, 0, 30, 30)
    square_i.center = (780, 260)
    square_k = pygame.Rect(0, 0, 30, 30)
    square_k.center = (780, 300)

    square_o = pygame.Rect(0, 0, 30, 30)
    square_o.center = (870, 250)
    square_p = pygame.Rect(0, 0, 30, 30)
    square_p.center = (920, 250)

    square_n = pygame.Rect(0, 0, 30, 30)
    square_n.center = (870, 310)
    square_m = pygame.Rect(0, 0, 30, 30)
    square_m.center = (920, 310)


    if key_list[4] == 1 and key_list[5] == 0:
        pygame.draw.rect(screen, green, square_u)
        pygame.draw.rect(screen, black, square_j)
    elif key_list[4] == 0 and key_list[5] == 1:
        pygame.draw.rect(screen, black, square_u)
        pygame.draw.rect(screen, green, square_j)
    else:
        pygame.draw.rect(screen, black, square_u)
        pygame.draw.rect(screen, black, square_j)

    if key_list[6] == 1 and key_list[7] == 0:
        pygame.draw.rect(screen, green, square_i)
        pygame.draw.rect(screen, black, square_k)
    elif key_list[6] == 0 and key_list[7] == 1:
        pygame.draw.rect(screen, black, square_i)
        pygame.draw.rect(screen, green, square_k)
    else:
        pygame.draw.rect(screen, black, square_i)
        pygame.draw.rect(screen, black, square_k)

    if key_list[8] == 1 and key_list[9] == 0:
        pygame.draw.rect(screen, green, square_o)
        pygame.draw.rect(screen, black, square_p)
    elif key_list[8] == 0 and key_list[9] == 1:
        pygame.draw.rect(screen, black, square_o)
        pygame.draw.rect(screen, green, square_p)
    else:
        pygame.draw.rect(screen, black, square_o)
        pygame.draw.rect(screen, black, square_p)

    if key_list[10] == 1 and key_list[11] == 0:
        pygame.draw.rect(screen, green, square_n)
        pygame.draw.rect(screen, black, square_m)
    elif key_list[10] == 0 and key_list[11] == 1:
        pygame.draw.rect(screen, black, square_n)
        pygame.draw.rect(screen, green, square_m)
    else:
        pygame.draw.rect(screen, black, square_n)
        pygame.draw.rect(screen, black, square_m)

    # Blit arm picture
    arm = pygame.image.load('arm.jpg')
    screen.blit(arm, [695,400])

    white = (255, 255, 255)
    font = pygame.font.Font('freesansbold.ttf', 30)

    button_u = font.render('u', True, white)
    U_Rect = button_u.get_rect()
    U_Rect.center = (710, 260)
    screen.blit(button_u, U_Rect)

    button_j = font.render('j', True, white)
    J_Rect = button_j.get_rect()
    J_Rect.center = (710, 300)
    screen.blit(button_j, J_Rect)

    button_i = font.render('i', True, white)
    I_Rect = button_i.get_rect()
    I_Rect.center = (780, 260)
    screen.blit(button_i, I_Rect)

    button_j = font.render('k', True, white)
    J_Rect = button_j.get_rect()
    J_Rect.center = (780, 300)
    screen.blit(button_j, J_Rect)

    button_o = font.render('o', True, white)
    O_Rect = button_o.get_rect()
    O_Rect.center = (870, 250)
    screen.blit(button_o, O_Rect)

    button_p = font.render('p', True, white)
    P_Rect = button_p.get_rect()
    P_Rect.center = (920, 250)
    screen.blit(button_p, P_Rect)

    button_n= font.render('n', True, white)
    N_Rect = button_n.get_rect()
    N_Rect.center = (870, 310)
    screen.blit(button_n, N_Rect)

    button_m = font.render('m', True, white)
    M_Rect = button_m.get_rect()
    M_Rect.center = (920, 310)
    screen.blit(button_m, M_Rect)

def blit_camera_buttons():
    black = (0, 0, 0)
    green = (0, 255, 0)
    square_c = pygame.Rect(0, 0, 30, 30)
    square_c.center = (290, 550)
    square_v = pygame.Rect(0, 0, 30, 30)
    square_v.center = (350, 550)

    if key_list[12] == 1:
        pygame.draw.rect(screen, green, square_c)
        pygame.draw.rect(screen, black, square_v)
    elif key_list[13] == 1:
        pygame.draw.rect(screen, black, square_c)
        pygame.draw.rect(screen, green, square_v)
    else:
        pygame.draw.rect(screen, black, square_c)
        pygame.draw.rect(screen, black, square_v)


    white = (255, 255, 255)
    font = pygame.font.Font('freesansbold.ttf', 30)

    button_c = font.render('c', True, white)
    C_Rect = button_c.get_rect()
    C_Rect.center = (290, 550)
    button_v = font.render('v', True, white)
    V_Rect = button_v.get_rect()
    V_Rect.center = (350, 550)

    screen.blit(button_c,C_Rect)
    screen.blit(button_v,V_Rect)




speed =[0]
def blit_movment_speed(speed):

    if key_list[0] == 1 or key_list[0] == 1 or key_list[2] == 1 or key_list[3] == 1:
        try:
            old_speed = [0]
            with open('speed.txt', 'r') as speed_wheel:
                lines = json.load(speed_wheel)
                speed_new = lines["speed"]
                speed = speed_new
                old_speed = speed

        except:

             print('not loaded')
             speed = old_speed
    else:
         speed = [0]


    print(speed)
    speed_value = 'Movement speed is ' + str(speed) + 'cm/s'
    white = (255, 255, 255)
    font = pygame.font.Font('freesansbold.ttf', 20)
    ##movement massage
    speed_print = font.render(speed_value, True, white)
    speed_Rect = speed_print.get_rect()
    speed_Rect.center = (810, 30)
    screen.blit(speed_print, speed_Rect)


def blit_car_buttons():
    green = (0,255,0)
    black = (0,0,0)
    square_w = pygame.Rect(0, 0, 30, 30)
    square_w.center = (810,80)
    square_s = pygame.Rect(0, 0, 30, 30)
    square_s.center = (810, 120)
    square_a = pygame.Rect(0, 0, 30, 30)
    square_a.center = (760, 120)
    square_d = pygame.Rect(0, 0, 30, 30)
    square_d.center = (860, 120)


    if key_list[0] and key_list [2]:
        pygame.draw.rect(screen, green, square_w)
        pygame.draw.rect(screen, black, square_s)
        pygame.draw.rect(screen, green, square_a)
        pygame.draw.rect(screen, black, square_d)
    elif key_list[0] and key_list[3]:
        pygame.draw.rect(screen, green, square_w)
        pygame.draw.rect(screen, black, square_s)
        pygame.draw.rect(screen, black, square_a)
        pygame.draw.rect(screen, green, square_d)
    elif key_list[1] and key_list[2]:
        pygame.draw.rect(screen, black, square_w)
        pygame.draw.rect(screen, green, square_s)
        pygame.draw.rect(screen, green, square_a)
        pygame.draw.rect(screen, black, square_d)
    elif key_list[1] and key_list[3]:
        pygame.draw.rect(screen, black, square_w)
        pygame.draw.rect(screen, green, square_s)
        pygame.draw.rect(screen, black, square_a)
        pygame.draw.rect(screen, green, square_d)
    elif key_list[0] == 1:
        pygame.draw.rect(screen, green, square_w)
        pygame.draw.rect(screen,black, square_s)
        pygame.draw.rect(screen, black, square_a)
        pygame.draw.rect(screen, black, square_d)
    elif key_list[1] == 1:
        pygame.draw.rect(screen, black, square_w)
        pygame.draw.rect(screen, green, square_s)
        pygame.draw.rect(screen, black, square_a)
        pygame.draw.rect(screen, black, square_d)
    elif key_list[2] == 1:
        pygame.draw.rect(screen, black, square_w)
        pygame.draw.rect(screen, black, square_s)
        pygame.draw.rect(screen, green, square_a)
        pygame.draw.rect(screen, black, square_d)
    elif key_list[3] == 1:
        pygame.draw.rect(screen, black, square_w)
        pygame.draw.rect(screen, black, square_s)
        pygame.draw.rect(screen, black, square_a)
        pygame.draw.rect(screen, green, square_d)

    else:
        pygame.draw.rect(screen, black, square_w)
        pygame.draw.rect(screen, black, square_s)
        pygame.draw.rect(screen, black, square_a)
        pygame.draw.rect(screen, black, square_d)




    white = (255, 255, 255)
    font = pygame.font.Font('freesansbold.ttf', 30)

    button_w = font.render('w', True, white)
    W_Rect = button_w.get_rect()
    W_Rect.center = (810, 80)
    button_s = font.render('s', True, white)
    S_Rect = button_s.get_rect()
    S_Rect.center = (810, 120)
    button_a = font.render('a', True, white)
    A_Rect = button_s.get_rect()
    A_Rect.center = (760, 120)
    button_d = font.render('d', True, white)
    D_Rect = button_d.get_rect()
    D_Rect.center = (860, 120)
    screen.blit(button_w, W_Rect)
    screen.blit(button_s, S_Rect)
    screen.blit(button_a, A_Rect)
    screen.blit(button_d, D_Rect)


def controls_info():
    white = (255, 255, 255)
    font = pygame.font.Font('freesansbold.ttf', 10)
    camera_controls = font.render("Press <c> to move camera left | Press <v> to move camera right", True, white)
    camera_control_Rect = camera_controls.get_rect()
    camera_control_Rect.center = (325, 500)
    screen.blit(camera_controls, camera_control_Rect)

    car_controls_w_s = font.render("Hold <w> to move car forward | Hold <s> to move car backward", True, white)
    car_controls_w_s_Rect = car_controls_w_s.get_rect()
    car_controls_w_s_Rect.center = (810, 180)
    car_controls_a_d = font.render("Hold <a> to move car left | Hold <d> to move car right" , True, white)
    car_controls_a_d_Rect = car_controls_a_d.get_rect()
    car_controls_a_d_Rect.center = (810, 190)
    screen.blit(car_controls_w_s, car_controls_w_s_Rect)
    screen.blit(car_controls_a_d, car_controls_a_d_Rect)


    arm_controls = font.render("Hold button shown on picture to control arm", True, white)
    arm_controls_Rect = arm_controls.get_rect()
    arm_controls_Rect = (710, 380)
    screen.blit(arm_controls,arm_controls_Rect)


def massage():
    #receving camera pw
    data_cam = s.recv(1024)
    data_cam = codecs.decode(data_cam)
    data_cam = int(data_cam)

    cam_angle = interp(data_cam, [825, 2175], [-70, 70])
    cam_angle = round(cam_angle)
    camera = 'Camera is on: ' + str(cam_angle) + ' degrees'

    white = (255, 255, 255)
    font = pygame.font.Font('freesansbold.ttf', 20)
    ##movement massage
    forward = font.render('Moving Forward!', True, white)
    forward_Rect = forward.get_rect()
    forward_Rect.center = (810, 160)
    backward = font.render('Moving Backward!', True, white)
    backward_Rect = backward.get_rect()
    backward_Rect.center = (810, 160)
    left = font.render('Moving Left!', True, white)
    left_Rect = left.get_rect()
    left_Rect.center = (810, 160)
    right = font.render('Moving Right!', True, white)
    right_Rect = right.get_rect()
    right_Rect.center = (810, 160)
    forward_left = font.render('Moving Forward Left!', True, white)
    forward_left_Rect = forward_left.get_rect()
    forward_left_Rect.center = (810, 160)
    forward_right = font.render('Moving Forward Right!', True, white)
    forward_right_Rect = forward_right.get_rect()
    forward_right_Rect.center = (810, 160)
    backward_left = font.render('Moving Backward Left!', True, white)
    backward_left_Rect =backward_left.get_rect()
    backward_left_Rect.center = (810, 160)
    backward_right = font.render('Moving Backward Right!', True, white)
    backward_right_Rect = backward_right.get_rect()
    backward_right_Rect.center = (810, 160)
    stop = font.render('       Car Is Stopped!', True, white)
    stop_Rect = backward_right.get_rect()
    stop_Rect.center = (810, 160)


    # camera rotation massage
    left_cam = font.render('Camera rotating to left!', True, white)
    left_cam_Rect = left_cam.get_rect()
    left_cam_Rect.center = (320, 590)
    right_cam = font.render('Camera rotating to right!', True, white)
    right_cam_Rect = right_cam.get_rect()
    right_cam_Rect.center = (320, 590)
    stop_cam = font.render(camera, True, white)
    stop_cam_Rect = stop_cam.get_rect()
    stop_cam_Rect.center = (320, 590)

    #arm moving massage
    moving_arm = font.render('Arm Is Moving!', True, white)
    moving_arm_Rect = moving_arm.get_rect()
    moving_arm_Rect.center = (810, 350)
    stop_arm = font.render('Arm Is Stopped!', True, white)
    stop_arm_Rect= stop_arm.get_rect()
    stop_arm_Rect.center = (810, 350)

    if key_list[0] and key_list [2]:
        screen.blit(forward_left, forward_left_Rect)
    elif key_list[0] and key_list[3]:
        screen.blit(forward_right,forward_right_Rect)
    elif key_list[1] and key_list[2]:
        screen.blit(backward_left,backward_left_Rect)
    elif key_list[1] and key_list[3]:
        screen.blit(backward_right,backward_right_Rect)
    elif key_list[0] == 1:
        screen.blit(forward,forward_Rect)
    elif key_list[1] == 1:
        screen.blit(backward,backward_Rect)
    elif key_list[2] == 1:
        screen.blit(left,left_Rect)
    elif key_list[3] == 1:
        screen.blit(right, right_Rect)
    else:
        screen.blit(stop,stop_Rect)

    if key_list[12] == 1:
        screen.blit(left_cam, left_cam_Rect)
    elif key_list[13] == 1:
        screen.blit(right_cam, right_cam_Rect)
    else:
        screen.blit(stop_cam, stop_cam_Rect)

    if key_list[4] == 1:
        screen.blit(moving_arm, moving_arm_Rect)
    elif key_list[5] == 1:
        screen.blit(moving_arm, moving_arm_Rect)
    elif key_list[6] == 1:
        screen.blit(moving_arm, moving_arm_Rect)
    elif key_list[7] == 1:
        screen.blit(moving_arm, moving_arm_Rect)
    elif key_list[8] == 1:
        screen.blit(moving_arm, moving_arm_Rect)
    elif key_list[9] == 1:
        screen.blit(moving_arm, moving_arm_Rect)
    elif key_list[10] == 1:
        screen.blit(moving_arm, moving_arm_Rect)
    elif key_list[11] == 1:
        screen.blit(moving_arm, moving_arm_Rect)
    else:
        screen.blit(stop_arm, stop_arm_Rect)


def send_key_list():
    new_list = str(key_list)
    new_key = []
    for k in new_list:
        if k == '[' or k == ',' or k == ']':
            pass
        else:
            new_key.append(k)
    new = ''
    for x in new_key:
        new = new + x
    keys = codecs.encode(new)
    s.send(keys)




draw_green_line = []
draw_red_line = []
while True:
    list_data = sensor_data(first)
    distance = list_data[1]
    new_data = list_data[0]
    check_buttons()
    send_key_list()
    if key_list[14] == 0:
        blit_sonar(new_data, distance)
    blit_camera()
    massage()
    controls_info()
    blit_camera_buttons()
    blit_movment_speed(speed)
    blit_car_buttons()
    blit_arm_buttons()
    if key_list[14] == 1:
        blit_sonar(new_data, distance)

    first = False
    pygame.display.flip()





