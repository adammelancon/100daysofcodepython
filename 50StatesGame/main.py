import turtle as t
import pandas as pd

ALIGNMENT = "center"
TEXTFONT = ("Courier", 8, "normal")
GAMEOVERTEXT = "YOU GOT ALL 50, YOU WIN!"
G_OVERFONT = ("Courier", 45, "normal")

screen = t.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)

data = pd.read_csv('50_states.csv')

all_states = data.state.to_list()
lower_states = []
guessed_states = []

for i in all_states:
    lower_states.append(i.replace(" ", "").lower())

x_cord = data.x.to_list()
y_cord = data.y.to_list()

def write_state(state, x, y, si):
    text = t.Turtle()
    text.hideturtle()
    text.penup()
    text.color("red")
    text.speed("fastest")
    text.clear()
    text.goto(x, y)
    text.write(f"{state}", align=ALIGNMENT, font=TEXTFONT)
    screen.title(f"U.S. States Game - Score: {len(guessed_states)}/50")
    lower_states.pop(si)
    all_states.pop(si)
    y_cord.pop(si)
    x_cord.pop(si)
    
t.shape(image)


while len(guessed_states) < 50:
    
    answer_state = screen.textinput(title='Guess the state', prompt='Name another state! - or "exit"')
    answer_state = answer_state.lower().replace(" ", "")
    # print(answer_state)
    if answer_state == "exit":
        statedf = pd.DataFrame(all_states)
        statedf.to_csv('unguessed.csv', header=False, index=False)
        t.bye()

    if answer_state in lower_states:

        guessed_states.append(answer_state)

        state_index = lower_states.index(answer_state)

        x_index_item = x_cord[state_index]
        y_index_item = y_cord[state_index]
        write_state(all_states[state_index], x_index_item, y_index_item, state_index)
        print("-----------")
        print(all_states)
        print("-----------")
        print(lower_states)
        print("-----------")
        print(f"{answer_state}, {x_index_item}, {y_index_item}")

text = t.Turtle()
text.hideturtle()
text.penup()
text.color("red")
text.speed("fastest")
text.clear()
text.goto(0, 275)
text.write(f"{GAMEOVERTEXT}", align=ALIGNMENT, font=G_OVERFONT)



screen.exitonclick()
