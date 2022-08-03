import pygame as py
from Start import Page
from pygame.locals import *
import time
f=open("text.txt", "r")
newText = f.read()
py.init()
size = len(newText)
height = Page().height
width = Page().width
screen = Page().screen
display = ""

for i in range(size):
    display+="_"

class Game:
    def __init__(self):
        self.display = display
        self.spaceDisplay=""
        self.exit = py.transform.scale(py.image.load('exit.png'),(50,50))  
        self.font = py.font.Font(None, 40)
        
    def result(self,word,flag):
        if flag == True:
            state = "Congrats! "
        else: 
            state = "You Lost! "
        while True:
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.running = False
                    py.quit()
                if event.type == py.MOUSEBUTTONDOWN:
                        mx,my = py.mouse.get_pos() 
                        print(mx,my)
                        if mx>=270 and mx<=310 and my>=400 and my<= 430:
                            self.running = False
                            py.exit()
            screen.fill("black")
            screen.blit(self.exit,(270,400))
            state_surf = self.font.render(state, True, "white")
            word_surf = self.font.render("The Word was "+ word , True, "white")
            screen.blit(state_surf , state_surf.get_rect(center=(width/2 , height/2-50)))
            screen.blit(word_surf , word_surf.get_rect(center=(width/2 , height/2+20)))
            py.display.update()
        
    def draw(self,letter, flag):
        if flag == True:
            found = self.text.index(letter)
            for i in range(len(self.text)):
                if found == i:
                    self.display = self.display[:i] + letter + self.display[i + 1:]
                    self.spaceDisplay = " ".join(self.display)
        else:
            self.spaceDisplay = " ".join(self.display)           
        display_surf = self.font.render(self.spaceDisplay, True,"white")
        screen.blit(display_surf ,(width/2-120 , height/2-60))
        py.display.update()
        
class Timer:
    def __init__(self):
        self.timer_font = py.font.SysFont(None, 50, False, False)
        self.mins = 2 
        self.secs = 60
        self.font = py.font.Font(None, 40)
        
    def countdown(self,t):
        if t != 0:
            self.mins, self.secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(self.mins, self.secs)
            time.sleep(1)
            timer = str(timer)
            time_surf = self.font.render(timer, True, "red")
            screen.blit(time_surf, (40,20))
            py.display.flip()
        else:
            return False
            
class Page3:
    def __init__(self):
        self.text = newText
        self.font = py.font.Font(None, 40)
        self.entered_font = py.font.SysFont('yugothicuilight', 30)
        self.running = True
        self.input_letter=""
        self.count = 6
        self.word = ""
        self.guessed = ""
        self.t = 120
        
    def mainPlay(self):
        while self.running:
            if Timer().countdown(self.t)==False:
                self.running = False
                py.quit()
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.running = False
                    py.quit()
                elif event.type == py.KEYDOWN:
                    if event.key == py.K_RETURN:
                        if self.input_letter in self.word:
                                entered_surf = self.entered_font.render("*letter already pressed*", True,"white")
                                screen.blit(entered_surf , entered_surf.get_rect(center=(width/2, height/2+170)))
                                py.display.update()
                        else:
                            self.word += self.input_letter
                            if self.input_letter in self.text:
                                Game().draw(self.input_letter, True)
                                self.guessed+= self.input_letter
                                if len(self.guessed) == len(self.text):
                                    Game().result(self.text,True)
                            else:
                                    self.count -= 1
                    else:
                        self.input_letter = event.unicode
                        if self.count == 0:
                            Game().result(self.text,False)
            self.bg = py.image.load('hangman'+str(self.count)+'.jpg')
            screen.blit(self.bg, (220,55))
            self.t-=1
            Timer().countdown(self.t)
            input_surf = self.font.render(self.input_letter, True, "white")
            screen.blit(input_surf, (width/2,height/2+120))
            Game().draw(self.input_letter,False)