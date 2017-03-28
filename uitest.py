import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *
from time import sleep
from turings import Turing_machine

text=" "
transition_function={}
flag=0
# create our window
app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('Turing Machine')
 
# Create textbox
textbox = QLineEdit(w)
textbox.move(20, 20)
textbox.resize(280,40)

textbox1 = QLineEdit(w)
textbox1.move(20, 300)
textbox1.resize(280,40)
 
# Set window size.
w.resize(320, 400)
 
# Create a button in the window
add_button = QPushButton('    Addition    ', w)
add_button.move(20,80)

# Create a button in the window
sub_button = QPushButton(' Subtraction ', w)
sub_button.move(20,120)

# Create a button in the window
com_button = QPushButton('Complement', w)
com_button.move(20,160) 

# Create a button in the window
play_button = QPushButton('Play', w)
play_button.move(210,80)

# Create a button in the window
pause_button = QPushButton('Pause', w)
pause_button.move(210,120)

# Create a button in the window
stop_button = QPushButton('Stop', w)
stop_button.move(210,160)

# Create the actions
@pyqtSlot()
def addition():
	transition_function = {("init","0"):("init", "0", "R"),
                       ("init","1"):("init", "1", "R"),
                       ("init"," "):("s1","1", "R"),
                       
                       ("s1","0"):("s1", "0", "R"),
                       ("s1","1"):("s1", "1", "R"),
                       ("s1"," "):("s2"," ", "L"),
                       
                       ("s2","0"):("s2", "0", "L"),
                       ("s2","1"):("s3", "0", "L"),
                       ("s2"," "):("s2"," ", "L"),
                       
                       ("s3","0"):("s3", " ", "L"),
                       ("s3","1"):("s3", "1", "R"),
                       ("s3"," "):("final"," ", "R"),

                       }
	final_states = {"final"}

	text = str(textbox.text())
	global t
	t = Turing_machine( 
                  initial_state = "init",
                  final_states = final_states,
                  configurations=transition_function,tape=text)
   # print text

def subtraction():
	transition_function = {("init","0"):("init", "0", "R"),
                       ("init","1"):("init", "1", "R"),
                       ("init"," "):("s1"," ", "R"),
                       
                       ("s1","0"):("s1", "0", "R"),
                       ("s1","1"):("s1", "1", "R"),
                       ("s1"," "):("s2"," ", "L"),
                       
                       ("s2","0"):("s2", "0", "L"),
                       ("s2","1"):("s3", "0", "L"),
                       ("s2"," "):("s4"," ", "R"),
                       
                       ("s3","0"):("s3", "0", "L"),
                       ("s3","1"):("s3", "1", "L"),
                       ("s3"," "):("s7"," ", "L"),

                       ("s4","0"):("s4", "0", "R"),
                       ("s4","1"):("s6", "1", "R"),
                       ("s4"," "):("s5"," ", "L"),
                       
                       ("s5","0"):("s5", " ", "L"),
                       ("s5","1"):("s5", "1", "L"),
                       ("s5"," "):("s6"," ", "L"),
                       
                       
                       ("s6","0"):("s6", " ", "L"),
                       ("s6","1"):("s6", "1", "L"),
                       ("s6"," "):("final"," ", "R"),
                       
                       ("s7","0"):("s7", "0", "L"),
                       ("s7","1"):("init", "0", "L"),
                       ("s7"," "):("final"," ", "N"),
                       }
	final_states = {"final"}

	text = str(textbox.text())
	global t
	t = Turing_machine( 
                  initial_state = "init",
                  final_states = final_states,
                  configurations=transition_function,tape=text)
    
def complement():
	transition_function = {("init","0"):("init", "1", "R"),
                       ("init","1"):("init", "0", "R"),
                       ("init"," "):("final"," ", "N"),
                       }
	final_states = {"final"}

	text = str(textbox.text())
	global t
	t = Turing_machine( 
                  initial_state = "init",
                  final_states = final_states,
                  configurations=transition_function,tape=text)
	

def play():
	play_button.setEnabled(False)
	pause_button.setEnabled(True)
	stop_button.setEnabled(True)
	textbox1.setText("Running")
	flag = 1
	while t.state not in t.final_states:
		t.step()
	a=""
	for j,i in t.tape.items():
		a+=str(i)
	textbox1.setText("Result:"+a)
	print a
	return

def pause():
	play_button.setEnabled(True)
	pause_button.setEnabled(False)
	stop_button.setEnabled(True)
	flag=0
	textbox1.setText("Paused")
	play_button.setCheckable(True)
	if play_button.isChecked()==False:
		#print flag+3
		sleep(1)
		#pause()
	#while(play_button.isChecked()==False):
	#	print flag
	else:
		flag=1
		#print flag
		play_button.setCheckable(False)
		return
	#return()

def stop():
	play_button.setEnabled(True)
	pause_button.setEnabled(False)
	stop_button.setEnabled(False)
	flag=0
	#print flag
	textbox1.setText("Stopped")
	textbox.setText("")
	text = ""
	transition_function = {}
	return
	

# connect the signals to the slots
add_button.clicked.connect(addition)
sub_button.clicked.connect(subtraction)
com_button.clicked.connect(complement)
play_button.clicked.connect(play)
pause_button.clicked.connect(pause)
stop_button.clicked.connect(stop)
 
# Show the window and run the app
w.show()
app.exec_()
