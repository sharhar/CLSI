def getContents(txt, name)
	ts = txt.index("<" + name + ">")
	te = txt.index("</" + name + ">")
	st = ts+name.length+2
	ln = te-st
	return txt[st, ln]
end

class Lang

	def initialize(src, indexFuncs, varPrefix, varSufix)
		@src = src
		@body = ""
		@head = getContents(src, "head")
		@foot = getContents(src, "foot")
		@dest = getContents(src, "file")
		@varPrefix = varPrefix
		@varSufix = varSufix
		@indent = ""

		@funcs = Hash.new()

		funcsDef = getContents(src, "funcs")

		for f in indexFuncs
			name = f.split(" ")[0]

			@funcs.store(name, getContents(funcsDef, name))
		end
	end

	def func(name, varDict)
		if (name == "add_indent")
			@indent += "\t"
			return
		end

		if(name == "sub_indent" && @indent.length > 0) 
			@indent.slice!(0)
			return
		end

		result = @funcs[name]

		for var in varDict.keys()
			result = result.gsub("$" + var, varDict[var])
		end

		@body += (@indent + result + "\n")
	end

	def write(dest)
		result = @head + @body + @foot
		file = File.open(dest + "/" + @dest, "w")
		file.write(result)
		file.close()
	end

end

settingsFile = File.new("settings.txt", "r")
settings = settingsFile.read()
settingsFile.close()

dest = getContents(settings, "dest")
srcs = getContents(settings, "langs")
funcsRaw = getContents(settings, "funcs")
fnOpen = getContents(settings, "fnOpen")
fnClose = getContents(settings, "fnClose")
seperator = getContents(settings, "seperator")
varPrefix = getContents(settings, "varPrefix")
varSufix = getContents(settings, "varSufix")

idxFuncs = Array.new()

for f in funcsRaw.split("\n")
	if f != ""
		idxFuncs.push(f)
	end
end

langs = Array.new()

for l in srcs.split("\n")
	if not l == ""
		file = File.new(l, "r")
		rawText = file.read()
		file.close()
		langs.push(Lang.new(rawText, idxFuncs, varPrefix, varSufix))
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
		parts = line.split(fnOpen)
		name = parts[0]

		argStart = line.index(fnOpen)+1
		argEnd = line.index(fnClose)

		fnArgs = line[argStart, argEnd-argStart]
		pArgs = fnArgs.split(seperator)

		varDict = Hash.new()

		i = 0
		while i < pArgs.length do
			varDict.store(idxFuncsDictTemplate[name.gsub(" ", "")][i+1], pArgs[i])
			i = i + 1
		end

		for l in langs
			l.func(name.gsub(" ", ""), varDict)
		end
	end
end

for l in langs
	l.write(dest)
end