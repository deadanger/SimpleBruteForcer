import random

class Bruteforce:
		
	def __init__(self):
		self.password = 0
	
	def setPassword(self):
		self.password = str(random.randint(0,9999))
	
	def findPassword(self):
		for i in range(10000):
			trial = str(i)
			if trial == self.password:
				print('found password: {}'.format(self.password) )

agent = Bruteforce()
agent.setPassword()
agent.findPassword()