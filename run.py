import os, time

print("Compiling C++")
cppCompStartTime = int(time.time() * 1000000)
os.system("g++ CppTest.cpp -o CppTest")
cppCompEndTime = int(time.time() * 1000000)
print("Compiling Java")
javaCompStartTime = int(time.time() * 1000000)
os.system("javac JavaTest.java")
javaCompEndTime = int(time.time() * 1000000)

print("Running C++!")
cppStartTime = int(time.time() * 1000000)
os.system("./CppTest")
cppEndTime = int(time.time() * 1000000)

print("Running Java!")
javaStartTime = int(time.time() * 1000000)
os.system("java JavaTest")
javaEndTime = int(time.time() * 1000000)

print("Running Python!")
pythonStartTime = int(time.time() * 1000000)
os.system("python3 PythonTest.py")
pythonEndTime = int(time.time() * 1000000)

print("\n\n--------------RESULTS---------------")

print("CPP  comp: " + str(cppCompEndTime - cppCompStartTime))
print("JAVA comp: " + str(javaCompEndTime - javaCompStartTime))

print("")

print("CPP   : " + str(cppEndTime - cppStartTime))
print("JAVA  : " + str(javaEndTime - javaStartTime))
print("PYTHON: " + str(pythonEndTime - pythonStartTime))
