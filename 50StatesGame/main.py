import turtle as t
import pandas as pd

ALIGNMENT = "center"
TEXTFONT = ("Courier", 8, "normal")
GAMEOVERTEXT = "YOU GOT ALL 50, YOU WIN!"
G_OVERFONT = ("Courier", 45, "normal")

# Setup Screen
screen = t.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
t.shape(image)

# Read csv file with states and text positions and make into list.
data = pd.read_csv('50_states.csv')
all_states = data.state.to_list()

lower_states = [] # List to hold lowercase state names with no spaces
guessed_states = [] # List to hold states you have guessed

# Make all_states list lowercase  names with no spaces
for i in all_states:
    lower_states.append(i.replace(" ", "").lower())

# Make lists for x/y coords from the csv file.
x_cord = data.x.to_list()
y_cord = data.y.to_list()

def write_state(state, x, y, si):
    ''' Writes the name of the state on top of the map location, 
    then removes the state from the regular and lower cased lists, and removes the x/y coords from their list as well. This will give us a list at the end of only the states that weren't guessed that you need to work on.'''
    text = t.Turtle()
    text.hideturtle()
    text.penup()
    text.color("red")
    text.speed("fastest")
    text.clear()
    text.goto(x, y)
    text.write(f"{state}", align=ALIGNMENT, font=TEXTFONT)
    screen.title(f"U.S. States Game - Score: {len(guessed_states)}/50")
    # these pops remove correct answers keep the indexes in sync between these lists, so that I have a final list of all_states with only the ones not guessed in it.
    lower_states.pop(si)
    all_states.pop(si)
    y_cord.pop(si)
    x_cord.pop(si)
    

 # Keep doing this until you have guessed all 50 or typed 'exit'
while len(guessed_states) < 50:
    
    answer_state = screen.textinput(title='Guess the state', prompt='Name another state! - or "exit"')
    # Take the answer and make it lower case as well as remove spaces, for comparison.
    answer_state = answer_state.lower().replace(" ", "")
    # print(answer_state)

    # Check for exit cue.  If exiting, take all the states left in the all_states list that we haven't guessed, and output them to a csv file for study.
    if answer_state == "exit":
        statedf = pd.DataFrame(all_states)
        statedf.to_csv('unguessed.csv', header=False, index=False)
        t.bye()

    if answer_state in lower_states:
        # Add your guess to guessed_states list for tracking
        guessed_states.append(answer_state)

        # Get the state's and x/y list index for your answer.
        state_index = lower_states.index(answer_state)
        x_index_item = x_cord[state_index]
        y_index_item = y_cord[state_index]
        # Draw the state name over the state and othe magic.
        write_state(all_states[state_index], x_index_item, y_index_item, state_index)
        # Debug print statements.
        # print("-----------")
        # print(all_states)
        # print("-----------")
        # print(lower_states)
        # print("-----------")
        # print(f"{answer_state}, {x_index_item}, {y_index_item}")

# If all states were guessed, print congrats message!
text = t.Turtle()
text.hideturtle()
text.penup()
text.color("red")
text.speed("fastest")
text.clear()
text.goto(0, 275)
text.write(f"{GAMEOVERTEXT}", align=ALIGNMENT, font=G_OVERFONT)

screen.exitonclick()
