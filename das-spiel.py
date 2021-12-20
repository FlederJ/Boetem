#pygame ab Version 2.0 wird benoetigt
#Installation im Terminal mit 
#   --> pip install pygame (windows) 
#   --> pip3 install pygame (mac)
#   --> sudo apt-get install python3-pygame (Linux Debian/Ubuntu/Mint)
import sys
import random
import time
import pygame as pg
from pygame.locals import *
from pygame.constants import KSCAN_D, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from pprint import pprint

pg.display.set_caption("Alhamdulabugabing")
pg.init()
pg.font.init()

#hi

done = False
width = 640
height = 640
weight = 1000
blue = 72,180,204, 50
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()
myfont = pg.font.SysFont('Sans Serif',16)
screen.fill(blue)
FPS = 40
#music = pg.music.load("smaba")

#Schiff Settings:
multi_speed = 0
speed = 0.5
multi_handling = 0
direction = 0
x_pos = 50
y_pos = 320
bewegung = 0

while not done:
    for event in pg.event.get():
        if event == pg.QUIT:
            done = True
            
pg.quit()
