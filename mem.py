#import symbol_table as st 

class mem:
    
    #Size of the memory given to each of our lists
    memorySize = 15000

    #Constructor
    def __init__(self) :
        self.globalInt = [None] * self.memorySize
        self.globalFloat = [None] * self.memorySize
        self.globalBool = [None] * self.memorySize
        self.localInt = [None] * self.memorySize
        self.localFloat = [None] * self.memorySize
        self.localBool = [None] * self.memorySize
        self.tempInt = [None] * self.memorySize
        self.tempFloat = [None] * self.memorySize
        self.tempBool = [None] * self.memorySize
        self.consInt = [None] * self.memorySize
        self.consFloat = [None] * self.memorySize

        self.giCont = 0
        self.gfCont = 0
        self.gbCont = 0
        self.liCont = 0
        self.lfCont = 0
        self.lbCont = 0
        self.tiCont = 0
        self.tfCont = 0
        self.tbCont = 0
        self.ciCont = 0
        self.cfCont = 0

    def add_var(self, data_type, value, size, scope) :
        if data_type == "int" :
            if scope == "GLOBAL":
                self.globalInt[self.giCont] = value
                self.giCont += size
                return self.giCont - size
            else :
                self.localInt[self.liCont] = value
                self.liCont += size
                return self.liCont - size
        elif data_type == "float" :
            if scope == "GLOBAL":
                self.globalFloat[self.gfCont] = value
                self.gfCont += size
                return self.gfCont - size
            else :
                self.localFloat[self.lfCont] = value
                self.lfCont += size
                return self.lfCont - size
        elif data_type == "bool" :
            if scope == "GLOBAL":
                self.globalBool[self.gbCont] = value
                self.gbCont += size
                return self.gbCont - size
            else :
                self.localBool[self.lbCont] = value
                self.lbCont += size
                return self.lbCont - size       

    def checkSizeAvail(self, sizeRequested, data_type, scope) :
        sumAddr = 0
        if data_type == "int" :
            if scope == "GLOBAL":
                sumAddr = sizeRequested + self.giCont
            else :
                sumAddr = sizeRequested + self.liCont
        elif data_type == "float" :
            if scope == "GLOBAL":
                sumAddr = sizeRequested + self.gfCont
            else :
                sumAddr = sizeRequested + self.lfCont
        elif data_type == "bool" :
            if scope == "GLOBAL":
                sumAddr = sizeRequested + self.gbCont
            else :
                sumAddr = sizeRequested + self.lbCont
        
        return sumAddr < self.memorySize                         

mem = mem()

mem.localInt[14000] = 2

print(mem.localInt[14000])
print(mem.localInt[0])