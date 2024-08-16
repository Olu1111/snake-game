from turtle import *
import random as r


class Food(Turtle):  # inheritance in python! inherits turtle class so turtle is now superclass

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # reduce size from 20px to 10px
        self.speed('fastest')
        self.goto(r.randint(-285, 285), r.randint(-285, 285))

    def move(self):
        self.speed('fastest')
        self.goto(r.randint(-285, 285), r.randint(-285, 285))

