import symbol_table as st 

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

    def add_var(self, data_type, size) :
        if data_type == "int" :
            print("jeje xd")

mem = mem()

mem.localInt[14000] = 2

print(mem.localInt[14000])
print(mem.localInt[0])