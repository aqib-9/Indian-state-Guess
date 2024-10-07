import turtle
import pandas

screen=turtle.Screen()
image='india-state.gif'
screen.addshape(image)
turtle.shape(image)



data=pandas.read_csv('states_data.csv')
state=data['state'].to_list()
answer=[]
missed_state=[]
while len(answer) < 30:
    answer_state=screen.textinput(f'Guessed {len(answer)}/30 States','Guess an Indian State').title()

    if answer_state == 'Exit':
        for i in state:
            if i not in answer:
                missed_state.append(i)
        new_data=pandas.DataFrame(missed_state)
        new_data.to_csv('missed_states.csv')
        break

    if answer_state in state:
        answer.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(state_data.state.item())





        
    



screen.exitonclick()