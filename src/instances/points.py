from src.utils import _create_circle

class Point:
	def __init__(self, _position, _color, _info = ""):
		self.position = _position
		self.color = _color
		self.info = _info
		self.deleteQuery = False

class Line:
	def __init__(self, _position1, _position2, _color, _info = ""):
		self.position1 = _position1
		self.position2 = _position2
		self.color = _color
		self.info = _info
		self.deleteQuery = False


