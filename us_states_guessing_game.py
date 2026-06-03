import pandas as pd
import turtle

states_data = pd.read_csv('50_states.csv')
states_list = states_data.state.to_list()
unguessed_list = states_list
states_xy_list = []
states_dict = {}

for i in range(0,len(states_list)):
    new_xy= [states_data.x.to_list()[i], states_data.y.to_list()[i]]
    states_xy_list.append(new_xy)

for i in range(len(states_list)):
    states_dict[states_list[i]] = states_xy_list[i]

screen = turtle.Screen()
screen.title('U.S. State Game')
image = "blank_states_img.gif"
screen.addshape(image)
height = screen.window_height()
width = screen.window_width()
image = turtle.shape(image)

state = turtle.Turtle()
state.penup()
state.hideturtle()

score = turtle.Turtle()
score.penup()
score.hideturtle()

total_states = len(states_dict)
num_state_guessed = 0

def score_update(total, num_guessed):
    score.clear()
    score.setpos(0,height/2 - 40)
    score.write(f"Score:{num_guessed}/{total_states}", align="center", font=("Courier", 24, "bold"))


def final_message():
    score.setpos(0,height/2 - 80)
    score.write(f"Congratulations! You won the game. Click to exit", align="center", font=("Courier", 24, "bold"))


def exit_message():
    score.setpos(0, height / 2 - 80)
    score.write(f"You lose. You've quit the Game. Check the list of unguessed in the csv file"
                f" 'unguessed_states.csv'",
                align="center", font=("Courier", 11, "bold"))

while num_state_guessed <50:
    score_update(total_states, num_state_guessed)
    user_guess= screen.textinput(title="Can you guess all the U.S states?", prompt="Please guess a state").title()
    if user_guess == "Exit":
        exit_message()
        break
    if user_guess in states_list:
        idx = states_list.index(user_guess)
        unguessed_list.pop(idx)
        states_xy = states_dict[user_guess]
        state.setposition(states_xy)
        state.write(user_guess)
        num_state_guessed += 1
score_update(total_states, num_state_guessed)

if num_state_guessed == total_states:
    final_message()
else:
    exit_message()

pd.DataFrame(unguessed_list).to_csv('unguessed_states.csv')

screen.exitonclick()
