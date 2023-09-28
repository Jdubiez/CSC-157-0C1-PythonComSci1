import math

class Airplane:

	# data fields: (double) distance
	#			   (integer) direction
	#			   (integer) altitude
	#			   (string)	 callSign
	
	
	# object initializer or constructor
	# @param callSign - this airplanes unique call sign 
	#	     distance - the horizontal distance in miles from the tower 
	#		 direction - a bearing (compass direction) from the tower 
	#		 altitude - a positive altitude (height) in feet 
	# Precondition: callSign consists of a string containing letters, numbers, and symbols
	#				distance is a positive decimal number
	#				direction is an integer from 0 to 360
	#				altitude is a positive integer
	# Postcondition: correctly sets the data fields to the input parameters
	def __init__(self, callSign = 'AAA01', distance = 1, direction = 0, altitude = 0):
		self.callSign = callSign
		self.distance = float(math.fabs(distance))
		self.direction = int(direction % 360)
		self.altitude = int(math.fabs(altitude))
		
	# object string representation 		
	def __str__(self):
		info = str(self.callSign) + ' - '
		info += str(round(100*float(self.distance))/100)
		info += ' miles away at bearing '
		
		if self.direction < 100:
			info += '0'
		if self.direction < 10:
			info += '0'
		
		info += str(self.direction) + '\u00b0, altitude ' + str(self.altitude) + ' feet'
		
		return info	
		
	
	# Postcondition: Increases the altitude of the Airplane by 1000 feet.
	def gainAlt(self):
		self.altitude += 1000
	
	# Postcondition: Decreases the altitude of the Airplane by 1000 feet, 
	#				 or to 0 if altitude is less than 1000 feet.
	def loseAlt(self):
		self.altitude -= 1000
		
		if self.altitude < 0:
			self.altitude = 0	
	
	# Postcondition: Returns the altitude for this airplane object	
	def getAlt(self):
		return self.altitude	
	
	
	# @param distance - the horizontal distance in miles from the tower 
	#	     direction - a bearing (compass direction) from the tower 
	# Precondition: distance is a positive decimal number
	#				direction is an integer from 0 to 360
	#			
	# Postcondition: changes the Airplane position by distance miles on a heading of 
	#				 direction degrees.
	#				 
	def move(self, distance, direction):
		r1 = self.distance
		r2 = distance
		u1 = math.radians(self.direction)
		u2 = math.radians(direction)
		self.distance = math.sqrt(r1*r1 + r2*r2 + 2*r1*r2*math.cos(u2-u1))
		ang = math.atan2(r1*math.sin(u1) + r2*math.sin(u2), r1*math.cos(u1) + r2*math.cos(u2))
		dividend = int(round(math.degrees(ang)))
		self.direction = dividend - ((dividend//360)*360)
		
		

	# determines the distance between two airplane objects
	# @param other_plane - the other airplane relative to the calling(this) airplane
	#	     
	# Precondition: other_plane is a valid initialized airplane object
	#			
	# Postcondition: returns the distance between the calling(this) airplane and the 
	#				 other_plane object
	#				 
	def distTo(self,other_plane):
		r1 = self.distance
		r2 = other_plane.distance
		u1 = math.radians(self.direction)
		u2 = math.radians(other_plane.direction)
		between = math.sqrt(r1*r1 + r2*r2 - 2*r1*r2*math.cos(u2-u1))
		return round(100*between)/100
	
	
	

