import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(730, 500)
screen.title("Name the States")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 State's Correct",
                                    prompt="What's the another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        states_data = data[data.state == answer_state]
        t.goto(int(states_data.x), int(states_data.y))
        t.write(answer_state)
