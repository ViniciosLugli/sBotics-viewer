from src.instances.points import LineRescue

class RescueInfo:
	def __init__(self):
		self.triangle = None
		self.exit = None

	def reset(self):
		self.triangle = None
		self.exit = None

	def update(self):
		if(self.triangle is None):
			return None
		if(self.triangle == 1):
			obj = LineRescue([200, 300], [300, 200], "black")

		elif(self.triangle == 2):
			obj = LineRescue([300, 100], [200, 0], "black")

		elif(self.triangle == 3):
			obj = LineRescue([0, 100], [100, 0], "black")
		return obj