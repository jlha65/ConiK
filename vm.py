import math

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

from global_variables import gv
from mem import mem as memx
from semantics_cube import operators_dict, sem_cube, var_types_dict

#counter = 0
memory = memx

def run(quadList, symtab, mem) :                              
    # print("Now in the VM")
    memory = mem
    finished = False
    while not finished:
        if quadList[gv.counterVm][0] == 'GOTO':
            GOTO(quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == 'GOTOF':
            GOTOF(quadList[gv.counterVm][1], quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == 'GOTOV':
            GOTOV(quadList[gv.counterVm][1], quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == 'PRINT':
            PRINT(quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == 'ERA':
            ERA(quadList[gv.counterVm][1])
        elif quadList[gv.counterVm][0] == 'PARAM':
            PARAM(quadList[gv.counterVm][1],quadList[gv.counterVm][3],symtab)
        elif quadList[gv.counterVm][0] == 'GOSUB':
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
            VER(quadList[gv.counterVm][1],quadList[gv.counterVm][2],quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == 'PLOT':
            PLOT(quadList[gv.counterVm][1],quadList[gv.counterVm][2], symtab)
        elif quadList[gv.counterVm][0] == 'RETURN':
            RETURN(quadList[gv.counterVm][1],quadList[gv.counterVm][3])
        elif quadList[gv.counterVm][0] == 'END':
            finished = True
            #memory.print()
        gv.counterVm = gv.counterVm + 1

def GOTO(dir):
    gv.counterVm = dir - 1

def GOTOF(condition, dir):
    condition = memory.access(condition)
    if(not condition):
        gv.counterVm = dir - 1

def GOTOV(condition, dir):
    condition = memory.access(condition)
    if(condition):
        gv.counterVm = dir - 1

def ERA(mod):
    gv.nextModule = mod

def PARAM(value, paramNum, symtab):
    for x,y in symtab.SYM_TABLE[gv.nextModule].items():
        if x != "#type" and x != "#address":
            if y["#paramNum"] == paramNum:
                if isinstance(value,str):
                    if value[0] == '%':
                        value = getCons(value[1:])
                else:
                    value = memory.access(value)
                memory.save(value,y["#address"])
                return

def GOSUB(dir):
    gv.currentQuad.append(gv.counterVm)
    gv.counterVm = dir - 1

def ENDPROC():
    gv.counterVm = gv.currentQuad.pop()
    #print(gv.currentQuad)

def PRINT(a):
    if type(a) == str:
        print(a)
    else:
        print(memory.access(a))

# B = A    #if 10000 <= number <= 30000:
def EQUAL(a, b):
    aisNum = False
    if isinstance(a,str):
        if a[0] == '%':
            a = getCons(a[1:])
    else:
        a = memory.access(a)
        aisNum = True
    if isinstance(b,str):
        if b[0] == '%':
            b = getCons(b[1:])
    #else:
        #b = memory.access(b)
    if isinstance(a,str):
        if memory.memorySize*6 <= b < memory.memorySize*9:
            b = memory.access(b)
        memory.save(a,b)
    else:
        if memory.memorySize*6 <= b < memory.memorySize*9:
            memaux = memory.access(b)#arrays work thanks to this, don't delete
            if memaux == None:
                memaux = b
            #memaux = b
            if memory.memorySize*6 <= a < memory.memorySize*9:
                if not aisNum:
                    memory.save(memory.access(a),memaux)
                else:
                    memory.save(a,memaux)
            else :
                memory.save(a,memaux)
        elif memory.memorySize*6 <= a < memory.memorySize*9:
            if not aisNum:
                memaux = memory.access(a)
            else:
                memaux = a
            if memory.memorySize*6 <= b < memory.memorySize*9:
                memory.save(memaux,memory.access(b))
            else :
                memory.save(memaux,b)
        else:
            memory.save(a,b)

def RETURN(a, addressToReturn):
    if isinstance(a,str):
        if a[0] == '%':
            a = getCons(a[1:])
    else:
        a = memory.access(a)
    memory.save(a, addressToReturn)

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
    if isinstance(a,float) or isinstance(b, float):
        return a / b
    else:
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
    
    if isinstance(b,str):
        if b[0] == '%':
            b = getCons(b[1:])
    else:
        b = memory.access(b)
    
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
    return memory.access(memory.access(a))

def VER(a,x,b):
    if isinstance(x,int):
        #print(str(a) + " : " + str(b))
        if a < 0:
            raise Exception("ERROR: Negative array index")
        if a >= b:
            raise Exception("ERROR: Index out of bounds")
    elif memory.memorySize*6 <= a < memory.memorySize*9:
        #print(a)
        a = memory.access(a)
        #print(str(a) + " : " + str(b))
        if a < 0:
            #print(a)
            raise Exception("ERROR: Negative array index")
        if a >= b:
            raise Exception("ERROR: Index out of bounds")

#The plot operation code receives 
def PLOT(conicSection, color, symtab):
    #If no color is defined, then black is assigned
    if not isinstance(color, str):
        color = "black"
    id = symtab.get_var_name(conicSection)
    #Parabola plot, check if ID is in the memory ranges for parabola
    if memory.memorySize*11 <= conicSection < memory.memorySize*12 or memory.memorySize*15 <= conicSection < memory.memorySize*16:
        idScope = symtab.get_scope(conicSection)
        A = symtab.get_var_address(idScope,"#" + id + "A")
        B = symtab.get_var_address(idScope,"#" + id + "B")
        C = symtab.get_var_address(idScope,"#" + id + "C")

        A = memory.access(A)
        B = memory.access(B)
        C = memory.access(C)

        axes()
        parabola = createParabola(A, B, C, color)
    #Ellipse plot, check if ID is in the memory ranges for Ellipse
    elif memory.memorySize*12 <= conicSection < memory.memorySize*13 or memory.memorySize*16 <= conicSection < memory.memorySize*17:
        idScope = symtab.get_scope(conicSection)
        A = symtab.get_var_address(idScope,"#" + id + "A")
        B = symtab.get_var_address(idScope,"#" + id + "B")
        R = symtab.get_var_address(idScope,"#" + id + "R")

        A = memory.access(A)
        B = memory.access(B)
        R = memory.access(R)

        ellipse = createEllipse(A, B, R, color)
        axes()
        addPlot(ellipse)
    #Hyperbola plot, check if ID is in the memory ranges for Hyperbola
    elif memory.memorySize*13 <= conicSection < memory.memorySize*14 or memory.memorySize*17 <= conicSection < memory.memorySize*18:
        idScope = symtab.get_scope(conicSection)
        A = symtab.get_var_address(idScope,"#" + id + "A")
        B = symtab.get_var_address(idScope,"#" + id + "B")

        A = memory.access(A)
        B = memory.access(B)

        axes()
        hyperbola = createHyperbola(A, B, color)
    #Circle plot, check if ID is in the memory ranges for Circle
    elif memory.memorySize*14 <= conicSection < memory.memorySize*15 or memory.memorySize*18 <= conicSection < memory.memorySize*19:
        #The circle doesn't need the A and B values, just the R value for the radius.
        idScope = symtab.get_scope(conicSection)
        A = symtab.get_var_address(idScope,"#" + id + "A")
        B = symtab.get_var_address(idScope,"#" + id + "B")
        R = symtab.get_var_address(idScope,"#" + id + "R")

        A = memory.access(A)
        B = memory.access(B)
        R = memory.access(R)

        circle = createCircle(A, B, R, color)
        axes()
        addPlot(circle)
    #This shouldn't happen, since semantics validation for receiving a plottable conic section is done in the parser
    else:
        raise Exception("Fatal error, not a conic section")

#Creates an ellipse object using parameters and returns it, it doesn't show the graph yet
def createEllipse(A, B, R, color):
    ellipse = Ellipse(xy=(0,0), width = A, height = B, edgecolor = color, fc = "None")
    return ellipse

#Creates a circle object using radius parameter and returns it, it doesn't show the graph yet
def createCircle(A, B, R, color):
    R = math.sqrt(R)
    circle = plt.Circle((0, 0), R, edgecolor=color, fc = 'None')
    return circle

#Creates a parabola and plots it, since there's no "Figure" for it we must calculate it by hand
def createParabola(A, B, C, color):
    #Using code from https://mmas.github.io/conics-matplotlib, but modified for parabola general form usage
    mpl.rcParams['lines.color'] = 'k'
    mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color', ['k'])

    #This line is modifiable to change the range of the parabola plot.
    x = np.linspace(-90, 90, 400)
    y = np.linspace(-50, 50, 400)
    x, y = np.meshgrid(x, y)

    axes()
    plt.contour(x, y, (A*x**2 + B*x + C - y ), [0], colors=color)
    plt.show()

#Creates a hyperbola and plots it, since there's no "Figure" for it we must calculate it by hand
def createHyperbola(A, B, color):
    #From https://mmas.github.io/conics-matplotlib
    mpl.rcParams['lines.color'] = 'k'
    mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color', ['k'])

    #This line is modifiable to change the range of the hyperbola plot.
    x = np.linspace(-90, 90, 400)
    y = np.linspace(-50, 50, 400)
    x, y = np.meshgrid(x, y)

    axes()
    #Only one of A or B must be negative, we rely on semantics from parser for that
    #Draw hyperbola in standard position
    plt.contour(x, y,(x**2/A + y**2/B), [1], colors=color)
    plt.show()

#Used for circles and ellipses, this function adds the figure to the current plot and shows it.
def addPlot(patch):
	ax=plt.gca()
	ax.add_patch(patch)
    #Make it so the width of the window scales with the size of the figure.
	plt.axis('scaled')
	plt.show()

#Plot the origin axes, with a bit of transparency (alpha)
def axes():
        plt.axhline(0, alpha=.1)
        plt.axvline(0, alpha=.1)

#Receives a string with a number on it, and returns either its float value (if float) or int value
def getCons(x):
    if "." in x:
        return float(x)
    else:
        return int(x)
