import os

def getContents(text, name):
	start = text.find("<" + name + ">")
	end = text.find("</" + name + ">")
	return text[start+len(name)+2:end]

settingsFile = open("settings.txt", "r")
settings = settingsFile.read()
settingsFile.close()

srcs = getContents(settings, "langs")

langs = []

for l in srcs.split("\n"):
	if not l == "":
		file = open(l, "r")
		rawText = file.read()
		file.close()
		langs.append(rawText)

comps = []
for lang in langs:
	comps.append(getContents(lang, "comp"))

for comp in comps:
	command = ""

	for line in comp.split("\n"):
		if not line == "":
			command += line + ";"

	#print(command)
	os.system(command)
