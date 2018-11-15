from mem import mem as memx
from semantics_cube import sem_cube
from semantics_cube import operators_dict
from semantics_cube import var_types_dict
counter = 1
memorySize = 15000
memory = memx

def run(quadList, symtab, mem) :
    print("Now in the VM")
    memory = mem
    #print(quadList)
    for x in quadList :
        if x[0] == 'GOTO':
            GOTO(x[3])
        elif x[0] == 'GOTOF':
            GOTOF(x[1], x[3])
        elif x[0] == 'GOTOV':
            GOTOV(x[1], x[3])
        elif x[0] == 'PRINT':
            PRINT(x[3])
        elif x[0] == '=':
            EQUAL(x[1], x[3])
        elif x[0] == '+': #TO DO: REPLACE TEMPS AND x[X] WITH THE MEMORY VALUES
            memory.save(ADD(x[1], x[2]), x[3])
        elif x[0] == '-':
            memory.save(SUBSTRACT(x[1], x[2]), x[3])
        elif x[0] == '*':
            memory.save(MULTIPLY(x[1], x[2]), x[3])
        elif x[0] == '/':
            memory.save(DIVIDE(x[1], x[2]), x[3])
        elif x[0] == '>':
            temp = MORETHAN(x[1], x[2])
        elif x[0] == '<':
            temp = LESSTHAN(x[1], x[2])
        elif x[0] == '<>':
            temp = NOTEQUAL(x[1], x[2])
        elif x[0] == '==':
            temp = EQUALS(x[1], x[2])


def GOTO(dir):
    counter = dir

def GOTOF(condition, dir):
    if(not condition):
        counter = dir

def GOTOV(condition, dir):
    if(condition):
        counter = dir

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
    #print(str(b) + " = " + str(a))
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
    if(a > b):
        return True
    return False

def LESSTHAN(a, b):
    if(a < b):
        return True
    return False

def NOTEQUAL(a, b):
    if(a != b):
        return True
    return False

def EQUALS(a, b):
    if(a == b):
        return True
    return False

def getCons(x):
    if "." in x:
        return float(x)
    else:
        return int(x)