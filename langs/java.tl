Java JavaTest.java
self.code += ("\t\t" + self.indent)
self.code += (type + " " + name + " = " + value + ";\n")
self.code += (name + " = " + value + ";\n")
self.code += ('System.out.print("' + text + '");\n')
self.code += ('System.out.print(' + name + ');\n')
self.code += ("for(int " + name + " = 0;" + name + " < " + size + ";" + name + "++) {\n")
self.code += ("}\n")
self.code += (varname + " = " + "Math." + name + "(" + args + ");\n")
START HEAD
import java.util.Scanner;

public class JavaTest {
	public static void main(String[] args) {
END HEAD
START FOOT
	}
}
END FOOT
