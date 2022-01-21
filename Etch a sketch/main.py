from turtle import Turtle, Screen

coco = Turtle()
screen = Screen()


def move_forward():
    coco.forward(10)

def move_backward():
    coco.backward(10)

def turn_left():
    new_h = coco.heading() + 10
    coco.setheading(new_h)
def turn_right():
    new_h = coco.heading() - 10
    coco.setheading(new_h)

def clear_screen():
    coco.speed("fastest")
    coco.clear()
    coco.penup()
    coco.home()
    coco.setheading(0)
    coco.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
