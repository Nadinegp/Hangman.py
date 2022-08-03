import pygame as py
from Start import Page
from GetWord import Page2
from Play import Page3
# from trial import Page3
from pygame.locals import *
p = Page()
p1 = Page2()
p3 = Page3()

while p.running:
    p.mainIntro()
while p1.running:
    p1.mainGetWord()
while p3.running:
    p3.mainPlay()
        


