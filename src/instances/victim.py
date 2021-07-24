from src.utils import _create_circle
from src.entity import Entity
from tkinter import *

class Victim(Entity):
	def __init__(self, position, priority, isRescued, pontuation, color):
		super().__init__()
		self.position = position
		self.priority = priority
		self.pontuation = pontuation
		self.color = color
		self.isRescued = isRescued
		self.substracter = 20
		self.attempt = 0
		self.canvas = None

	def rescue(self, value = True):
		isRescued = value

	def draw(self, canvas):
		_create_circle(canvas, self.position, 12, fill = self.color, outline = "")

class AliveVictim(Victim):
	def __init__(self, position, priority = 1, isRescued = False):
		super().__init__(position, priority, isRescued, 60, "#BFBFBF")

class DeadVictim(Victim):
	def __init__(self, position, priority = 0, isRescued = False):
		super().__init__(position, priority, isRescued, 50, "#343434")
