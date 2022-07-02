import turtle
import pandas as pd

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = pd.read_csv("50_states.csv")
states_count = len(states)
states_list = states.state.to_list()
guessed_states = []


def get_input_string():
    return f"{len(guessed_states)}/{states_count} States Correct"


while len(guessed_states) < states_count:
    answer_state = screen.textinput(title=get_input_string(), prompt="What's another state's name?").title()
    if answer_state.lower() == "exit":
        data_dic = {
            "state": [state for state in states_list if state not in guessed_states]
        }
        data = pd.DataFrame(data_dic)
        data.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list:
        guessed_states.append(answer_state)
        write_turtle = turtle.Turtle()
        write_turtle.hideturtle()
        write_turtle.penup()
        state_data = states[states["state"] == answer_state]
        write_turtle.goto(int(state_data.x), int(state_data.y))
        write_turtle.write(answer_state)
