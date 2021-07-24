class Entity:
	def __init__(self):
		self.deleteQuery = False

	def delete(self):
		self.deleteQuery = True

	def undoDelete(self):
		self.deleteQuery = False

	def inDeleteQuery(self):
		return self.deleteQuery