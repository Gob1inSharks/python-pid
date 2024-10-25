#import matplotlib.pyplot as plt
#import numpy as np
#import random

import pygame
import sys
import os

#import math

from vex import VexCar
from botcontroller import Controller

import utils

TIME_START = 0
TIME_STOP = 60
TIME_INCREMENTS = 0.1

INITIAL_POSITION = 0
INITIAL_VELOCITY = 0

bot = VexCar()
control = Controller(bot)

def run(totalSeconds):

    #times = np.arange(0, totalSeconds, self.TICK)

    while True:

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                sys.exit() 

        bot.scene.fill((35,35,35)) 

        bot.scene.blit(bot.assets['field'],(0,0))

        bot.drawCar(bot.SCENE_WIDTH//2 + bot.h,
                      (bot.s[0]+bot.s[1])//2,
                      100,100,(255,255,255),
                      rotation = bot.findCarAngle())
        
        bot.gyro = bot.findCarAngle()
            
        bot.drawLine()

        bot.screen.blit(pygame.transform.scale(bot.scene,(bot.SCREEN_WIDTH,bot.SCREEN_HEIGHT)), (0,0)) 

        pygame.display.update() 

        dt = bot.clock.tick(bot.FPS) * .001 

        bot.timer += dt

        if bot.timer > totalSeconds:
            pygame.quit() 
            sys.exit() 

        control.updateMotors()

        bot.advance(dt = dt)

        #print(positions) #for debugging(

if __name__ == "__main__":

    control.Kp = 3
    control.Kd = 0.012
    control.Ki = 0.0001

    run(TIME_STOP)