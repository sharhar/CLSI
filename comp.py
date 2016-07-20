import os, time

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
names = []
for lang in langs:
	comps.append(getContents(lang, "comp"))
	names.append(getContents(lang, "name"))

times = []

for i in range(len(comps)):
	command = ""

	for line in comps[i].split("\n"):
		if not line == "":
			command += line + ";"

	print("Compiling " + names[i] + "...")
	startTime = int(time.time() * 1000000)
	os.system(command)
	endTime = int(time.time() * 1000000)

	times.append(names[i] + ": " + str(endTime - startTime))

print("\n=========================TIMES=========================\n")
print("time is measured in micro seconds")

for t in times:
	print(t)
