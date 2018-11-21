#import symbol_table as st 

class mem:
    
    #Size of the memory given to each of our lists
    memorySize = 100000

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
        print("In memory")
        print(data_type)
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
                print("guardando circle...")
                print("dir: "+ str(self.gcCont))
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
                # p
                return sumAddr < self.memorySize
            elif scope == "TEMP":
                sumAddr = sizeRequested + self.tiCont
                #
                return sumAddr < self.memorySize*7
            else :
                sumAddr = sizeRequested + self.liCont
                # 
                return sumAddr < self.memorySize*4
        elif data_type == "float" or data_type == 1 :
            if scope == "GLOBAL":
                sumAddr = sizeRequested + self.gfCont
                # pri
                return sumAddr < self.memorySize*2
            elif scope == "TEMP":
                sumAddr = sizeRequested + self.tfCont
                # p
                return sumAddr < self.memorySize*8
            else :
                sumAddr = sizeRequested + self.lfCont
                # pr
                return sumAddr < self.memorySize*5
        elif data_type == "bool" or data_type == 2 :
            if scope == "GLOBAL":
                sumAddr = sizeRequested + self.gbCont
                # pr
                return sumAddr < self.memorySize*3
            elif scope == "TEMP":
                sumAddr = sizeRequested + self.tbCont
                # prin
                return sumAddr < self.memorySize*9
            else :
                sumAddr = sizeRequested + self.lbCont
                # p
                return sumAddr < self.memorySize*6
        elif data_type == "parabola" :
            if scope == "GLOBAL":
                sumAddr = sizeRequested + self.gpCont
                # print(
                return sumAddr < self.memorySize*12
            elif scope == "TEMP":
                sumAddr = sizeRequested + self.tpCont
                # print("p
                return sumAddr < self.memorySize*20
            else :
                sumAddr = sizeRequested + self.lpCont
                # print
                return sumAddr < self.memorySize*16
        elif data_type == "ellipse" :
            if scope == "GLOBAL":
                sumAddr = sizeRequested + self.geCont
                # print
                return sumAddr < self.memorySize*13
            elif scope == "TEMP":
                sumAddr = sizeRequested + self.teCont
                # print("
                return sumAddr < self.memorySize*21
            else :
                sumAddr = sizeRequested + self.leCont
                # prin
                return sumAddr < self.memorySize*17
        elif data_type == "hyperbola" :
            if scope == "GLOBAL":
                sumAddr = sizeRequested + self.ghCont
                # print("
                return sumAddr < self.memorySize*14
            elif scope == "TEMP":
                sumAddr = sizeRequested + self.thCont
                # print("hy
                return sumAddr < self.memorySize*22
            else :
                sumAddr = sizeRequested + self.lhCont
                # print(
                return sumAddr < self.memorySize*18
        elif data_type == "circle" :
            if scope == "GLOBAL":
                sumAddr = sizeRequested + self.gcCont
                # prin
                return sumAddr < self.memorySize*15
            elif scope == "TEMP":
                sumAddr = sizeRequested + self.tcCont
                # print(
                return sumAddr < self.memorySize*23
            else :
                sumAddr = sizeRequested + self.lcCont
                # pri
                return sumAddr < self.memorySize*19
        else :
            print("jeje equis de")
    
    def nextAvail(self, data_type):
        if data_type == 0: #int
            self.tiCont += 1
            return self.tiCont - 1
        elif data_type == 1: #float
            self.tfCont += 1
            return self.tfCont - 1   
        elif data_type == 2: #bool
            self.tbCont += 1
            return self.tbCont - 1
        elif data_type == 3: #parabola
            self.tpCont += 1
            return self.tpCont - 1
        elif data_type == 4: #circle
            self.tcCont += 1
            return self.tcCont - 1
        elif data_type == 5: #ellipse
            self.teCont += 1
            return self.teCont - 1
        elif data_type == 6: #hyperbola
            self.thCont += 1
            return self.thCont - 1

    def save(self,value,address):
        #print("value: " + str(value))
        #print("address: " + str(address))
        self.memory[address] = value

    def access(self,address):
        # print("access address: " + str(address))
        return self.memory[address]

    def print(self):
        print("printing memory")
        cont = 0
        for x in self.memory:
            if x != None:
                print(str(cont) + ".- " + str(x))
            cont = cont + 1

mem = mem()