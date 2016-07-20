import os
import sys

def getContents(text, name):
	start = text.find("<" + name + ">")
	end = text.find("</" + name + ">")
	return text[start+len(name)+2:end]

class Lang:
	def __init__(self, src, indexFuncs):
		self.src = src
		self.body = ""
		self.head = getContents(src, "head")
		self.foot = getContents(src, "foot")
		self.dest = getContents(src, "file")

		self.funcs = {}

		funcsDef = getContents(src, "funcs")

		for f in indexFuncs:
			name = f.split(" ")[0]

			self.funcs[name] = getContents(funcsDef, name)

	def func(self, name, varDict):
		result = self.funcs[name]

		for var in varDict.keys():
			result = result.replace("$" + var, varDict[var])

		self.body += (result + "\n")

	def write(self, dest):
		result = self.head + self.body + self.foot
		file = open(dest + "/" + self.dest, "w")
		file.write(result)
		file.close()



settingsFile = open("settings.txt", "r")
settings = settingsFile.read()
settingsFile.close()

dest = getContents(settings, "dest")
srcs = getContents(settings, "langs")
funcsRaw = getContents(settings, "funcs")

idxFuncs = []

for f in funcsRaw.split("\n"):
	if not f == "":
		idxFuncs.append(f)

langs = []

for l in srcs.split("\n"):
	if not l == "":
		file = open(l, "r")
		rawText = file.read()
		file.close()
		langs.append(Lang(rawText, idxFuncs))

idxFuncsDictTemplate = {}

for func in idxFuncs:
	idxFuncsDictTemplate[func.split(" ")[0]] = func.split(" ")

codeFile = open("code.txt", "r")
code = codeFile.read()
codeFile.close()

for line in code.split("\n"):
	if not line == "":
		parts = line.split("#")
		name = parts[0]

		varDict = {}

		for i in range(1, len(parts)):
			varDict[idxFuncsDictTemplate[name.replace(" ", "")][i]] = parts[i]

		for l in langs:
			l.func(name.replace(" ", ""), varDict)

for l in langs:
	l.write(dest)