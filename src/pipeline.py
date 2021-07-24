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

	def getUpdates(self, callback):
		for position, line in enumerate(file):
			if position > self.last_line_limit:
				self.last_line_limit = position
				print("New line: ", line)
				callback(line)

class Parser:
	def getClass(line):
		return line[line.find("[") + 1:line.find("]")]

	def getArgs(line):
		return line[line.find("(") + 1:line.find(")")]

	def check(self, line):
		sclass = getClass(line)
		sargs = "{" + getArgs(line) + "}"
		dictArgs = json.loads(sargs.replace("'", "\""))

		if sclass == "ALIVEVICTIM":
			return (AliveVictim(dictArgs["position"], dictArgs["priority"], dictArgs["isRescued"]), dictArgs["id"])
		elif sclass == "DEADVICTIM":
			return (DeadVictim(dictArgs["position"], dictArgs["priority"], dictArgs["isRescued"]), dictArgs["id"])
		elif sclass == "POINT":
			return Point(dictArgs["position"], dictArgs["color"], dictArgs["info"])
		elif sclass == "LINE":
			return Line((dictArgs["position1"], dictArgs["position2"], dictArgs["color"], dictArgs["info"])
		elif sclass == "RESCUE":
			return {"triangle": dictArgs["triangle"], "exit": dictArgs["exit"]}
		elif sclass == "CLEARLINES":
			return {"clear_lines": True}
		else:
			print("Not found source for line:", line)