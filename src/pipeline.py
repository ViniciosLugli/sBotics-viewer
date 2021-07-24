from src.instances.victim import AliveVictim, DeadVictim
from src.instances.points import Point, Line
import json
class Pipeline:
	def __init__(self, _path):
		self.last_line_limit = 0
		self.path = _path
		self.file = open(self.path, "r")

	def reset(self):
		self.last_line_limit = 0
		self.file = open(self.path, "r")

	def update(self, callback):
		for position, line in enumerate(self.file):
			if position >= self.last_line_limit:
				self.last_line_limit = position
				print("New line: ", line)
				callback(line)

class Parser:
	def getClass(line):
		return line[line.find("[") + 1:line.find("]")]

	def getArgs(line):
		return line[line.find("(") + 1:line.rfind(")")]

	def check(line):
		sclass = Parser.getClass(line)
		sargs = "{" + Parser.getArgs(line) + "}"
		print(sargs.replace("'", "\""))
		dictArgs = json.loads(sargs.replace("'", "\""))

		if sclass == "ALIVEVICTIM":
			return (sclass, AliveVictim(dictArgs["position"], dictArgs["priority"], dictArgs["isRescued"]), dictArgs["id"])
		elif sclass == "DEADVICTIM":
			return (sclass, DeadVictim(dictArgs["position"], dictArgs["priority"], dictArgs["isRescued"]), dictArgs["id"])
		elif sclass == "POINT":
			return (sclass, Point(dictArgs["position"], dictArgs["color"], dictArgs["info"]))
		elif sclass == "LINE":
			return (sclass, Line(dictArgs["position1"], dictArgs["position2"], dictArgs["color"], dictArgs["info"]))
		elif sclass == "RESCUE":
			return (sclass, {"triangle": dictArgs["triangle"], "exit": dictArgs["exit"]})
		elif sclass == "CLEARLINES":
			return (sclass)
		else:
			print("Not found source for line:", line)