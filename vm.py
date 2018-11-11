counter = 1

def run(quadList, symtab) :
    print("Now in the VM")
    print(quadList)
    for x in quadList :
        if quadList[0] == 'GOTO':
            GOTO(quadList[3])
        elif quadList[0] == 'GOTOF':
            GOTOF(quadList[1], quadList[3])
        elif quadList[0] == 'GOTOV':
            GOTOF(quadList[1], quadList[3])
        elif quadList[0] == 'PRINT':
            PRINT(quadList[3])
        elif quadList[0] == '=':
            EQUAL(quadList[1], quadList[3])
        elif quadList[0] == '+': #TO DO: REPLACE TEMPS AND QUADLIST[X] WITH THE MEMORY VALUES
            temp = ADD(quadList[1], quadList[2])
        elif quadList[0] == '-':
            temp = SUBSTRACT(quadList[1], quadList[2])
        elif quadList[0] == '*':
            temp = MULTIPLY(quadList[1], quadList[2])
        elif quadList[0] == '/':
            temp = DIVIDE(quadList[1], quadList[2])
        elif quadList[0] == '>':
            temp = MORETHAN(quadList[1], quadList[2])
        elif quadList[0] == '<':
            temp = MULTIPLY(quadList[1], quadList[2])
        elif quadList[0] == '<>':
            temp = DIVIDE(quadList[1], quadList[2])
        elif quadList[0] == '==':
            temp = EQUALS(quadList[1], quadList[2])


def GOTO(dir):
    counter = dir

def GOTOF(condition, dir):
    if(not condition):
        counter = dir

def GOTOV(condition, dir):
    if(condition):
        counter = dir

def PRINT(a):
    print(a)

def EQUAL(a, b):
    b = a

def ADD(a, b):
    return a + b

def SUBSTRACT(a, b):
    return a - b

def MULTIPLY(a, b):
    return a * b

def DIVIDE(a, b):
    return a / b

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