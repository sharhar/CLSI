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

class LangManager:

	def __init__(self):
		self.langs = []

	def addLang(self, lang):
		self.langs.append(lang)

	def newLine(self):
		for lang in self.langs:
			lang.newLine()

	def createVar(self, name, type, value):
		for lang in self.langs:
			lang.createVar(name, type, value)

	def setVar(self, name, value):
		for lang in self.langs:
			lang.setVar(name, value)

	def outputString(self, text):
		for lang in self.langs:
			lang.outputString(text)

	def outputVar(self, name):
		for lang in self.langs:
			lang.outputVar(name)

	def startFor(self, name, size):
		for lang in self.langs:
			lang.startFor(name, size)

	def endFor(self):
		for lang in self.langs:
			lang.endFor()

	def mathFunc(self, varname, name, args):
		for lang in self.langs:
			lang.mathFunc(varname, name, args)

	def end(self):
		for lang in self.langs:
			lang.end()

indexFile = open("langs/index.txt", "r")
index = indexFile.read().split("\n")
indexFile.close()

sourceCodes = []

for l in index:
	if(not l == ""):
		langFile = open("langs/" + l, "r")
		sourceCodes.append(langFile.read())
		langFile.close()

manager = LangManager()

for sourceCode in sourceCodes:
	manager.addLang(LangDef(sourceCode))

codeFile = open(sys.argv[1], "r")
code = codeFile.read().split("\n")
codeFile.close()

for line in code:
	if(not line == ""):
		parts = line.split(" ")
		if(parts[0] == "crv"):
			manager.createVar(parts[1], parts[2], parts[3])
		elif(parts[0] == "stv"):
			manager.setVar(parts[1], parts[2])
		elif(parts[0] == "mth"):
			manager.mathFunc(parts[1], parts[2], parts[3])
		elif(parts[0] == "for"):
			manager.startFor(parts[1], parts[2])
		elif(parts[0] == "edl"):
			manager.endFor()
		elif(parts[0] == "ots"):
			manager.outputString(parts[1])
		elif(parts[0] == "otv"):
			manager.outputVar(parts[1])
		else:
			print("-----------SYNTAX ERROR------------")
			print("Line: " + line)
			print("Unknown command: " + parts[0] + "\n-----------------------------------\n")
			exit()

manager.end()

for lang in manager.langs:
	nameParts = lang.name.split(" ")
	print("Writting " + nameParts[0] + "!")
	codeOut = open(nameParts[1], "w")
	codeOut.write(lang.code)
	codeOut.close()