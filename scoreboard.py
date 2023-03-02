from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = self.load_data()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=270)
        self.update_scoreboard()

    def load_data(self):
        with open('data.txt', 'r') as data:
            data = int(data.read())
            return data

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.highest_score}", align="center", font=("Courier", 24, "normal"))

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open('data.txt', 'w') as data:
                data.write(str(self.highest_score))
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

