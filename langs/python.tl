Python pyTest.py
self.code += ("" + self.indent)
self.code += (name + " = " + value + "\n")
self.code += (name + " = " + value + "\n")
self.code += ('print("' + text + '", end = "")\n')
self.code += ('print(str(' + name + '), end = "")\n')
self.code += ("for " + name + " in range(" + size + "):\n")
self.code += ("\n")
self.code += (varname + " = " + "math." + name + "(" + args + ")\n")
START HEAD
import math
END HEAD
START FOOT
END FOOT
