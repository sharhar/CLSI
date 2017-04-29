def getContents(txt, name)
	ts = txt.index("<" + name + ">")
	te = txt.index("</" + name + ">")
	st = ts+name.length+2
	ln = te-st
	return txt[st, ln]
end

settingsFile = File.new("settings.txt", "r")
settings = settingsFile.read()
settingsFile.close()

srcs = getContents(settings, "langs")

langs = Array.new()

for l in srcs.split("\n")
	if l != ""
		file = File.new(l, "r")
		rawText = file.read()
		file.close()
		langs.push(rawText)
	end
end

comps = Array.new()
names = Array.new()
for lang in langs
	comps.push(getContents(lang, "run"))
	names.push(getContents(lang, "name"))
end

times = Array.new()

i = 0
while i < comps.length do
	cmdArr = Array.new()

	cmd = "cd test;"

	for line in comps[i].split("\n")
		if line.lstrip().rstrip().length > 0
			cmd += line.gsub("\r", "")
			cmd += ";"
		end
	end

	puts("Running " + names[i] + "...")
	startTime = Time.now()
	system(cmd)
	endTime = Time.now()

	times.push(names[i] + ": " + ((endTime - startTime)*1000).to_s())

	i = i + 1
end

puts("\n=========================TIMES=========================\n")
puts("time is measured in micro seconds")

for t in times
	puts(t)
end
