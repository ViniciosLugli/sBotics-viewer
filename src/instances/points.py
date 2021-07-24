from src.utils import _create_circle
from src.entity import Entity
class Point(Entity):
	def __init__(self, _position, _color, _info = ""):
		super().__init__()
		self.position = _position
		self.color = _color
		self.info = _info
		self.deleteQuery = False

	def draw(self, canvas):
		_create_circle(canvas, self.position[0] * 2, self.position[1] * 2, 3, fill = self.color, outline = "")

class Line(Entity):
	def __init__(self, _position1, _position2, _color, _info = ""):
		super().__init__()
		self.position1 = _position1
		self.position2 = _position2
		self.color = _color
		self.info = _info
		self.deleteQuery = False


