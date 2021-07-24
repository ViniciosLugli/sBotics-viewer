from src.instances.victim import AliveVictim, DeadVictim
from src.instances.points import Point, Line

class Pipeline:
	def __init__(self, _path):
		self.last_line_limit = 0
		self.path = _path
		self.file = open(self.path, "r")

	def reset(self):
		self.last_line_limit = 0
		self.file = open(self.path, "r")

	def getUpdates(self, callback):
		for position, line in enumerate(file):
			if position > self.last_line_limit:
				self.last_line_limit = position
				print("New line: ", line)
				callback(line)

class Parser:
	def check(self, line):
		sclass = line[line.find("(") + 1:line.find(")")]
		if sclass == "ALIVEVICTIM":
			return AliveVictim()
		elif sclass == "DEADVICTIM":
			return DeadVictim()
		elif sclass == "POINT":
			return Point()
		elif sclass == "LINE":
			return Line()
		elif sclass == "TRIANGLE":
			return {"triangle": 0}
		elif sclass == "EXIT":
			return {"exit": 0}