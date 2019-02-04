from sys import platform
import os

class Konsola:

	def __init__(self):
		if platform == "win32":
			self.type = "cls"
		elif platform == "darwin" or "linux":
			self.type = "clear"
		else:
			return None
	def clear(self):
		os.system(self.type)
		pass
