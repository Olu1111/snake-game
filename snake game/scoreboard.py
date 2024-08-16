from turtle import *


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.setposition(-30, 270)
        self.color('indigo')
        self.ht()
        with open('scores.txt', mode='r') as file:
            self.highscore = int(file.read())
        self.sco = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.sco} high score: {self.highscore}", False, "center", ('Comic Sans MS', 24, 'normal'))

    def reset(self):
        if self.sco > self.highscore:
            self.highscore = self.sco
            with open('scores.txt', mode='w') as file:
                file.write(f'{self.highscore}')
        self.sco = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('Game Over', False, "center", ('Comic Sans MS', 24, 'normal'))

    def update(self):
        self.sco += 1
        self.update_scoreboard()
