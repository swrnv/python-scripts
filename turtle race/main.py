from turtle import Turtle, Screen
import random

is_race_on = False

new_turtle = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Racing")
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race. Enter a color :  ")
print(user_bet)

all_turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color =turtle.pencolor()
            if winning_color == user_bet:
                print('you won')
            else:
                print(f'you lost. {winning_color} won')

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
