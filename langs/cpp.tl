Cpp CppTest.cpp
self.code += ("\t" + self.indent)
self.code += (type + " " + name + " = " + value + ";\n")
self.code += (name + " = " + value + ";\n")
self.code += ('std::cout << "' + text + '";\n')
self.code += ('std::cout << ' + name + ';\n')
self.code += ("for(int " + name + " = 0;" + name + " < " + size + ";" + name + "++) {\n")
self.code += ("}\n")
self.code += (varname + " = " + name + "(" + args + ");\n")
START HEAD
#include <iostream>
#include <math.h>

int main() {
END HEAD
START FOOT
}
END FOOT
