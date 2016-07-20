<name>Cpp</name>
<file>CppTest.cpp</file>

<funcs>
	<print>printf($value);</print>
	<var>$type $name = $value;</var>
	<setvar>$name = $value;</setvar>
</funcs>

<head>
#include <stdio.h>

int main() {
</head>

<foot>
return 0;
}
</foot>

<comp>
cd test
g++ -c CppTest.cpp
g++ CppTest.o -o CppTest
</comp>

<run>
cd test
./CppTest
</run>