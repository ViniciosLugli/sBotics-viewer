from src.instances.points import LineRescue

class RescueInfo:
	def __init__(self):
		self.triangle = None
		self.exit = None

	def reset(self):
		self.triangle = None
		self.exit = None

	def update(self):
		objt = None
		obje = None
		if(not (self.triangle is None)):
			if(self.triangle == 1):
				objt = LineRescue([200, 300], [300, 200], "black")

			elif(self.triangle == 2):
				objt = LineRescue([300, 100], [200, 0], "black")

			elif(self.triangle == 3):
				objt = LineRescue([0, 100], [100, 0], "black")

		if(not (self.exit is None)):
			if(self.exit == 1):
				obje = LineRescue([300-2.5, 300-4], [300-2.5, 200], "#41B564")

			elif(self.exit == 2):
				obje = LineRescue([300-4, 2.5], [200, 2.5], "#41B564")

			elif(self.exit == 3):
				obje = LineRescue([2.5, 100], [2.5, 4], "#41B564")
		return (obje, objt)