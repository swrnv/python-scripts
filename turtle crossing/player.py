STARTING_POSITION = (0, -280)

FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)
        self.MOVE_DISTANCE = 10

    def go_up(self):
        self.forward(self.MOVE_DISTANCE)

    def go_down(self):
        self.backward(self.MOVE_DISTANCE)

    def is_at_finish(self):
        return self.ycor() >= FINISH_LINE_Y

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def level_speed(self):
        self.MOVE_DISTANCE += 1


