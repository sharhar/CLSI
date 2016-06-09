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

			tempList = []
			tempList.append(f)
			tempList.append(getContents(funcsDef, name))

			self.funcs[name] = tempList


indexFile = open("langs/index.txt", "r")
index = indexFile.read()
indexFile.close()

dest = getContents(index, "dest")
srcs = getContents(index, "langs")
funcsRaw = getContents(index, "funcs")

langs = []

for l in srcs.split("\n"):
	if not l == "":
		file = open("langs/" + l, "r")
		rawText = file.read()
		file.close()
		langs.append(Lang(rawText))


