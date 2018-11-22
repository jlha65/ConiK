#import symbol_table as st 

class mem:
    
    #Size of the memory given to each of our lists
    memorySize = 1000

    #Constructor
    def __init__(self) :

        self.memory = [None] * self.memorySize * 24

        self.giCont = 0                 #Global int
        self.gfCont = self.memorySize   #Global float
        self.gbCont = self.memorySize*2 #Global bool
        self.liCont = self.memorySize*3 #local int
        self.lfCont = self.memorySize*4 #local float
        self.lbCont = self.memorySize*5 #local bool
        self.tiCont = self.memorySize*6 #temporal int
        self.tfCont = self.memorySize*7 #temporal float
        self.tbCont = self.memorySize*8 #temporal bool
        self.ciCont = self.memorySize*9 #constant int jeje xd
        self.cfCont = self.memorySize*10 #constant float jeje xc

        self.gpCont = self.memorySize*11
        self.geCont = self.memorySize*12
        self.ghCont = self.memorySize*13
        self.gcCont = self.memorySize*14
        self.lpCont = self.memorySize*15
        self.leCont = self.memorySize*16
        self.lhCont = self.memorySize*17
        self.lcCont = self.memorySize*18
        self.tpCont = self.memorySize*19
        self.teCont = self.memorySize*20
        self.thCont = self.memorySize*21
        self.tcCont = self.memorySize*22

    def add_var(self, data_type, value, size, scope) :
        if data_type == "int" or data_type == 0 :
            if scope == "GLOBAL":
                self.memory[self.giCont] = value
                self.giCont += size
                return self.giCont - size
            else :
                self.memory[self.liCont] = value
                self.liCont += size
                return self.liCont - size
        elif data_type == "float" or data_type == 1 :
            if scope == "GLOBAL":
                self.memory[self.gfCont] = value
                self.gfCont += size
                return self.gfCont - size
            else :
                self.memory[self.lfCont] = value
                self.lfCont += size
                return self.lfCont - size
        elif data_type == "bool" or data_type == 2 :
            if scope == "GLOBAL":
                self.memory[self.gbCont] = value
                self.gbCont += size
                return self.gbCont - size
            else :
                self.memory[self.lbCont] = value
                self.lbCont += size
                return self.lbCont - size
        elif data_type == "parabola" :
            if scope == "GLOBAL":
                self.memory[self.gpCont] = value
                self.gpCont += size
                return self.gpCont - size
            else :
                self.memory[self.lpCont] = value
                self.lpCont += size
                return self.lpCont - size
        elif data_type == "ellipse" :
            if scope == "GLOBAL":
                self.memory[self.geCont] = value
                self.geCont += size
                return self.geCont - size
            else :
                self.memory[self.leCont] = value
                self.leCont += size
                return self.leCont - size
        elif data_type == "hyperbola" :
            if scope == "GLOBAL":
                self.memory[self.ghCont] = value
                self.ghCont += size
                return self.ghCont - size
            else :
                self.memory[self.lhCont] = value
                self.lhCont += size
                return self.lhCont - size
        elif data_type == "circle" :
            if scope == "GLOBAL":
                self.memory[self.gcCont] = value
                self.gcCont += size
                return self.gcCont - size
            else :
                self.memory[self.lcCont] = value
                self.lcCont += size
                return self.lcCont - size

    def checkSizeAvail(self, sizeRequested, data_type, scope) :
        sumAddr = 0 
        if data_type == "int" or data_type == 0 :
            if scope == "GLOBAL":
                sumAddr = sizeRequested + self.giCont
                return sumAddr < self.memorySize
            elif scope == "TEMP":
                sumAddr = sizeRequested + self.tiCont
                return sumAddr < self.memorySize*7
            else :
                sumAddr = sizeRequested + self.liCont
                return sumAddr < self.memorySize*4
        elif data_type == "float" or data_type == 1 :
            if scope == "GLOBAL":
                sumAddr = sizeRequested + self.gfCont
                return sumAddr < self.memorySize*2
            elif scope == "TEMP":
                sumAddr = sizeRequested + self.tfCont
                return sumAddr < self.memorySize*8
            else :
                sumAddr = sizeRequested + self.lfCont
                return sumAddr < self.memorySize*5
        elif data_type == "bool" or data_type == 2 :
            if scope == "GLOBAL":
                sumAddr = sizeRequested + self.gbCont
                return sumAddr < self.memorySize*3
            elif scope == "TEMP":
                sumAddr = sizeRequested + self.tbCont
                return sumAddr < self.memorySize*9
            else :
                sumAddr = sizeRequested + self.lbCont
                return sumAddr < self.memorySize*6
        elif data_type == "parabola" :
            if scope == "GLOBAL":
                sumAddr = sizeRequested + self.gpCont
                return sumAddr < self.memorySize*12
            elif scope == "TEMP":
                sumAddr = sizeRequested + self.tpCont
                return sumAddr < self.memorySize*20
            else :
                sumAddr = sizeRequested + self.lpCont
                return sumAddr < self.memorySize*16
        elif data_type == "ellipse" :
            if scope == "GLOBAL":
                sumAddr = sizeRequested + self.geCont
                return sumAddr < self.memorySize*13
            elif scope == "TEMP":
                sumAddr = sizeRequested + self.teCont
                return sumAddr < self.memorySize*21
            else :
                sumAddr = sizeRequested + self.leCont
                return sumAddr < self.memorySize*17
        elif data_type == "hyperbola" :
            if scope == "GLOBAL":
                sumAddr = sizeRequested + self.ghCont
                return sumAddr < self.memorySize*14
            elif scope == "TEMP":
                sumAddr = sizeRequested + self.thCont
                return sumAddr < self.memorySize*22
            else :
                sumAddr = sizeRequested + self.lhCont
                return sumAddr < self.memorySize*18
        elif data_type == "circle" :
            if scope == "GLOBAL":
                sumAddr = sizeRequested + self.gcCont
                return sumAddr < self.memorySize*15
            elif scope == "TEMP":
                sumAddr = sizeRequested + self.tcCont
                return sumAddr < self.memorySize*23
            else :
                sumAddr = sizeRequested + self.lcCont
                return sumAddr < self.memorySize*19
        else :
            raise Exception("Fatal error, no memory for such data type")
    
    def nextAvail(self, data_type):
        if data_type == 0 or data_type == "int": #int
            self.tiCont += 1
            return self.tiCont - 1
        elif data_type == 1 or data_type == "float": #float
            self.tfCont += 1
            return self.tfCont - 1   
        elif data_type == 2 or data_type == "bool": #bool
            self.tbCont += 1
            return self.tbCont - 1
        elif data_type == 3 or data_type == "parabola": #parabola
            self.tpCont += 1
            return self.tpCont - 1
        elif data_type == 4 or data_type == "circle": #circle
            self.tcCont += 1
            return self.tcCont - 1
        elif data_type == 5 or data_type == "ellipse": #ellipse
            self.teCont += 1
            return self.teCont - 1
        elif data_type == 6  or data_type == "hyperbola": #hyperbola
            self.thCont += 1
            return self.thCont - 1

    #Save value in address in memory
    def save(self,value,address):
        #print("saved value "+str(value)+" in address "+str(address))
        self.memory[address] = value

    #Returns the value stored in an address
    def access(self,address):
        return self.memory[address]

    #Utility function that prints memory in case it is needed
    def print(self):
        print("printing memory")
        cont = 0
        for x in self.memory:
            if x != None:
                print(str(cont) + ".- " + str(x))
            cont = cont + 1

mem = mem()