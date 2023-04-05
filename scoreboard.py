from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.current_score = 0
        self.write(arg=f"score: {self.current_score} high score: {self.high_score}", align="center", font=("", 15, ""))

    def game_over(self):
        self.goto(0, 20)
        self.write(arg="GAME OVER\nPress 'r' to play again", align="center", font=("", 15, ""))

    def reset(self):
        if self.high_score < self.current_score:
            self.high_score = self.current_score
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
        self.current_score = 0
        self.goto(0, 270)
        self.clear()
        self.write(arg=f"score: {self.current_score} high score: {self.high_score}", align="center", font=("", 15, ""))

    def update_score(self):
        self.clear()
        self.current_score += 1
        self.write(arg=f"score: {self.current_score} high score: {self.high_score}", align="center", font=("", 15, ""))

