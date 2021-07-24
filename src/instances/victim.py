from src.utils import _create_circle
from tkinter import *

class Victim:
	def __init__(self, position, priority, pontuation, color, attempt):
		self.position = position
		self.priority = priority
		self.pontuation = pontuation
		self.color = color
		self.isRescued = False
		self.substracter = 20
		self.attempt = 0
		self.canvas = None
		self.deleteQuery = False

	def draw(self, canvas):
		pass

	def rescue(self, value = True):
		isRescued = value

	def draw(self, canvas):
		_create_circle(canvas, self.position[0] * 2, self.position[1] * 2, 12, fill = self.color, outline = "")


class AliveVictim(Victim):
	def __init__(self, position, priority = 1, attempt = 0):
		super().__init__(position, priority, 60, "#BFBFBF", attempt)

class DeadVictim(Victim):
	def __init__(self, position, priority = 0, attempt = 0):
		super().__init__(position, priority, 50, "#343434", attempt)
