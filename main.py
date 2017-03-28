from time import sleep
from detect import det
from serial import Serial

ser = Serial('/dev/ttyACM0', 9600)
a1=raw_input('turing input:')
ser.flush()
for c in a1:
	if c!=' ':
		print "sending",c
		ser.write(c)
		while ser.in_waiting==0:
			x=ser.read()
			print x
			break
	print "sending",3
	ser.write('3')
	while ser.in_waiting==0:
		x=ser.read()
		print x
		break

for c in a1:
	print "sending",4
	ser.write('4')
	while ser.in_waiting==0:
		x=ser.read()
		print x
		break
	


def s0(i):
	y=det()
	print "State=",0
	print "captured",y
	if(y==' '):
		#print "sending",1
		ser.write('1')
		while ser.in_waiting==0:
			x=ser.read()
			print x
			break
		#print "sending",3
		ser.write('3')
		while ser.in_waiting==0:
			x=ser.read()
			print x		
			break
		s1(i)
	elif(y=='0'):
		#print "sending",3
		ser.write('3')
		while ser.in_waiting==0:
			x=ser.read()
			print x
		s0(i)
	else:
		#print "sending",3
		ser.write('3')
		while ser.in_waiting==0:
			x=ser.read()
			print x
			break
		s0(i)

def s1(i):
	y=det()
	print "State=",1
	print "captured",y
	if(y==' '):
		#print "sending",4
		ser.write('4')
		while ser.in_waiting==0:
			x=ser.read()
			print x		
			break
		s2(i)
	elif(y=='0'):
		#print "sending",3
		ser.write('3')
		while ser.in_waiting==0:
			x=ser.read()
			print x
			break
		s1(i)
	else:
		#print "sending",3
		ser.write('3')
		while ser.in_waiting==0:
			x=ser.read()
			print x
			break
		s1(i)

def s2(i):
	y=det()
	print "State=",2
	print "captured",y
	if(y==' '):
		#print "sending",4
		ser.write('4')	
		while ser.in_waiting==0:
			x=ser.read()
			print x	
			break
		s2(i)
	elif(y=='0'):
		#print "sending",4
		ser.write('4')
		while ser.in_waiting==0:
			x=ser.read()
			print x
			break
		s2(i)
	else:
		#print "sending"
		ser.write(' ')
		while ser.in_waiting==0:
			x=ser.read()
			print x
			break
		#print "sending",0
		ser.write('0')
		while ser.in_waiting==0:
			x=ser.read()
			print x
			break
		#print "sending",4
		ser.write('4')
		while ser.in_waiting==0:
			x=ser.read()
			print x
			break
		s3(i)

def s3(i):
	y=det()
	print "State=",3
	print "captured",y
	if(y==' '):
		#print "sending",4
		ser.write('4')
		while ser.in_waiting==0:
			x=ser.read()
			print x	
			break	
		s4(i)
	elif(y=='0'):
		#print "sending"
		ser.write(' ')
		while ser.in_waiting==0:
			x=ser.read()
			print x
			break
		#print "sending",4
		ser.write('4')
		while ser.in_waiting==0:
			x=ser.read()
			print x
			break
		s3(i)
	else:
		#print "sending",3
		ser.write('3')
		while ser.in_waiting==0:
			x=ser.read()
			print x
			break
			
		s3(i)

def s4(i):
	y=det()
	print "State=",4
	print "captured",y
	if(y==' ')	:
		ser.write('3')
		while ser.in_waiting==0:
			x=ser.read()
			print x
			break	
		return()
	elif(y=='0'):
		#print "sending",4
		ser.write('4')
		while ser.in_waiting==0:
			x=ser.read()
			print x
			break
		s4(i)
	else:
		#print "sending",4
		ser.write('4')
		while ser.in_waiting==0:
			x=ser.read()
			print x
			break
		s4(i)


s0(5)


