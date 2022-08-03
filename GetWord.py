from pickle import NONE
import pygame as py
from Start import Page
# from GoTo3 import Page3
from pygame.locals import *
import sys
#referencing parameters from the Start file
height = Page().height
width = Page().width
screen = Page().screen
py.init()
class Page2:
    def __init__(self):
        self.running = True
        self.font_header = py.font.Font(None, 100)
        self.font_input_word = py.font.Font(None, 40)
        self.bg = py.image.load('getText.jpg')
        self.submit_button = py.transform.scale(py.image.load('submit.jpg'),(120,100))
        self.HeaderText_surf = self.font_header.render(("Guessed Word"),1,'WHITE')
        self.input_text=""

    def mainGetWord(self):
        while self.running:
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.running = False
                    py.quit()
                    sys.exit()
                elif event.type == py.KEYDOWN:
                    if event.key == py.K_RETURN:
                        file = open("text.txt", "w") 
                        file.write(self.input_text)
                        file.close()
                        self.running = False
                    if event.key == py.K_BACKSPACE:
                        self.input_text =  self.input_text[:-1]
                    else:
                        self.input_text += event.unicode
                if event.type == py.MOUSEBUTTONDOWN:
                    mx,my = py.mouse.get_pos() 
                    print (mx , my)
                    if mx>=210 and mx<=370 and my>=325 and my <=450 or py.K_RETURN:
                        file = open("text.txt", "w") 
                        file.write(self.input_text)
                        file.close()
                        py.display.update()
                        self.running = False
        
                screen.blit(self.bg, (0,0))
                text_surf = self.font_input_word.render(self.input_text, True, "white")
                text_rect = text_surf.get_rect(center=(width/2, height/2))
                screen.blit(text_surf, text_rect)
                HeaderText_rect = self.HeaderText_surf.get_rect(center=(width/2, height/2-120))
                screen.blit(self.HeaderText_surf , HeaderText_rect)
                submit_rect = self.submit_button.get_rect(center=(width/2, height/2+170))
                screen.blit(self.HeaderText_surf , HeaderText_rect)
                screen.blit(self.submit_button , submit_rect)
                py.display.update()