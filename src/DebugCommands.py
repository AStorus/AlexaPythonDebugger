import sys

class DebugCommands:
	def __init__(self, filename):
		self.filename = filename

	def set_breakpoint(self, line):
		print "b " + filename + ":" + str(line)

filename = sys.argv[1]
debugCommands = DebugCommands(filename)
debugCommands.set_breakpoint(5)
