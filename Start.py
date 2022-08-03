import pygame as py
import sys
from pygame.locals import *

res =  (600,600)
py.init()
running = True
screen = py.display.set_mode(res)

class Page:
    def __init__(self): #variables to use later for other functions in the same class
        self.running = running
        self.screen = screen
        self.height,self.width = 600,600
        self.bg = py.image.load('starttt.jpg')
        self.start_button = py.transform.scale(py.image.load('start.png'),(100,100)).convert_alpha(self.screen)
        
    def mainIntro(self):
        while self.running:
            for ev in py.event.get():#for quitting
                if ev.type == py.QUIT:
                    py.quit()
                    self.running = False
                    sys.exit()
                if ev.type == py.MOUSEBUTTONDOWN: #when buttons are pressed or released
                    mx, my = py.mouse.get_pos() #here it works by position as its an image
                    print(mx,my)
                    if mx>=300 and mx<=460 and my>=270 and my<=340: 
                            self.running = False
            self.screen.blit(self.bg, (0,0)) #blits bg
            self.screen.blit(self.start_button , (self.width/2+20,self.height/2-50)) #blits button
            py.display.update()