from serial import Serial
from detect import det

ser = Serial('/dev/ttyACM0', 9600)

class Turing_machine(object):
	#initialize turing machine parameters
	def __init__(self,initial_state,final_states,configurations,tape=''):
		self.initial=initial_state
		self.final_states=final_states
		self.state=self.initial
		self.config=configurations
		self.tape=tape
		self.position=0
		self.settape()
		print "Initialized"
	
	#function to set tape to initial value
	def settape(self):
		print "set tape"
		for c in self.tape:
			if c!=' ':
				print "sending",c
				ser.write(c)
				self.waitack()
			print "sending",3
			ser.write('3')
			self.waitack()
		for c in self.tape:
			print "sending",4
			ser.write('4')
			self.waitack()
	
	#function to wait for serial acknowledge signal once task is done.		
	def waitack(self):
		while ser.in_waiting==0:
				x=ser.read()
				print "acknowledged:",x
				return
	
	#function for performing transition steps				
	def step(self):
		print "state:",self.state
		tape_value=det()
		print "read value:",tape_value
		x=(self.state,tape_value)
		y=self.config[x]
		self.state=y[0]
		'''if	(tape_value!=y[1]) and (tape_value!=' '):
			print "sending",2
			ser.write('2')
			self.waitack()
		if y[1]!=' ':
			print "sending",y[1]
			ser.write(y[1])
			self.waitack()'''
		
		if y[1]!=tape_value:
			if tape_value!=' ':
				print "sending",2
				ser.write('2')
				self.waitack()
			print "sending",y[1]
			ser.write(y[1])
			self.waitack()
		if y[2]=='R':
			self.position+=1
			print "sending",3
			ser.write('3')
			self.waitack()
			
		elif y[2]=='L':
			self.position-=1
			print "sending",4
			ser.write('4')
			self.waitack()



