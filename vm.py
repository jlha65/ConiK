from mem import mem as memx
from semantics_cube import sem_cube
from semantics_cube import operators_dict
from semantics_cube import var_types_dict
from global_variables import gv
#counter = 0
memorySize = 15000
memory = memx

def run(quadList, symtab, mem) :                              
    print("Now in the VM")
    memory = mem
    #print(quadList)
    finished = False
    while not finished:
        #print(str(gv.counterVm) + " " + quadList[gv.counterVm][0])
        if quadList[gv.counterVm][0] == 'GOTO':
            GOTO(quadList[gv.counterVm][3])
            # print(" Counter: " + str(gv.counterVm))
        elif quadList[gv.counterVm][0] == 'GOTOF':
            GOTOF(quadList[gv.counterVm][1], quadList[gv.counterVm][3])
            # print("Gotof goes to " + str(quadList[gv.counterVm][3]))
        elif quadList[gv.counterVm][0] == 'GOTOV':
            GOTOV(quadList[gv.counterVm][1], quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == 'PRINT':
            PRINT(quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == 'ERA':
            ERA(quadList[gv.counterVm][1])
        elif quadList[gv.counterVm][0] == 'PARAM':
            PARAM(quadList[gv.counterVm][1],quadList[gv.counterVm][3],symtab)
        elif quadList[gv.counterVm][0] == 'GOSUB':
            #print(symtab.SYM_TABLE[quadList[gv.counterVm][1]])
            GOSUB(quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == 'ENDPROC':
            ENDPROC()
        elif quadList[gv.counterVm][0] == '=':
            EQUAL(quadList[gv.counterVm][1], quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == '+': #TO DO: REPLACE TEMPS AND quadList[gv.counterVm][quadList[gv.counterVm]] WITH THE MEMORY VALUES
            memory.save(ADD(quadList[gv.counterVm][1], quadList[gv.counterVm][2]), quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == '-':
            memory.save(SUBSTRACT(quadList[gv.counterVm][1], quadList[gv.counterVm][2]), quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == '*':
            memory.save(MULTIPLY(quadList[gv.counterVm][1], quadList[gv.counterVm][2]), quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == '/':
            memory.save(DIVIDE(quadList[gv.counterVm][1], quadList[gv.counterVm][2]), quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == '>':
            memory.save(MORETHAN(quadList[gv.counterVm][1], quadList[gv.counterVm][2]),quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == '<':
            # print(quadList[gv.counterVm])
            memory.save(LESSTHAN(quadList[gv.counterVm][1], quadList[gv.counterVm][2]),quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == '<>':
            memory.save(NOTEQUAL(quadList[gv.counterVm][1], quadList[gv.counterVm][2]),quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == '==':
            memory.save(EQUALS(quadList[gv.counterVm][1], quadList[gv.counterVm][2]),quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == 'and':
            memory.save(AND(quadList[gv.counterVm][1], quadList[gv.counterVm][2]),quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == 'or':
            memory.save(OR(quadList[gv.counterVm][1], quadList[gv.counterVm][2]),quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == 'not':
            memory.save(NOT(quadList[gv.counterVm][1]),quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == 'ACC':
            memory.save(ACC(quadList[gv.counterVm][1]),quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == 'VER':
            VER(quadList[gv.counterVm][1],quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == 'END':
            finished = True
        gv.counterVm = gv.counterVm + 1
    print(memory.print())

def GOTO(dir):
    gv.counterVm = dir - 1

def GOTOF(condition, dir):
    condition = memory.access(condition)
    if(not condition):
        # print(" GOTOF Goes to: " + str(gv.counterVm))
        gv.counterVm = dir - 1

def GOTOV(condition, dir):
    condition = memory.access(condition)
    if(condition):
        gv.counterVm = dir - 1

def ERA(mod):
    gv.nextModule = mod
    #print("jeje no hay ERA we xdXdxD")

def PARAM(value, paramNum, symtab):
    for x,y in symtab.SYM_TABLE[gv.nextModule].items():
        #print(symtab.SYM_TABLE)
        #print(symtab.SYM_TABLE[gv.nextModule])
        #print(y)
        if y != "void":
            if y["#paramNum"] == paramNum:
                if isinstance(value,str):
                    if value[0] == '%':
                        value = getCons(value[1:])
                else:
                    value = memory.access(value)
                memory.save(value,y["#address"])
                return
                #return y["#address"]

def GOSUB(dir):
    gv.currentQuad.append(gv.counterVm)
    gv.counterVm = dir - 1

def ENDPROC():
    gv.counterVm = gv.currentQuad.pop()

def PRINT(a):
    if type(a) == str:
        print(a)
    else:
        print(memory.access(a))

# B = A    #if 10000 <= number <= 30000:
def EQUAL(a, b):
    #print(b)
    if isinstance(a,str):
        if a[0] == '%':
            a = getCons(a[1:])
    else:
        a = memory.access(a)
    if isinstance(b,str):
        if b[0] == '%':
            b = getCons(b[1:])
    #else:
        #b = memory.access(b)
    if memory.memorySize*6 <= b < memory.memorySize*9:
        #print("In equal left side, for arrays")
        memaux = memory.access(b)
        #print(memaux)
        if memory.memorySize*6 <= a < memory.memorySize*9:
            memory.save(memory.access(a),memaux)
            #print("saved1 "+str(memory.access(a))+" in "+str(memaux))
        else :
            memory.save(a,memaux)
            #print("saved2 "+str(a)+" in "+str(memaux))
    if memory.memorySize*6 <= a < memory.memorySize*9:
        #print("In equal left side, for arrays")
        memaux = memory.access(a)
        #print(memaux)
        if memory.memorySize*6 <= b < memory.memorySize*9:
            memory.save(memaux,memory.access(b))
            #print("saved3 "+str(memaux)+" in "+str(memory.access(b)))
        else :
            memory.save(memaux,b)
            #print("saved4 "+str(memaux)+" in "+str(b))
    else:
        #if isinstance(a,str):
            #if a[0] == '%':
                #a = getCons(a[1:])
        #else:
            #a = memory.access(a)
        # print("Er " + str(b) + " = " + str(a))
        memory.save(a,b)
        #print("saved "+str(a)+" in "+str(b))
        #print(str(b) + " = " + str(a))

    # memauxa = a
    # memauxb = b
    # if isinstance(a,str):
    #     if memauxa[0] == '%':
    #         memauxa = getCons(memauxa[1:])
    # else:
    #     if memory.memorySize*6 <= b < memory.memorySize*9:
    #         memauxb = memory.access(b)
    #     if memory.memorySize*6 <= a < memory.memorySize*9:
    #         memauxa = memory.access(a)
    #     memory.save(memauxa,memauxb)

def ADD(a, b):
    if isinstance(a,str):
        if a[0] == '%':
            a = getCons(a[1:])
    else:
        a = memory.access(a)
    
    if isinstance(b,str):
        if b[0] == '%':
            b = getCons(b[1:])
    else:
        b = memory.access(b)
    #print(str(a) + " + " + str(b))
    return a + b

def SUBSTRACT(a, b):
    if isinstance(a,str):
        if a[0] == '%':
            a = getCons(a[1:])
    else:
        a = memory.access(a)
    
    if isinstance(b,str):
        if b[0] == '%':
            b = getCons(b[1:])
    else:
        b = memory.access(b)
    #print(str(a) + " - " + str(b))
    return a - b

def MULTIPLY(a, b):
    if isinstance(a,str):
        if a[0] == '%':
            a = getCons(a[1:])
    else:
        a = memory.access(a)
    
    if isinstance(b,str):
        if b[0] == '%':
            b = getCons(b[1:])
    else:
        b = memory.access(b)
    #print(str(a) + " * " + str(b))
    return a * b

def DIVIDE(a, b):
    if isinstance(a,str):
        if a[0] == '%':
            a = getCons(a[1:])
    else:
        a = memory.access(a)
    
    if isinstance(b,str):
        if b[0] == '%':
            b = getCons(b[1:])
    else:
        b = memory.access(b)
    #print(str(a) + " / " + str(b))
    if isinstance(a,float) or isinstance(b, float):
        #print(a/b)
        return a / b
    else:
        #print(a//b)
        return a//b

def MORETHAN(a, b):
    if isinstance(a,str):
        if a[0] == '%':
            a = getCons(a[1:])
    else:
        a = memory.access(a)
    
    if isinstance(b,str):
        if b[0] == '%':
            b = getCons(b[1:])
    else:
        b = memory.access(b)
        
    return a > b

def LESSTHAN(a, b):
    if isinstance(a,str):
        if a[0] == '%':
            a = getCons(a[1:])
    else:
        a = memory.access(a)
        #print("aqui deberia salir la i: " + str(a))
    
    if isinstance(b,str):
        if b[0] == '%':
            b = getCons(b[1:])
    else:
        b = memory.access(b)
    #print(str(a) + " < " + str(b))
    # print(a<b)
    
    return a<b

def NOTEQUAL(a, b):
    if isinstance(a,str):
        if a[0] == '%':
            a = getCons(a[1:])
    else:
        a = memory.access(a)
    
    if isinstance(b,str):
        if b[0] == '%':
            b = getCons(b[1:])
    else:
        b = memory.access(b)
        
    return a != b

def EQUALS(a, b):
    if isinstance(a,str):
        if a[0] == '%':
            a = getCons(a[1:])
    else:
        a = memory.access(a)
    
    if isinstance(b,str):
        if b[0] == '%':
            b = getCons(b[1:])
    else:
        b = memory.access(b)
        
    return a == b

def AND(a, b):
    #checks if a and b are constant True or False values
    if isinstance(a,str):
        a = a == "true"
    if isinstance(b,str):
        b = b == "true"

    # If they were not constant, then they are variables 
    # So, we access the memory values for them.
    if not isinstance(a,bool):
        a = memory.access(a)
    if not isinstance(b,bool):
        b = memory.access(b)      
        
    return a and b

def OR(a, b):
    #checks if a and b are constant True or False values
    if isinstance(a,str):
        a = a == "true"
    if isinstance(b,str):
        b = b == "true"

    # If they were not constant, then they are variables
    # So, we access the memory values for them.
    if not isinstance(a,bool):
        a = memory.access(a)
    if not isinstance(b,bool):
        b = memory.access(b)
        
    return a or b

def NOT(a):
    #checks if A is constant True or False value
    if isinstance(a,str):
        a = a == "true"
    # If it wasn't a constant, then it is a variable
    # So, we access the memory value for it.
    if not isinstance(a,bool):
        a = memory.access(a)

    return not a

def ACC(a):
    #print("ACC"+str(a)+":")
    #print(memory.access(memory.access(a)))
    return memory.access(memory.access(a))

def VER(a,b):
    if memory.memorySize*6 <= a < memory.memorySize*9:
        a = memory.access(a)
    if a < 0:
        raise Exception("ERROR: Negative array index")
    if a >= b:
        raise Exception("ERROR: Index out of bounds")

def getCons(x):
    if "." in x:
        return float(x)
    else:
        return int(x)