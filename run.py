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

runs = []
names = []
for lang in langs:
	runs.append(getContents(lang, "run"))
	names.append(getContents(lang, "name"))

times = []

for i in range(len(runs)):
	command = ""

	for line in runs[i].split("\n"):
		if not line == "":
			command += line + ";"

	print("Starting " + names[i] + " test...")
	startTime = int(time.time() * 1000000)
	os.system(command)
	endTime = int(time.time() * 1000000)
	print("Ending " + names[i] + " test...")

	times.append(names[i] + ": " + str(endTime - startTime))

print("\n=========================TIMES=========================\n")
print("time is measured in micro seconds")

for t in times:
	print(t)
