
class dateTime:

	def __init__(self,concert):
		self.date = concert.date
		self.startingTime = concert.startingTime

	def convert(self):
		self.date = self.date[5:8]+self.date[8:]+self.date[4]+self.date[0:4]
		remainder = ':00 pm'
		if self.startingTime[0:2]>='12':
			self.startingTime = str( int(self.startingTime[0:2])-12)+remainder
		else :
			self.startingTime = str( int(self.startingTime[0:2]))+remainder
		return self
