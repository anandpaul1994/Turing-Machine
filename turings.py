class Turing_machine(object):
	def __init__(self,initial_state,final_states,configurations,tape=''):
		self.initial=initial_state
		self.final_states=final_states
		self.state=self.initial
		self.config=configurations
		self.tape={}
		for i in range(len(tape)):
			self.tape[i]=tape[i]
		self.tape[i+1]=' '
		#print "test",self.tape
		self.position=0
	def step(self):
		tape_value=self.tape[self.position]
		x=(self.state,tape_value)
		y=self.config[x]
		print "state:",self.state
		self.state=y[0]
		self.tape[self.position]=y[1]
		if y[2]=='R':
			self.position+=1
		elif y[2]=='L':
			self.position-=1



