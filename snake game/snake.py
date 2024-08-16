from turtle import *

POSITIONS = [(-20, 0), (-40, 0), (-60, 0)]

DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()

    def create_snake(self):
        for square in POSITIONS:
            self.add(square)

    def move(self):
        body = self.body
        for part in range(len(body) - 1, 0, -1):
            # last body part go too 2nd to last part position and so on until get to first part
            body[part].goto(body[part - 1].xcor(), body[part - 1].ycor())
        self.body[0].forward(DIST)

    def up(self):
        body = self.body
        if body[0].heading() != DOWN:
            body[0].setheading(UP)

    def down(self):
        body = self.body
        if body[0].heading() != UP:
            body[0].setheading(DOWN)

    def left(self):
        body = self.body
        if body[0].heading() != RIGHT:
            body[0].setheading(LEFT)

    def right(self):
        body = self.body
        if body[0].heading() != LEFT:
            body[0].setheading(RIGHT)

    def loopx(self):
        body = self.body
        if body[0].xcor() < -1:
            body[0].setx(300)
        elif body[0].xcor() > 1:
            body[0].setx(-300)

    def loopy(self):
        body = self.body
        if body[0].ycor() < 0:
            body[0].sety(300)
        elif body[0].ycor() > 0:
            body[0].sety(-300)

    def add(self, pos):
        t = Turtle('square')
        t.penup()
        t.color('green')  # create 3 20X20 square turtle objects & line them up. Add to list for movements
        t.goto(pos)
        self.body.append(t)

    def grow(self):
        self.add(self.body[-1].position())

    def reset(self):
        for part in self.body:
            part.goto(1000, 1000)       # makes the snake not visible to the player
        self.body.clear()               # clear out all the turtles in body array
        self.create_snake()
