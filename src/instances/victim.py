from src.utils import _create_circle
from src.entity import Entity
from tkinter import *

class Victim(Entity):
	def __init__(self, position, priority, isRescued, pontuation, color, attempt):
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
	def __init__(self, position, priority = 1, isRescued = False, attempt = 0):
		super().__init__(position, priority, 60, "#BFBFBF", attempt)

class DeadVictim(Victim):
	def __init__(self, position, priority = 0, isRescued = False, attempt = 0):
		super().__init__(position, priority, 50, "#343434", attempt)
