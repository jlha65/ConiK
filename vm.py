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
        print(str(gv.counterVm) + quadList[gv.counterVm][0])
        if quadList[gv.counterVm][0] == 'GOTO':
            GOTO(quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == 'GOTOF':
            GOTOF(quadList[gv.counterVm][1], quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == 'GOTOV':
            GOTOV(quadList[gv.counterVm][1], quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == 'PRINT':
            PRINT(quadList[gv.counterVm][3])
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
            print(quadList[gv.counterVm])
            memory.save(LESSTHAN(quadList[gv.counterVm][1], quadList[gv.counterVm][2]),quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == '<>':
            memory.save(NOTEQUAL(quadList[gv.counterVm][1], quadList[gv.counterVm][2]),quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == '==':
            memory.save(EQUALS(quadList[gv.counterVm][1], quadList[gv.counterVm][2]),quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == 'END':
            finished = True
        gv.counterVm = gv.counterVm + 1

    # for x in quadList :
    #     if x[0] == 'GOTO':
    #         GOTO(x[3])
    #     elif x[0] == 'GOTOF':
    #         GOTOF(x[1], x[3])
    #     elif x[0] == 'GOTOV':
    #         GOTOV(x[1], x[3])
    #     elif x[0] == 'PRINT':
    #         PRINT(x[3])
    #     elif x[0] == '=':
    #         EQUAL(x[1], x[3])
    #     elif x[0] == '+': #TO DO: REPLACE TEMPS AND x[X] WITH THE MEMORY VALUES
    #         memory.save(ADD(x[1], x[2]), x[3])
    #     elif x[0] == '-':
    #         memory.save(SUBSTRACT(x[1], x[2]), x[3])
    #     elif x[0] == '*':
    #         memory.save(MULTIPLY(x[1], x[2]), x[3])
    #     elif x[0] == '/':
    #         memory.save(DIVIDE(x[1], x[2]), x[3])
    #     elif x[0] == '>':
    #         temp = MORETHAN(x[1], x[2])
    #     elif x[0] == '<':
    #         temp = LESSTHAN(x[1], x[2])
    #     elif x[0] == '<>':
    #         temp = NOTEQUAL(x[1], x[2])
    #     elif x[0] == '==':
    #         temp = EQUALS(x[1], x[2])


def GOTO(dir):
    gv.counterVm = dir - 1

def GOTOF(condition, dir):
    if(not condition):
        gv.counterVm = dir - 1

def GOTOV(condition, dir):
    if(condition):
        gv.counterVm = dir - 1

def PRINT(a):
    if type(a) == str:
        print(a)
    else:
        print(memory.access(a))

def EQUAL(a, b):
    if isinstance(a,str):
        if a[0] == '%':
            a = getCons(a[1:])
    else:
        a = memory.access(a)
    print("Er " + str(b) + " = " + str(a))
    memory.save(a,b)
    #print(str(b) + " = " + str(a))

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
    print(str(a) + " < " + str(b))
    return a < b

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

def getCons(x):
    if "." in x:
        return float(x)
    else:
        return int(x)