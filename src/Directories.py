import os, sys
import pdb

class Directories:
	def __init__(self):
		self.currDir = "/"

	def getCurrDir(self):
		currDirStr = self.currDir
		currDirStr = currDirStr.replace('/', ' ')
		if len(currDirStr) == 1:
			currDirStr = "root directory"
		return currDirStr

	def getNumDirs(self):
		dirs = os.listdir(self.currDir)
                dirs = [dir for dir in dirs if os.path.isdir(os.path.join(self.currDir, dir))]
		return str(len(dirs))

	def listDirs(self, sortOrder):
		dirs = os.listdir(self.currDir)
		dirs = [dir for dir in dirs if os.path.isdir(os.path.join(self.currDir, dir))]
		if sortOrder is not None:
			if len(sortOrder) > 0:
				if sortOrder[0] == "a" or sortOrder[0] == "A":
					dirs = sorted(dirs)
				if sortOrder[0] == "r" or sortOrder[0] == "R":
					dirs = sorted(dirs, reverse=True)
		dirsStr = ""
		for i in range(len(dirs)):
			data = dirs[i]
			data = data.replace("+", " and ")
			dirsStr += str(i) + " " + data + ' <break time="1s"/>'
		return dirsStr
