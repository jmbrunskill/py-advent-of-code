class intcode():
    def __init__(self):
        self.instructionPointer = 0
        self.memory = []
        self.stopped = False
   
    def loadMemory(self, memList):
        self.memory = memList.copy()

    def loadProgram(self, programString):
        numbers = programString.split(",")
        self.memory = list(map(int,numbers))

    def isStopped(self):
        return self.stopped

    def add(self,p1_location,p2_location,output_location):
        self.memory[output_location] = self.memory[p1_location] + self.memory[p2_location]
        self.instructionPointer += 4
        return

    def mult(self, p1_location, p2_location, output_location):
        self.memory[output_location] = self.memory[p1_location] * \
            self.memory[p2_location]
        self.instructionPointer += 4
        return

    def stop(self, p1_location, p2_location, output_location):
        #Stop function doesn't use any of these parameters, but needs them to use the dictionary based case
        self.stopped = True
        return

    def decode(self):
        opcode = self.memory[self.instructionPointer]

        p1_location = 0
        p2_location = 0
        p3_location = 0
        if opcode != 99:
            p1_location = self.memory[self.instructionPointer+1]
            p2_location = self.memory[self.instructionPointer+2]
            p3_location = self.memory[self.instructionPointer+3]
        
        return opcode,p1_location,p2_location,p3_location

    def step(self, opcode, p1_location, p2_location, p3_location):
        funcs = {
            1: self.add,
            2: self.mult,
            99: self.stop
        }
        funcs[opcode](p1_location, p2_location, p3_location)
        

    def execute(self):

        while not self.isStopped():
            #Interpret the current instruction
            #Find the parameters
            opcode, p1_location, p2_location, p3_location = self.decode()
            #Execute that instruction
            self.step(opcode, p1_location, p2_location, p3_location)
            #Update instruction Pointer - This happens automatically in each instruction