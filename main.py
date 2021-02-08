import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. 50 States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_list = []
state_data = pandas.read_csv("50_states.csv")

game_over = False

while not game_over:

    state_list = state_data["state"].to_list()
    # state_x = state_data["x"].to_list()
    # state_y = state_data["y"].to_list()

    answer_state = screen.textinput(title=f"State {len(answer_list)}/50", prompt="What is the state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in answer_list:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("learn_states.csv")
        break

    if answer_state in state_list:
        answer_list.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_row = state_data.loc[state_data["state"] == answer_state]
        t.goto(int(state_row.x), int(state_row.y))
        t.write(state_row.state.item())
