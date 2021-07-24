from src.utils import _create_circle

class RescueInfo:
	def __init__(self):
		self.triangle = None
		self.exit = None

	def reset(self):
		self.triangle = None
		self.exit = None