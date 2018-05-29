class Player:
	def __init__(self, location):
		self.location = location
		
	def move(self, exit):
		self.location = exit.location
