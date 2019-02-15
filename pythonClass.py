#robot class

class Robot:
	def __init__(self, givenName, givenColor, givenWeight):
		self.name = givenName
		self.name = givenColor
		self.weight = givenWeight
		Robot lookingAt

	def intro(self):
		print("my name is " + self.name)

r1 = Robot("Tom", "red", 30)
'''r1.name = "Tom"
r1.color = "red"
r1.weight = 30

r2 = Robot()
r2.name = "Jerry"
r2.color = "blue"
r2.weight = 40
'''
r1.intro()
#r2.intro()


class Person:
	def __init__(self, n, p, i):
		self.name = n
		self.personality = p
		self.is_sitting = i

	def sit_down(self):
		self.is_sitting = True

	def stand_up(self):
		self.is_sitting = False

p1 = Person("Alice", "aggresive", False)
p1.robot_owned = r1
p1.robot_owned.intro()
