#import symbol_table as st 

class mem:
    
    #Size of the memory given to each of our lists
    memorySize = 15000

    #Constructor
    def __init__(self) :
        # self.globalInt = [None] * self.memorySize
        # self.globalFloat = [None] * self.memorySize
        # self.globalBool = [None] * self.memorySize
        # self.localInt = [None] * self.memorySize
        # self.localFloat = [None] * self.memorySize
        # self.localBool = [None] * self.memorySize
        # self.tempInt = [None] * self.memorySize
        # self.tempFloat = [None] * self.memorySize
        # self.tempBool = [None] * self.memorySize
        # self.consInt = [None] * self.memorySize
        # self.consFloat = [None] * self.memorySize

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
                print(self.gpCont)
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
                print("int global " + str(sumAddr))
                return sumAddr < self.memorySize
            elif scope == "TEMP":
                sumAddr = sizeRequested + self.tiCont
                print("int temp " + str(sumAddr))
                return sumAddr < self.memorySize*7
            else :
                sumAddr = sizeRequested + self.liCont
                print("int local " + str(sumAddr))
                return sumAddr < self.memorySize*4
        elif data_type == "float" or data_type == 1 :
            if scope == "GLOBAL":
                sumAddr = sizeRequested + self.gfCont
                print("float global " + str(sumAddr))
                return sumAddr < self.memorySize*2
            elif scope == "TEMP":
                sumAddr = sizeRequested + self.tfCont
                print("float temp " + str(sumAddr))
                return sumAddr < self.memorySize*8
            else :
                sumAddr = sizeRequested + self.lfCont
                print("float local " + str(sumAddr))
                return sumAddr < self.memorySize*5
        elif data_type == "bool" or data_type == 2 :
            if scope == "GLOBAL":
                sumAddr = sizeRequested + self.gbCont
                print("bool global " + str(sumAddr))
                return sumAddr < self.memorySize*3
            elif scope == "TEMP":
                sumAddr = sizeRequested + self.tbCont
                print("bool temporal " + str(sumAddr))
                return sumAddr < self.memorySize*9
            else :
                sumAddr = sizeRequested + self.lbCont
                print("bool local " + str(sumAddr))
                return sumAddr < self.memorySize*6
        elif data_type == "parabola" :
            if scope == "GLOBAL":
                sumAddr = sizeRequested + self.gpCont
                print("parabola global " + str(sumAddr))
                return sumAddr < self.memorySize*12
            elif scope == "TEMP":
                sumAddr = sizeRequested + self.tpCont
                print("parabola temporal " + str(sumAddr))
                return sumAddr < self.memorySize*20
            else :
                sumAddr = sizeRequested + self.lpCont
                print("parabola local " + str(sumAddr))
                return sumAddr < self.memorySize*16
        elif data_type == "ellipse" :
            if scope == "GLOBAL":
                sumAddr = sizeRequested + self.geCont
                print("ellipse global " + str(sumAddr))
                return sumAddr < self.memorySize*13
            elif scope == "TEMP":
                sumAddr = sizeRequested + self.teCont
                print("ellipse temporal " + str(sumAddr))
                return sumAddr < self.memorySize*21
            else :
                sumAddr = sizeRequested + self.leCont
                print("ellipse local " + str(sumAddr))
                return sumAddr < self.memorySize*17
        elif data_type == "hyperbola" :
            if scope == "GLOBAL":
                sumAddr = sizeRequested + self.ghCont
                print("hyperbola global " + str(sumAddr))
                return sumAddr < self.memorySize*14
            elif scope == "TEMP":
                sumAddr = sizeRequested + self.thCont
                print("hyperbola temporal " + str(sumAddr))
                return sumAddr < self.memorySize*22
            else :
                sumAddr = sizeRequested + self.lhCont
                print("hyperbola local " + str(sumAddr))
                return sumAddr < self.memorySize*18
        elif data_type == "circle" :
            if scope == "GLOBAL":
                sumAddr = sizeRequested + self.gcCont
                print("circle global " + str(sumAddr))
                return sumAddr < self.memorySize*15
            elif scope == "TEMP":
                sumAddr = sizeRequested + self.tcCont
                print("circle temporal " + str(sumAddr))
                return sumAddr < self.memorySize*23
            else :
                sumAddr = sizeRequested + self.lcCont
                print("circle local " + str(sumAddr))
                return sumAddr < self.memorySize*19
        else :
            print("jeje equis de")
    
    def nextAvail(self, data_type):
        if data_type == 0:
            self.tiCont += 1
            return self.tiCont - 1
        elif data_type == 1:
            self.tfCont += 1
            return self.tfCont - 1   
        elif data_type == 2:
            self.tbCont += 1
            return self.tbCont - 1

    def save(self,value,address):
        #print("value: " + str(value))
        #print("address: " + str(address))
        self.memory[address] = value

    def access(self,address):
        #print("access address: " + str(address))
        return self.memory[address]

mem = mem()