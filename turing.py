from turing_hw import Turing_machine
import uitest.py

initial_state = "init"
final_states = {"final"}

t = Turing_machine( 
                  initial_state = "init",
                  final_states = final_states,
                  configurations=transition_function,tape=text)


#print t.final_states
while t.state not in t.final_states:
    t.step()
