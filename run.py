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

runs = []
for lang in langs:
	runs.append(getContents(lang, "run"))

for run in runs:
	command = ""

	for line in run.split("\n"):
		if not line == "":
			command += line + ";"

	#print(command)
	os.system(command)
