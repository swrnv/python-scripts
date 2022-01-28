import turtle
import pandas


screen = turtle.Screen()
screen.title("India States Game")

screen.screensize(canvwidth= 900, canvheight=1200)

image = "India_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("data.csv")
all_states = data.State.to_list()

guessed_states = []

while len(guessed_states) < 29:
    answer_state = screen.textinput(title=f"Guess. {len(guessed_states)}/29 done", prompt="Enter the state you remember. Enter 'Exit' if you forgot").title()


    if answer_state == "Exit":
        missing_states = []
        for states in all_states:
            if states not in guessed_states:
                missing_states.append(states)
        print("The states you need to learn are : \n")
        print(missing_states)
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.State == answer_state]
        t.goto(int(state_data.X), int(state_data.Y))
        t.write(answer_state)
