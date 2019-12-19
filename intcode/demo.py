from intcode import intcode


programString = "2,4,4,5,99,0"
computer = intcode()
computer.loadProgram(programString)

print(computer.memory)

computer.execute()
print(computer.memory)