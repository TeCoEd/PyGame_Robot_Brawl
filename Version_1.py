#!/usr/bin/env python
###Coded by Raspberry Pi Club and @dan_aldred###
import random, pygame, sys
from pygame.locals import *
import os
import time

FPS = 15
WINDOWWIDTH = 100
WINDOWHEIGHT = 100

#UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def main():
     global FPSCLOCK, DISPLAYSURF# BASICFONT

     pygame.init()
     FPSCLOCK = pygame.time.Clock()
     DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    # BASICFONT = pygame.font.Font('freesansbold.tff', 18)
     pygame.display.set_caption('Robot Arm')

     while True:
          rungame()

#import the USB abd time libraries
import usb.core, usb.util, time

#dallocate the name 'RoboArm' to the USB device
RoboArm=usb.core.find(idVendor=0x1267,idProduct=0x0000)

#Check to see if arm is detected
if RoboArm is None:
     raise ValueError("Arm not found")

#Create a variable for duration
Duration=1

#Define a procedure to execute each movement
def MoveArm(Duration, ArmCmd):
     #start the movement
     RoboArm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,1000)
     #stop the movement atfer specified duration
     time.sleep(Duration)
     ArmCmd=(0,0,0)
     RoboArm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,1000)

#MoveArm(1,[16,0,0]) #elbow up
     
def rungame():
     #Set a random start point.
     while True:#main game loop
          for event in pygame.event.get():#event handling loop
               if event.type == QUIT:
                    terminate()

               elif event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                         print "right"
                         MoveArm(1,[0,2,0]) #rotate base clockwise

                    if event.key == K_LEFT:
                         print "left"
                         MoveArm(1,[0,1,0]) #rotate base clockwise

                    if event.key == K_UP:
                         print "UP"
                         MoveArm(1,[32,0,0]) #rotate base clock
                         
                    if event.key == K_DOWN:
                         print "down"
                         MoveArm(1,[16,0,0]) #rotate base clockwise

                    if event.key == K_c:
                         print "CLOSED"
                         MoveArm(1,[1,0,0]) #rotate base clockwise

                    if event.key == K_o:
                         print "OPEN"
                         MoveArm(1,[2,0,0]) #rotate base clockwise
                        
                        
                    if event.key == K_l:
                         print "on"
                         MoveArm(1,[0,0,1]) #rotate base clockwise
                         
                    if event.key == K_a:
                         print "shoulder up"
                         MoveArm(1,[64,0,1]) #rotate base clockwise
                         
                    if event.key == K_s:
                         print "shoulder down"
                         MoveArm(1,[128,0,1]) #rotate base clockwise

                    if event.key == K_u:
                         print "wrist up#"
                         MoveArm(1,[4,0,0]) #rotate base clockwise

                    if event.key == K_y:
                         print "wrist down"
                         MoveArm(1,[32,0,0]) #rotate base clockwise


                    if event.key == K_d:
                         print "wrist down"
                         MoveArm(1,[8,0,0]) #rotate base clockwise

                    if event.key == K_d:
                         print "wrist up"
                         MoveArm(1,[8,0,4]) #rotate base clockwise


if __name__ == "__main__":
     main()


'''#Give arm some commands
MoveArm(1,[0,1,0]) #rotate base anti-clockwise
MoveArm(1,[0,2,0]) #rotate base clockwise
MoveArm(1,[64,0,0]) #shoulder up
MoveArm(1,[128,0,0]) #shoulder down
MoveArm(1,[16,0,0]) #elbow up
MoveArm(1,[32,0,0]) #elbow down
MoveArm(1,[4,0,0]) #wrist up
MoveArm(1,[8,0,0]) #wrist down
MoveArm(1,[2,0,0]) #grip open
MoveArm(1,[1,0,0]) #grip close
MoveArm(1,[0,0,1]) #light off
MoveArm(1,[0,0,0]) #light off'''





