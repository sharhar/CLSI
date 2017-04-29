def getContents(txt, name)
	ts = txt.index("<" + name + ">")
	te = txt.index("</" + name + ">")
	st = ts+name.length+2
	ln = te-st
	return txt[st, ln]
end

class Lang

	def initialize(src, indexFuncs)
		@src = src
		@body = ""
		@head = getContents(src, "head")
		@foot = getContents(src, "foot")
		@dest = getContents(src, "file")

		@funcs = Hash.new()

		funcsDef = getContents(src, "funcs")

		for f in indexFuncs
			name = f.split(" ")[0]

			@funcs.store(name, getContents(funcsDef, name))
		end
	end

	def func(name, varDict)
		result = @funcs[name]

		for var in varDict.keys()
			result = result.sub("$" + var, varDict[var])
		end

		@body += (result + "\n")
	end

	def write(dest)
		result = @head + @body + @foot
		file = File.open(dest + "/" + @dest, "w")
		file.write(result)
		file.close()
	end

end

contents = IO.read("settings.txt")

dest = getContents(contents, "dest")
srcs = getContents(contents, "langs")
funcsRaw = getContents(contents, "funcs")

idxFuncs = Array.new()

for f in funcsRaw.split("\n")
	if f != ""
		idxFuncs.push(f)
	end
end

langs = Array.new()

for l in srcs.split("\n")
	if not l == ""
		rawText = IO.read(l)
		langs.push(Lang.new(rawText, idxFuncs))
	end
end

idxFuncsDictTemplate = Hash.new()

for func in idxFuncs
	idxFuncsDictTemplate.store(func.split(" ")[0] ,func.split(" "))
end

codeFile = File.new("code.txt", "r")
code = codeFile.read()
codeFile.close()

for line in code.split("\n")
	if line != ""
		parts = line.split("#")
		name = parts[0]

		varDict = Hash.new()

		i = 1
		while i < parts.length do
			varDict.store(idxFuncsDictTemplate[name.sub(" ", "")][i], parts[i])
			i = i + 1
		end

		for l in langs
			l.func(name.sub(" ", ""), varDict)
		end
	end
end

for l in langs
	l.write(dest)
end