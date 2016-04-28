import os
import sys

class LangDef:

	def __init__(self, source):
		self.source = source
		self.lines = self.source.split("\n")
		self.code = ""
		self.indent = ""
		self.name = self.lines[0]
		self.head = ""
		self.foot = ""
		endHead = -1

		if(not self.lines[9] == "START HEAD"):
			print("Cant find head!")
		else:
			for i in range(10, len(self.lines)):
				if(not self.lines[i] == "END HEAD"):
					self.head += (self.lines[i] + "\n")
				else:
					endHead = i
					break

		self.code += self.head

		if(not self.lines[endHead+1] == "START FOOT"):
			print("Cant find foot!")
		else:
			for i in range(endHead+2, len(self.lines)):
				if(not self.lines[i] == "END FOOT"):
					self.foot += (self.lines[i] + "\n")
				else:
					break
		

	def newLine(self):
		exec(self.lines[1])

	def createVar(self, name, type, value):
		self.newLine()
		exec(self.lines[2])

	def setVar(self, name, value):
		self.newLine()
		exec(self.lines[3])

	def outputString(self, text):
		self.newLine()
		exec(self.lines[4])

	def outputVar(self, name):
		self.newLine()
		exec(self.lines[5])

	def startFor(self, name, size):
		self.newLine()
		exec(self.lines[6])
		self.indent += "\t"

	def endFor(self):
		self.indent = self.indent[1:-1]
		self.newLine()
		exec(self.lines[7])

	def mathFunc(self, varname, name, args):
		self.newLine()
		exec(self.lines[8])

	def end(self):
		self.code += self.foot

indexFile = open("langs/index.txt", "r")
index = indexFile.read().split("\n")
indexFile.close()

sourceCodes = []

for l in index:
	if(not l == ""):
		langFile = open("langs/" + l, "r")
		sourceCodes.append(langFile.read())
		langFile.close()

langs = []

for sourceCode in sourceCodes:
	langs.append(LangDef(sourceCode))

codeFile = open(sys.argv[1], "r")
code = codeFile.read().replace("\\", "\\\\").split("\n")
codeFile.close()

for line in code:
	if(not line == ""):

		parts = line.split(" ", 1)
		for lang in langs:
			exec("lang." + parts[0] + "(" + parts[1] + ")")

for lang in langs:
	lang.end()

for lang in langs:
	nameParts = lang.name.split(" ")
	print("Writting " + nameParts[0] + "!")
	codeOut = open(nameParts[1], "w")
	codeOut.write(lang.code)
	codeOut.close()