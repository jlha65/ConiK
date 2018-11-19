reserved = {
    'int' : 'INT_KEYWORD',
    'float' : 'FLOAT_KEYWORD',
    'var' : 'VAR_KEYWORD',
    'parabola' : 'PARABOLA_KEYWORD',
    'ellipse' : 'ELLIPSE_KEYWORD',
    'area' : 'AREA_KEYWORD',
    'bool' : 'BOOL_KEYWORD',
    'hyperbola' : 'HYPERBOLA_KEYWORD',
    'circle' : 'CIRCLE_KEYWORD',
    'plot' : 'PLOT_KEYWORD',
    'if' : 'IF_STATEMENT',
    'else' : 'ELSE_STATEMENT',
    'proc' : 'PROC_KEYWORD',
    'perimeter' : 'PERIMETER_KEYWORD',
    'true' : 'TRUE_KEYWORD',
    'focus' : 'FOCUS_KEYWORD',
    'axis' : 'AXIS_KEYWORD',
    'center' : 'CENTER_KEYWORD',
    'pi' : 'PI_KEYWORD',
    'for' : 'FOR_LOOP_KEYWORD',
    'false' : 'FALSE_KEYWORD',
    'euler' : 'EULER_KEYWORD',
    'vertex' : 'VERTEX_KEYWORD',
    'radius' : 'RADIUS_KEYWORD',
    'standard' : 'STANDARD_KEYWORD',
    'general' : 'GENERAL_KEYWORD',
    'while' : 'WHILE_LOOP_KEYWORD',
    'exc' : 'EXC_KEYWORD',
	'red' : 'RED_KEYWORD',
	'orange' : 'ORANGE_KEYWORD',
	'yellow' : 'YELLOW_KEYWORD',
	'green' : 'GREEN_KEYWORD',
	'blue' : 'BLUE_KEYWORD',
	'purple' : 'PURPLE_KEYWORD',
	'reflection' : 'REFLECTION_KEYWORD',
	'translate' : 'TRANS_KEYWORD',
	'rotation' : 'ROTATION_KEYWORD',
	'stretch' : 'STRETCH_KEYWORD',
    'and' : 'AND_KEYWORD',
    'or' : 'OR_KEYWORD',
    'not' : 'NOT_KEYWORD',
    #Not in the official document (yet) :
    'print' : 'PRINT_KEYWORD',
    'program' : 'PROGRAM_KEYWORD',
    'x' : 'X_KEYWORD',
    'y' : 'Y_KEYWORD',
    '&' : 'POWER'
}
        #New tokens:
tokens = ['ID', 'EQPARABOLA', 'EQCIRCLE', 'EQELLIPSE', 'EQHYPERBOLA', 'CONS_STRING', 'CONS_INT', 
        'CONS_FLOAT', 'CONS_BOOL', 'RELOP', 'AND', 'OR', 'NOT',
        #Old tokens:
        'OPEN_BRACKET','CLOSE_BRACKET','OPEN_SQUARE_BRACKET','CLOSE_SQUARE_BRACKET', 'COMMA', 'POINT', 'PLUSOP', 'MINUSOP',
        'TIMESOP', 'DIVIDEOP', 'OPEN_PARENTHESES', 'CLOSE_PARENTHESES',
        'ARROW','TWO_POINTS', 'SEMICOLON', 'EQUALOP', 'CTE_I', 'CTE_F', 'STRING'] + list(reserved.values())
#New tokens:
#t_ID = r'[a-zA-Z_][a-zA-Z0-9]*' #Not needed since it's already been made below for LittleDuck
# t_EQPARABOLA = r'\s*y\s*\=\s*[\-]?[0-9]+(\.[0-9]+)?\s*x\s*\^\s*2\s*[+-]\s*([0-9]+(\.[0-9]+)?\s*)x\s*[-+]\s*([0-9]+(\.[0-9]+)?\s*)'
# def t_EQCIRCLE(t):
#     r'\s*x\s*\^\s*2\s*\+\s*y\s*\^\s*2\s*\=\s*([0-9]+(\.[0-9]+)?\s*)\s*\;'
#t_EQCIRCLE = r'\".*\"'
# t_EQELLIPSE = r'\s*x\s*\^\s*2\s*\/\s*([0-9]+(\.[0-9]+)?\s*)\+\s*y\s*\^\s*2\s*\/\s*([0-9]+(\.[0-9]+)?\s*)\=\s*1\s*'
# t_EQHYPERBOLA = r'\s*x\s*\^\s*2\s*\/\s*([0-9]+(\.[0-9]+)?\s*)\-\s*y\s*\^\s*2\s*\/\s*([0-9]+(\.[0-9]+)?\s*)\=\s*1\s*'
t_CONS_STRING = r'\".*\"'
t_CONS_INT = r'[0-9]+'
t_CONS_FLOAT = r'[0-9]+\.[0-9]+'
#t_CONS_BOOL = r'true | false'
#t_RELOP = r'' #Not needed since it's already been made below for LittleDuck

# def t_EQUALS(t):
#     r'=='

#Old tokens:
t_OPEN_BRACKET = r'\{'
t_CLOSE_BRACKET = r'\}'
t_OPEN_SQUARE_BRACKET = r'\['
t_CLOSE_SQUARE_BRACKET = r'\]'
t_COMMA = r'\,'
t_POINT = r'\.'
t_PLUSOP = r'\+'
t_MINUSOP = r'\-'
t_TIMESOP = r'\*'
t_DIVIDEOP = r'/'
t_OPEN_PARENTHESES = r'\('
t_CLOSE_PARENTHESES = r'\)'
t_ARROW = r'\~'#flechita
t_TWO_POINTS = r':'
t_SEMICOLON = r';'
t_EQUALOP = r'='
t_RELOP = r'<(>)? | > | =='
# t_NOT = r'\!'
# t_AND = r'\&'
# t_OR = r'\|'

#t_CTE_I = r'[0-9]+' #This was commented out since it is replaced by CONS_INT
#t_CTE_F = r'[0-9]+\.[0-9]+' #This was commented out since it is replaced by CONS_FLOAT
#t_STRING = r'\".*\"' #This was commented out since it is replaced by CONS_STRING

t_ignore = " \t" #Ignore whitespace

t_ignore_COMMENT = r'\#.*' #Ignore comments

def t_ID(t):
    r'[A-Za-z]([A-Za-z]|[0-9])*'
    t.type = reserved.get(t.value, 'ID')
    #print(t)
    if t.type == 'ID':
        gv.currentId = t.value
    else:
        gv.currentId = ''
    return t
#def t_PARABOLA_KEYWORD(t):
    #r'parabola'
    #return t


#Counter for lines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

#If error, print character that is the problem
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()



#Grammar and parsing
import symbol_table as symtab
from mem import mem #memory
import vm
import re #Regular expressions
from global_variables import gv
from semantics_cube import sem_cube
from semantics_cube import operators_dict
from semantics_cube import var_types_dict

#from collections import deque
#queue = deque([])

typeStack = []
scopeStack = []
PilaOp = []#Pila de operandos
PTypes = []#Pila de tipos
POper = []#Pila de operadores
PJumps = []#Pila de saltos
listPendingQuads = [] #lista de listas de cuadruplos que faltan
PModDataTypes = [] #pila de tipos de dato de declaraciones de modulos
temporal_mem = []
PAssign = [] #pila donde se guarda lo de arreglos del lado izquierdo

#cuScope = "GLOBAL"

def p_PROGRAM(t):
    'PROGRAM : goto_main PROGRAM_KEYWORD ID SEMICOLON A'
    gv.currentId = t[2] # guarda nombre del programa
    gv.currentType = "PROGRAM" # tipo de dato "PROGRAM"
    symtab.add_variable("GLOBAL",gv.currentId,gv.currentType,None,None)
    quad = ["END",[],[],[]]
    gv.quadList.append(quad)
    gv.quadCount += 1
    #print("program name: " + gv.currentId)
    #print("data type: " + gv.currentType)
    # print("current scope: " + gv.currentScope)
    # print(symtab.SYM_TABLE)
    # print (PilaOp)
    # print (PTypes)
    # print (POper)
    #print (gv.quadList)
    cont=0
    for x in gv.quadList:
        print(str(cont) + ".- " + str(x))
        cont = cont + 1
    #print(mem.globalInt)
    # print (gv.quadList[0])
    # print (gv.quadCount)
    # print (len(gv.quadList))
    vm.run(gv.quadList, symtab, mem)

def p_TYPE_S(t):
    '''TYPE_S : PARABOLA_KEYWORD
            | ELLIPSE_KEYWORD
			| HYPERBOLA_KEYWORD
			| CIRCLE_KEYWORD'''
    #gv.currentType = t[1] # tipo de dato
    #print("data type: " + gv.currentType)
    #print("data type: " + t[1])
    typeStack.append(t[1])
    gv.currentType = t[1]
    return t[1]
			
def p_TYPE_P(t):
    '''TYPE_P : INT_KEYWORD
            | FLOAT_KEYWORD
    		| BOOL_KEYWORD'''
    #print("data type: " + t[1])
    typeStack.append(t[1])
    gv.currentType = t[1]
    return t[1]
	
# def p_set_type(t):
    # 'set_type : '
	# gv.currentType = t[-1]

def p_A(t): 
    '''A : VARS B
            | B'''

def p_B(t):
    '''B : MODULE B
            | fill_main BLOCK'''


def p_goto_main(t):
    'goto_main : '
    quad = ['GOTO', [], [], -1]
    gv.quadList.append(quad)
    gv.quadCount += 1

def p_fill_main(t):
    'fill_main :'
    gv.quadList[0][3] = gv.quadCount
    
# def p_VARS(t):
#     'VARS : VAR_KEYWORD C'

def p_VARS(t):
    '''VARS : VAR_KEYWORD V'''

def p_V(t):
    '''V : TYPE_P C
            | TYPE_S C '''
    #gv.currentType = t[1] # tipo de dato
    #print(t[1])

def p_C(t):  
    '''C : ID add_variable D
            | ID OPEN_SQUARE_BRACKET EXP CLOSE_SQUARE_BRACKET add_variableArr D
			| ID OPEN_SQUARE_BRACKET EXP CLOSE_SQUARE_BRACKET OPEN_SQUARE_BRACKET EXP CLOSE_SQUARE_BRACKET add_variableArr2 D'''
    #gv.currentType = typeStack.pop() # tipo de dato
    #gv.currentId = t[1]#guarda nombre de variable
    #symtab.add_variable(gv.currentScope,gv.currentId,gv.currentType)
    #####symtab.add_variable(cuScope,gv.currentId,gv.currentType)
    #print("var name: " + gv.currentId)
    #print("scope   : " + gv.currentScope)
			
def p_add_variable(t):
    'add_variable :'
    #gv.currentType = typeStack.pop() # tipo de dato
    size = 1
    # print("Adding var to symtab")
    # print(gv.currentType, gv.currentScope)
    if mem.checkSizeAvail(size, gv.currentType, gv.currentScope) :
        memAddress = mem.add_var(gv.currentType, None, size, gv.currentScope)
        # print("Added var to memory")
        symtab.add_variable(gv.currentScope,gv.currentId,gv.currentType, size, memAddress)
        #print("Linked var memory to var table, its memory is: ")
        #print(memAddress)
    else :
        raise Exception("Memory size exceeded in variables declaration")
    #symtab.add_variable(cuScope,gv.currentId,gv.currentType)
    #####print("var name: " + gv.currentId)
    #####print("scope   : " + gv.currentScope)

def getCons(x):
    if "." in x:
        return float(x)
    else:
        return int(x)

def p_add_variableArr(t):
    'add_variableArr :'
    #size = int(t[-2])
    size = PilaOp.pop()
    if isinstance(size,str):
        if size[0] == '%':
            size = getCons(size[1:])
            print("size: " + str(size))

    #print(size)
    PTypes.pop()
    if mem.checkSizeAvail(size, gv.currentType, gv.currentScope) :
        memAddress = mem.add_var(gv.currentType, None, size, gv.currentScope)    
        symtab.add_variable(gv.currentScope,gv.currentId,gv.currentType, size, memAddress)
    else :
        raise Exception("Memory size exceeded in variables declaration (1D ARRAY SIZE)")
    
def p_add_variableArr2(t):
    'add_variableArr2 :'
    a = PilaOp.pop()
    b = PilaOp.pop()

    PTypes.pop()
    PTypes.pop()

    if isinstance(a,str):
        if a[0] == '%':
            a = getCons(a[1:])
            print("a: " + str(a))
    if isinstance(b,str):
        if b[0] == '%':
            b = getCons(b[1:])
            print("b: " + str(b))

    size = a * b

    if mem.checkSizeAvail(size, gv.currentType, gv.currentScope) :
        memAddress = mem.add_var(gv.currentType, None, size, gv.currentScope)
        symtab.add_variable(gv.currentScope,gv.currentId,gv.currentType, size, memAddress)
        symtab.add_dims(gv.currentScope,gv.currentId,b,a)
    else :
        raise Exception("Memory size exceeded in variables declaration (2D ARRAY SIZE)")


def p_D(t):
    '''D : COMMA C
            | SEMICOLON V
            | SEMICOLON termina_sym'''
			
def p_termina_sym(t):
    'termina_sym :'
    #print("termina sym")
    #print(symtab.SYM_TABLE)
			
# def p_E(t):
#     '''E : TYPE_P F
#             | TYPE_S F'''
			
# def p_F(t):
#     '''F : SEMICOLON C
#             | SEMICOLON'''

def p_BLOCK(t):
    'BLOCK : OPEN_BRACKET G'
	
def p_G(t):
    '''G : STATEMENT G
            | CLOSE_BRACKET'''
			
def p_STATEMENT(t):
    '''STATEMENT : EXPRESSION_OP
            | ASSIGN
			| WRITE
			| FOR_LOOP
			| WHILE_LOOP
			| CONDITION
            | PROC_CALL
            | F_CALL'''

def p_PROC_CALL(t):
    '''PROC_CALL : PROC_KEYWORD ID modCall_paso1 modCall_paso2 OPEN_PARENTHESES V1 '''
    print("PROC_CALL")

def p_V1(t):
    '''V1 : EXP modCall_paso3 W1
            | EXP modCall_paso3 COMMA modCall_paso4 V1
            | W1'''

def p_W1(t):
    '''W1 : modCall_paso5 CLOSE_PARENTHESES SEMICOLON modCall_paso6'''
    #print("CACA")

			
def p_ASSIGN(t):
    '''ASSIGN : ID ASSIGN0D EQUALOP EXPRESSION SEMICOLON
                | ID ASSIGNCS ARROW CONS_STRING ASSIGN_S SEMICOLON
                | ID OPEN_SQUARE_BRACKET EXP CLOSE_SQUARE_BRACKET ASSIGN1D EQUALOP EXPRESSION SEMICOLON
                | ID OPEN_SQUARE_BRACKET EXP CLOSE_SQUARE_BRACKET OPEN_SQUARE_BRACKET EXP CLOSE_SQUARE_BRACKET ASSIGN2D EQUALOP EXPRESSION SEMICOLON'''
    # ID ARROW EQUATION
    #result_Type = sem_cube[operators_dict[operator]][var_types_dict[left_type]][var_types_dict[right_type]]
    #print(t[1])
    lastType = PTypes.pop() #Get the type of the id (on the right side of the assign)
    result_Type = sem_cube[operators_dict["="]][var_types_dict[symtab.get_return_type(gv.currentScope,t[1])]][var_types_dict[lastType]] #Check if the assign is valid
    if result_Type != -1 :
        #address = symtab.get_var_address(gv.currentScope,t[1])
        print("IDDDDDDDDD:")
        print(gv.currentArrAddressL)
        #quad = ["=",PilaOp.pop(),[],gv.currentArrAddressL]
        if not PAssign:
            quad = ["=",PilaOp.pop(),[],gv.currentArrAddressL]
        else:
            quad = ["=",PilaOp.pop(),[],PAssign.pop()]
        #quad = ["=",PilaOp.pop(),[],t[1]]
        gv.quadList.append(quad)
        gv.quadCount = gv.quadCount + 1
    else:
        #print("Incompatible types for assign")
        raise Exception("Incompatible types " + lastType + " assigned to " + symtab.get_return_type(gv.currentScope,t[1]))

# def p_STRINGTYPE(t):
#     'STRINGTYPE :'
#     print(t[-1])
#     PTypes.append("string")

def p_ASSIGNCS(t):
    'ASSIGNCS :'
    PTypes.append(symtab.get_return_type(gv.currentScope,gv.currentId))
    gv.currentArrAddressL = symtab.get_var_address(gv.currentScope,t[-1])

def p_ASSIGN_S(t):
    'ASSIGN_S :'
    #print(t[-1])
    #Only for circles, in the future must check for other equations
    if verifyEquationCircle(t[-1]):
        PilaOp.append(t[-1])
    else:
        raise Exception("Error: invalid circle syntax")
    
def verifyEquationCircle(equation):
    #equation = equation.replace(" ", "")
    print(equation)
    #A*X^2 + B*Y^2 = R
    #Where A=B
    equation = equation[1:-1]
    print(equation)
    if re.match(r'\s*x\s*\^\s*2\s*\+\s*y\s*\^\s*2\s*\=\s*([0-9]+(\.[0-9]+)?\s*)\s*', equation):
        return True
    else:
        return False
    # A=""
    # B=""
    # R=""
    # i = 0
    # j = 0
    # flagA = False
    # flagB = False
    # for x in equation:
    #     if x == "X" or x == "x" and not flagA:
    #         A= equation[:i]
    #         j = i+4 #save position for next substring (B)
    #         flagA = True
    #         if equation[i] != "^" or equation[i+1] != "2":
    #             return False
    #     elif if x == "Y" or x == "y" and not flagB:
    #     i = i + 1

def p_ASSIGN0D(t):
    'ASSIGN0D :'
    gv.currentArrAddressL = symtab.get_var_address(gv.currentScope,t[-1])

def p_ASSIGN1D(t):
    'ASSIGN1D :'
    #print(t[-4])
    gv.currentArrAddressL = symtab.get_var_address(gv.currentScope,t[-4])
    print("KYC VIEJO LESBIANO")
    print(gv.currentArrAddressL)
    #print(gv.currentArrAddress)
    #symtab.get_var_address(gv.currentScope,t[-1])
    #print("arr1d " + str(gv.currentArrAddress))
    pos = PilaOp.pop()
    posType = PTypes.pop()
    print(pos)
    #PTypes.append(tipo)#regresar el tipo a la pila
    if posType == "int":
        # if isinstance(pos,str):
        #     if pos[0] == '%':
        #         pos = getCons(pos[1:])
        #         print("pos: " + str(pos))
        print("pos: " + str(pos))
        #gv.currentArrAddressL = gv.currentArrAddressL + pos
        print("CurrentArrAddressL : ")
        print(gv.currentArrAddressL)
    else:
        raise Exception("Array Index must be an integer")

    if gv.currentArrAddress < mem.memorySize or mem.memorySize*3 <= gv.currentArrAddress < mem.memorySize*4 or mem.memorySize*6 <= gv.currentArrAddress < mem.memorySize*7:
        rType = "int"
    elif mem.memorySize <= gv.currentArrAddress < mem.memorySize*2 or mem.memorySize*4 <= gv.currentArrAddress < mem.memorySize*5 or mem.memorySize*7 <= gv.currentArrAddress < mem.memorySize*8:
        rType = "float"
    elif mem.memorySize*2 <= gv.currentArrAddress < mem.memorySize*3 or mem.memorySize*5 <= gv.currentArrAddress < mem.memorySize*6 or mem.memorySize*8 <= gv.currentArrAddress < mem.memorySize*9:
        rType = "bool"
    result_Type = sem_cube[operators_dict["+"]][var_types_dict[posType]][var_types_dict[rType]]
    #Create a new temp variable for use in the '+' quad just below
    if mem.checkSizeAvail(1, result_Type, "TEMP"):
        result = mem.nextAvail(result_Type)
    else:
        raise Exception("Ran out of memory")

    #Create '+' quad for the BaseDir of Array + index of array
    #quad = ["+","%" + str(gv.currentArrAddressL),pos,result]
    quad = ["+","%" + str(gv.currentArrAddressL),pos,result]

    #Add the '+' quad to quadlist
    gv.quadList.append(quad)
    gv.quadCount += 1

    PAssign.append(result)

    # #Create another temp variable for use in the 'ACC' quad
    # if mem.checkSizeAvail(1, "int", "TEMP"):
    #     result2 = mem.nextAvail("int")
    # else:
    #     raise Exception("Ran out of memory")
    # #Now we generate the ACC quad, which will carry the result of the array access
    # quad2 = ["ACC", result,[],result2]

    # #Add the 'ACC' quad to quadlist
    # gv.quadList.append(quad)
    # gv.quadCount += 1

    #Finally assign the temporal variable that has the array access
    
    ############################################################################
    # result_Type = sem_cube[operators_dict["+"]][var_types_dict[posType]][var_types_dict["int"]]
    # if mem.checkSizeAvail(1, result_Type, "TEMP"):
    #     result = mem.nextAvail(result_Type)
    #     #print("simon wey " + str(result))
    # else:
    #     raise Exception("Ran out of memory")
    # #address1
    # left_op = "%" + str(gv.currentArrAddress)
    # # right_op = "%" + str(pos)
    # quad = ["+",left_op,pos,result]
    # gv.quadList.append(quad)
    # gv.quadCount = gv.quadCount + 1#incrmenta cuenta de cuadruplos
    # # if mem.checkSizeAvail(1, result_Type, "TEMP"):
    # #     result2 = mem.nextAvail(result_Type)
    # #     #print("simon wey " + str(result))
    # # else:
    # #     raise Exception("Ran out of memory")
    
    # #quad = ["ACC",result,[],result2]#Acceso a valor en result (result es una direccion)
    # #print(gv.currentArrAddress, mem.access(pos))
    # print(gv.currentArrAddress)
    # result2 = gv.currentArrAddress# + mem.access(pos)
    # quad = ["ACC",result,[],result2] #Acceso a valor en result (result es una direccion)
    # gv.quadList.append(quad)
    # gv.quadCount = gv.quadCount + 1#incrmenta cuenta de cuadruplos

    # PilaOp.append(result2)
    # #PTypes.append(result_Type)
    # if result_Type == 0:
    #     PTypes.append("int")
    # elif result_Type == 1:
    #     PTypes.append("float")
    # elif result_Type == 2:
    #     PTypes.append("bool")
    # #print("appendeando en arrCall: "+str(gv.currentArrAddress+pos))
    # #pos = mem.access(pos)
    # #PilaOp.append(pos)
    # #PilaOp.append(gv.currentArrAddress+pos)
    # #PilaOp.append(pos)
    # #PTypes.pop()
    # quad = ["VER",pos,[],symtab.get_size(gv.currentScope,t[-4])]
    # gv.quadList.append(quad)
    # gv.quadCount = gv.quadCount + 1#incrmenta cuenta de cuadruplos
    ############################################################################

def p_ASSIGN2D(t):
    'ASSIGN2D :'
    gv.currentArrAddressL = symtab.get_var_address(gv.currentScope,gv.currentId)
    #symtab.get_var_address(gv.currentScope,t[-1])
    #print("arr1d " + str(gv.currentArrAddress))
    index2 = PilaOp.pop()
    index1 = PilaOp.pop()
    tipo2 = PTypes.pop()
    tipo1 = PTypes.pop()
    #PTypes.append(tipo)#regresar el tipo a la pila
    if tipo1 == "int":
        if isinstance(index1,str):
            if index1[0] == '%':
                index1 = getCons(index1[1:])
                print("index1: " + str(index1))
    else:
        raise Exception("Array Index must be an integer")
    if tipo2 == "int":
        if isinstance(index2,str):
            if index2[0] == '%':
                index2 = getCons(index2[1:])
                print("index2: " + str(index2))
    else:
        raise Exception("Array Index must be an integer")

    gv.currentArrAddressL = gv.currentArrAddressL + index1*symtab.get_dims2(gv.currentScope,gv.currentId) + index2
    print("address d2: " + str(gv.currentArrAddressL))

def p_EQUATION(t):
    '''EQUATION : EQPARABOLA
			| X_KEYWORD EQUATION_N1 POWER CONS_INT PLUSOP Y_KEYWORD POWER CONS_INT EQUALOP CONS_FLOAT SEMICOLON
			| EQELLIPSE
            | EQHYPERBOLA'''

def p_EQUATION_N1(t):
    '''EQUATION_N1 : '''
    #print("Read until here")

def p_FOR_LOOP(t):
    #'FOR_LOOP : FOR_LOOP_KEYWORD saveCount OPEN_PARENTHESES ID EQUALOP EXP forJump SEMICOLON EXPRESSION forExpression SEMICOLON ID EQUALOP EXP pop_exp CLOSE_PARENTHESES BLOCK forBack'
    'FOR_LOOP : FOR_LOOP_KEYWORD saveCount OPEN_PARENTHESES ASSIGN forJump EXPRESSION_BOOL forExpression SEMICOLON ID EQUALOP EXP pop_exp CLOSE_PARENTHESES BLOCK forBack'

def p_saveCount(t):
    'saveCount :'
    gv.saveCount = gv.quadCount

def p_pop_exp(t):
    'pop_exp :'
    list_quad_aux = []
    quad_aux = gv.quadList.pop()
    gv.quadCount = gv.quadCount - 1
    while quad_aux[0] != "GOTOF": #quitamos quads hasta el GOTOF para agragarlos al rato
        list_quad_aux.append(quad_aux)
        #print(quad_aux)
        #print(gv.quadCount)
        quad_aux = gv.quadList.pop()
        gv.quadCount = gv.quadCount - 1
    gv.quadList.append(quad_aux)
    gv.quadCount = gv.quadCount + 1
    #list_quad_aux.reverse()
    listPendingQuads.append(list_quad_aux)

def p_forExpression(t):
    'forExpression :'
    exp_type = PTypes.pop()
    if exp_type != "bool":
        raise Exception("ERROR: Type Mismatch!!! paso1, gotoF")
    else:
        result = PilaOp.pop()
        quad = ["GOTOF",result,[],-1]#genera cuadruplo
        gv.quadList.append(quad)#agrega cuadruplo
        gv.quadCount = gv.quadCount + 1#incrmenta cuenta de cuadruplos
        PJumps.append(gv.quadCount - 1)

def p_forBack(t):
    'forBack :'
    #print("FORBACK")
    end = PJumps.pop()
    #print("Hello there " + str(end))
    ret = PJumps.pop()
    list_quad_aux = listPendingQuads.pop()
    while list_quad_aux: #agrega quads del incremento que quitamos hace rato
        quad = list_quad_aux.pop()
        gv.quadList.append(quad)
        gv.quadCount = gv.quadCount + 1
    address = symtab.get_var_address(gv.currentScope,t[-6])
    quad2 = ["=",quad[3],[],address]
    #quad2 = ["=",quad[3],[],t[-6]]
    gv.quadList.append(quad2)
    gv.quadCount = gv.quadCount + 1
    ###############################
    quad = ["GOTO",[],[],ret+1] #genera cuadruplo
    gv.quadList.append(quad) #agrega cuadruplo
    gv.quadCount = gv.quadCount + 1 #incrmenta cuenta de cuadruplos
    gv.quadList[end][3] = gv.quadCount

def p_forJump(t):
    'forJump :'
    # print(t[-1])
    # print(t[-2])
    # print(t[-3])
    #address = symtab.get_var_address(gv.currentScope,t[-3])
    #quad = ["=",t[-1],[],address]
    #gv.quadList.append(quad)
    #gv.quadCount = gv.quadCount + 1 #incrmenta cuenta de cuadruplos
    PJumps.append(gv.quadCount - 1)
	
def p_MODULE(t):
    #'''MODULE : TYPE_P ID set_scope OPEN_PARENTHESES I
    #			| TYPE_S ID set_scope OPEN_PARENTHESES I'''
    'MODULE : ID modDef_paso1 OPEN_PARENTHESES I'
    #gv.currentScope = t[1]
    #symtab.cuScope = t[1]
    #print("module scope: " + cuScope)
    #symtab.add_module(t[1],"void")

def p_modDef_paso1(t):
    'modDef_paso1 :'
    symtab.add_module(gv.currentId,"void")
    gv.currentScope = t[-1]

#def p_set_scope(t):
#    'set_scope :'
#    gv.currentScope = t[-1]
#    symtab.add_module(gv.currentId,"void")
#   print("prueba del modulo: " + gv.currentId)
	
def p_I(t):
    '''I : TYPE_P ID modDef_paso2 J
            | TYPE_S ID modDef_paso2 J'''

def p_modDef_paso2(t):
    'modDef_paso2 :'
    size = 1
    if mem.checkSizeAvail(size, gv.currentType, gv.currentScope) :
        memAddress = mem.add_var(gv.currentType, None, size, gv.currentScope)    
        symtab.add_variable(gv.currentScope,gv.currentId,gv.currentType, size, memAddress)
        PModDataTypes.append(gv.currentType)
        symtab.add_param_num(gv.currentScope,gv.currentId,len(PModDataTypes))#add param number for PARAM OpCode
    else :
        raise Exception("Memory size exceeded in variables declaration")
			
def p_J(t):
    '''J : COMMA I
	    | CLOSE_PARENTHESES modDef_paso4 modDef_paso5 modDef_paso6 BLOCK ret_glob modDef_paso7
	    | CLOSE_PARENTHESES modDef_paso4 VARS modDef_paso5 modDef_paso6 BLOCK ret_glob modDef_paso7'''
    #print(gv.currentScope)
    #print(cuScope)
    #gv.currentScope = 'GLOBAL'

def p_modDef_paso4(t):
    'modDef_paso4 :'
    symtab.add_num_param(gv.currentScope)
    symtab.add_param_type_list(gv.currentScope,PModDataTypes)

def p_modDef_paso5(t):
    'modDef_paso5 :'
    symtab.add_num_vars(gv.currentScope)

def p_modDef_paso6(t):
    'modDef_paso6 :'
    symtab.add_num_quad(gv.currentScope, gv.quadCount)

def p_modDef_paso7(t):
    'modDef_paso7 :'
    quad = ["ENDPROC",[],[],[]]
    gv.quadList.append(quad)
    gv.quadCount = gv.quadCount + 1

def p_ret_glob(t):
    'ret_glob :'
    gv.currentScope = "GLOBAL"

# def p_L(t):
#     'L : CLOSE_PARENTHESES BLOCK'

# def p_K(t):
#     '''K : COMMA I
# 			| CLOSE_PARENTHESES BLOCK'''
	
	
def p_COLOR(t):
    '''COLOR : RED_KEYWORD
            | ORANGE_KEYWORD
			| YELLOW_KEYWORD
			| GREEN_KEYWORD
			| BLUE_KEYWORD
			| PURPLE_KEYWORD'''
			
def p_WRITE(t):
    '''WRITE : PRINT
            | PLOT'''
			
def p_PRINT(t):
    '''PRINT : PRINT_KEYWORD OPEN_PARENTHESES M
                | PRINT_KEYWORD OPEN_PARENTHESES MM'''
	
def p_M(t):
    '''M : CONS_STRING CLOSE_PARENTHESES SEMICOLON'''
    string = t[1][1:-1] #quitar comillas al inicio y al final
    quad = ["PRINT",[],[],string]
    gv.quadList.append(quad)
    gv.quadCount = gv.quadCount + 1

def p_MM(t):
    '''MM : EXPRESSION_OP CLOSE_PARENTHESES SEMICOLON'''
    if len(PTypes) > 0 :
        PTypes.pop()
        #quad = ["PRINT",[],[],PilaOp.pop()]
        temp = PilaOp.pop()
        print(temp)
        quad = ["PRINT",[],[],temp]
        gv.quadList.append(quad)
        gv.quadCount = gv.quadCount + 1
        #print("PilaOp esta vacia we jeje xd")
			
def p_WHILE_LOOP(t):
    'WHILE_LOOP : WHILE_LOOP_KEYWORD WHILE_paso1 OPEN_PARENTHESES EXPRESSION_BOOL CLOSE_PARENTHESES WHILE_paso2 BLOCK WHILE_paso3'

def p_WHILE_paso1(t):
    'WHILE_paso1 :'
    PJumps.append(gv.quadCount)

def p_WHILE_paso2(t):
    'WHILE_paso2 :'
    exp_type = PTypes.pop()
    if exp_type != "bool":
        raise Exception("ERROR: Type Mismatch!!! paso1, gotoF")
    else:
        result = PilaOp.pop()
        quad = ["GOTOF",result,[],-1] # Generate quad for gotof while
        gv.quadList.append(quad)
        gv.quadCount = gv.quadCount + 1 # Increment the quad count
        PJumps.append(gv.quadCount - 1)

def p_WHILE_paso3(t):
    'WHILE_paso3 :'
    #Code here
    end = PJumps.pop()
    ret = PJumps.pop()
    quad = ["GOTO",[],[],ret] #genera cuadruplo
    gv.quadList.append(quad) #agrega cuadruplo
    gv.quadCount = gv.quadCount + 1 #incrmenta cuenta de cuadruplos
    gv.quadList[end][3] = gv.quadCount #fill
        
	
def p_PLOT(t):
    '''PLOT : PLOT_KEYWORD OPEN_PARENTHESES ID COMMA COLOR CLOSE_PARENTHESES SEMICOLON
            | PLOT_KEYWORD OPEN_PARENTHESES ID CLOSE_PARENTHESES SEMICOLON'''
    quad = ["PLOT",[],t[3],t[5]]
    gv.quadList.append(quad)
    gv.quadCount = gv.quadCount + 1
	
def p_TRANSFORM(t):
    '''TRANSFORM : REFLECTION_KEYWORD
            | TRANS_KEYWORD
			| ROTATION_KEYWORD
			| STRETCH_KEYWORD'''
			
def p_F_CALL(t):
    'F_CALL : ID POINT TRANSFORM OPEN_PARENTHESES EXP CLOSE_PARENTHESES SEMICOLON'
	
def p_CONDITION(t):
    'CONDITION : IF_STATEMENT OPEN_PARENTHESES EXPRESSION_BOOL CLOSE_PARENTHESES gotoFcond N'

def p_gotoFcond(t):
    'gotoFcond :'
    exp_type = PTypes.pop()
    if exp_type != "bool":
        raise Exception("ERROR: Type Mismatch!!! paso1, gotoF")
    else:
        result = PilaOp.pop()
        quad = ["GOTOF",result,[],-1]#genera cuadruplo
        gv.quadList.append(quad)#agrega cuadruplo
        gv.quadCount = gv.quadCount + 1 #incrmenta cuenta de cuadruplos
        PJumps.append(gv.quadCount - 1)
	
def p_N(t):
    '''N : BLOCK ELSE_STATEMENT gotoElse BLOCK endif
            | BLOCK endif'''

def p_gotoElse(t):
    'gotoElse :'
    quad = ["GOTO",[],[],-1] #genera cuadruplo
    gv.quadList.append(quad) #agrega cuadruplo
    gv.quadCount = gv.quadCount + 1 #incrmenta cuenta de cuadruplos
    falso = PJumps.pop()
    PJumps.append(gv.quadCount - 1)
    gv.quadList[falso][3] = gv.quadCount

def p_endif(t):
    'endif :'
    end = PJumps.pop()
    #print("General kenobi" + " " + str(end) + "  " + str(gv.quadCount))
    #PJumps.append(gv.quadCount - 1)
    #print("Length" + str(len(gv.quadList)))
    #print("endif" + str(gv.quadList[end]))
    gv.quadList[end][3] = gv.quadCount
			
def p_EXPRESSION_OP(t):
    '''EXPRESSION_OP : EXPRESSION_BOOL
            | ATTRIBUTE_2'''
			
def p_ATTR_2(t):
    '''ATTR_2 : CENTER_KEYWORD
            | FOCUS_KEYWORD
			| VERTEX_KEYWORD'''

# def p_EXPRESSION_BOOL(t):
#     '''EXPRESSION_BOOL : EXPRESSION AND_KEYWORD paso1bool EXPRESSION paso2bool
#             | EXPRESSION OR_KEYWORD paso1bool EXPRESSION paso2bool
#             | NOT_KEYWORD EXPRESSION pasoNotBool
#             | EXPRESSION'''

def p_EXPRESSION_BOOL(t):
    '''EXPRESSION_BOOL : EXPRESSION paso2bool BBB
            | EXPRESSION paso2bool
            | NOT_KEYWORD paso1bool EXPRESSION_BOOL pasoNotBool
            | NOT_KEYWORD paso1bool EXPRESSION_BOOL pasoNotBool BBB'''

def p_BBB(t):
    '''BBB : AND_KEYWORD paso1bool EXPRESSION_BOOL
            | OR_KEYWORD paso1bool EXPRESSION_BOOL'''

# def p_EXPRESSION(t):
#     '''EXPRESSION : EXP paso9 RRR
#             | EXP paso9'''

# def p_RRR(t):
#     'RRR : RELOP paso8 EXPRESSION'

def p_paso1bool(t):
    'paso1bool :'
    print("saludos : "+t[-1])
    POper.append(t[-1]) # Append left side of expression between boolean operator
    PTypes.append("bool")

def p_paso2bool(t):
    'paso2bool :'
    print("POpewr")
    print(POper)
    if POper:
        temp = POper.pop()
        POper.append(temp)
        print("temp")
        print(temp)
        if temp == "and" or temp == "or":
            right_op = PilaOp.pop()
            right_type = PTypes.pop()
            left_op = PilaOp.pop()
            left_type = PTypes.pop()
            operator = POper.pop()
            print(operator)
            print("operator")
            result_Type = sem_cube[operators_dict[operator]][var_types_dict[left_type]][var_types_dict[right_type]]
            if result_Type != -1 :
                if mem.checkSizeAvail(1, result_Type, "TEMP"):
                    result = mem.nextAvail(result_Type)
                else:
                    raise Exception("Ran out of memory")
                quad = [operator,left_op,right_op,result]# genera cuadruplo
                gv.quadList.append(quad)# agrega cuadruplo
                gv.quadCount = gv.quadCount + 1;# incrmenta cuenta de cuadruplos
                PilaOp.append(result)
                if result_Type == 0:
                    PTypes.append("int")
                elif result_Type == 1:
                    PTypes.append("float")
                elif result_Type == 2:
                    PTypes.append("bool")
                #if any operand were a temporal space, return it to AVAIL
            else:
                raise Exception("ERROR: Type Mismatch!!! Boolean operation invalid")                

# def p_EXPRESSION_NOT(t):
#     '''EXPRESSION_NOT : NOT_KEYWORD paso1bool EXPRESSION_BOOL pasoNotBool
#             | NOT_KEYWORD paso1bool EXPRESSION_BOOL pasoNotBool BBB'''

def p_pasoNotBool(t):
    'pasoNotBool :'
    if POper:
        temp = POper.pop()
        POper.append(temp)
        print("temp")
        print(temp)
        if temp == "not":
            right_op = PilaOp.pop()
            right_type = PTypes.pop()
            #We don't require left operator, 'NOT' is unary            
            operator = POper.pop()
            result_Type = sem_cube[operators_dict[operator]][2][var_types_dict[right_type]]
            if result_Type != -1 :
                if mem.checkSizeAvail(1, result_Type, "TEMP"):
                    result = mem.nextAvail(result_Type)
                else:
                    raise Exception("Ran out of memory")
                quad = [operator, right_op, [], result]
                gv.quadList.append(quad)# agrega cuadruplo
                gv.quadCount = gv.quadCount + 1;# incrmenta cuenta de cuadruplos
                PilaOp.append(result)
                if result_Type == 0:
                    PTypes.append("int")
                elif result_Type == 1:
                    PTypes.append("float")
                elif result_Type == 2:
                    PTypes.append("bool")
                    #if any operand were a temporal space, return it to AVAIL            
            else:
                raise Exception("ERROR: Type Mismatch!!! Boolean operation invalid")      
			
def p_EXPRESSION(t):
    '''EXPRESSION : EXP RELOP paso8 EXP paso9
            | EXP'''
# def p_EXPRESSION(t):
#     '''EXPRESSION : EXP paso9 RRR
#             | EXP paso9'''

# def p_RRR(t):
#     'RRR : RELOP paso8 EXPRESSION'

def p_paso8(t):
    'paso8 :'
    POper.append(t[-1])
	
def p_paso9(t):
    'paso9 :'
    if POper:
        temp = POper.pop()
        POper.append(temp)
        if temp == ">" or temp == "<" or temp == "<>" or temp == "==" :
            right_op = PilaOp.pop()
            right_type = PTypes.pop()
            left_op = PilaOp.pop()
            left_type = PTypes.pop()
            operator = POper.pop()
            #result_Type = sem_cube[left_op][right_op][operator]
            #print(var_types_dict[left_type])
            #print(var_types_dict[right_type])
            #print(operators_dict[operator])
            #result_Type = sem_cube[var_types_dict[left_type]][var_types_dict[right_type]][operators_dict[operator]]
            result_Type = sem_cube[operators_dict[operator]][var_types_dict[left_type]][var_types_dict[right_type]]
            if result_Type != -1 :
                if mem.checkSizeAvail(1, result_Type, "TEMP"):
                    result = mem.nextAvail(result_Type)
                    #print("simon wey " + str(result))
                else:
                    raise Exception("Ran out of memory")
                quad = [operator,left_op,right_op,result]#genera cuadruplo
                gv.quadList.append(quad)#agrega cuadruplo
                gv.quadCount = gv.quadCount + 1;#incrmenta cuenta de cuadruplos
                PilaOp.append(result)
                #PTypes.append(result_Type)
                if result_Type == 0:
                    PTypes.append("int")
                elif result_Type == 1:
                    PTypes.append("float")
                elif result_Type == 2:
                    PTypes.append("bool")
                #if any operand were a temporal space, return it to AVAIL
            else:
                raise Exception("ERROR: Type Mismatch!!! paso4")
	
# def p_O(t):
#     '''O : RELOP EXP
#             | empty'''
			
def p_EXP(t):
    '''EXP : TERM paso4 P
            | TERM paso4'''
			
def p_paso4(t):
    'paso4 :'
    if POper:
        temp = POper.pop()
        POper.append(temp)
        #print(temp)

        if temp == "+" or temp == "-" :
            right_op = PilaOp.pop()
            right_type = PTypes.pop()
            left_op = PilaOp.pop()
            left_type = PTypes.pop()
            operator = POper.pop()
            #result_Type = sem_cube[left_op][right_op][operator]
            #result_Type = sem_cube[var_types_dict[left_type]][var_types_dict[right_type]][operators_dict[operator]]
            result_Type = sem_cube[operators_dict[operator]][var_types_dict[left_type]][var_types_dict[right_type]]
            if result_Type != -1 :
                #result = next_memory()
                if mem.checkSizeAvail(1, result_Type, "TEMP"):
                    result = mem.nextAvail(result_Type)
                    #print("simon wey " + str(result))
                else:
                    raise Exception("Ran out of memory")
                #address1 
                quad = [operator,left_op,right_op,result]
                gv.quadList.append(quad)
                gv.quadCount = gv.quadCount + 1#incrmenta cuenta de cuadruplos
                PilaOp.append(result)
                #PTypes.append(result_Type)
                if result_Type == 0:
                    PTypes.append("int")
                elif result_Type == 1:
                    PTypes.append("float")
                elif result_Type == 2:
                    PTypes.append("bool")
                #if any operand were a temporal space, return it to AVAIL
            else:
                raise Exception("ERROR: Type Mismatch!!! paso4")
				
def p_P(t):
    '''P : PLUSOP paso2a EXP
			| MINUSOP paso2b EXP'''

def p_paso2a(t):
    'paso2a :'
    POper.append("+")

def p_paso2b(t):
    'paso2b :'
    POper.append("-")
			
#def p_P(t):
    #'''P : PLUSOP EXP
			#| MINUSOP EXP'''
			
def p_TERM(t):
    '''TERM : FACTOR paso5 Q
            | FACTOR paso5'''
			
def p_paso5(t):
    'paso5 :'
    if POper:
        temp = POper.pop()
        POper.append(temp)

        if temp == "*" or temp == "/" :
            right_op = PilaOp.pop()
            right_type = PTypes.pop()
            left_op = PilaOp.pop()
            left_type = PTypes.pop()
            operator = POper.pop()
            #result_Type = sem_cube[left_op][right_op][operator]
            #result_Type = sem_cube[var_types_dict[left_type]][var_types_dict[right_type]][operators_dict[operator]]
            result_Type = sem_cube[operators_dict[operator]][var_types_dict[left_type]][var_types_dict[right_type]]
            if result_Type != -1 :
                if mem.checkSizeAvail(1, result_Type, "TEMP"):
                    result = mem.nextAvail(result_Type)
                else:
                    raise Exception("Ran out of memory")
                quad = [operator,left_op,right_op,result]
                gv.quadList.append(quad)
                gv.quadCount = gv.quadCount + 1#incrmenta cuenta de cuadruplos
                PilaOp.append(result)
                #PTypes.append(result_Type)
                if result_Type == 0:
                    PTypes.append("int")
                elif result_Type == 1:
                    PTypes.append("float")
                elif result_Type == 2:
                    PTypes.append("bool")
                #if any operand were a temporal space, return it to AVAIL
            else:
                raise Exception("ERROR: Type Mismatch!!! paso4")
			
def p_Q(t):
    '''Q : TIMESOP paso3a TERM
			| DIVIDEOP paso3b TERM'''

def p_paso3a(t):
    'paso3a :'
    POper.append("*")

def p_paso3b(t):
    'paso3b :'
    POper.append("/")
			
def p_ATTR(t):
    '''ATTR : AREA_KEYWORD
			| PERIMETER_KEYWORD
			| EXC_KEYWORD
            | RADIUS_KEYWORD'''
			
def p_FACTOR(t):
    '''FACTOR : OPEN_PARENTHESES paso6 EXPRESSION_BOOL CLOSE_PARENTHESES paso7
            | VAR_CONS
            | ATTRIBUTE'''
			
def p_paso6(t):
    'paso6 :'
    POper.append("(")

def p_paso7(t):
    'paso7 :'
    POper.pop()
	
# def p_R(t):
#     '''R : PLUSOP
# 			| MINUSOP'''
			
def p_ATTRIBUTE(t):
    'ATTRIBUTE : ID POINT ATTR'
	
def p_ATTRIBUTE_2(t):
    'ATTRIBUTE_2 : ID POINT ATTR_2'
	
def p_VAR_CONS(t):
    '''VAR_CONS : ID paso1a
			| ID S
			| CONS_INT paso1b
            | CONS_FLOAT paso1c
            | MINUSOP addminus CONS_INT paso1b
            | MINUSOP addminus CONS_FLOAT paso1c
            | TRUE_KEYWORD paso1d
            | FALSE_KEYWORD paso1d'''

def p_addminus(t):
    'addminus :'
    gv.minusFlag = True

def p_paso1a(t):
    'paso1a :'
    #print("la variable del paso 1 es: " + t[-1])
    #print("El type es: " + symtab.SYM_TABLE["GLOBAL"]["iii"]["type"])
    address = symtab.get_var_address(gv.currentScope,t[-1])
    PilaOp.append(address)
    #PilaOp.append(t[-1])
    #print(symtab.SYM_TABLE)
    PTypes.append(symtab.SYM_TABLE[gv.currentScope][t[-1]]["#type"])
	
def p_paso1b(t):
    'paso1b :'
    #print("la variable del paso 1 es: " + t[-1])
    #print("El type es: " + symtab.SYM_TABLE["GLOBAL"]["iii"]["type"])
    if gv.minusFlag:
        op = "%-" + t[-1]
        gv.minusFlag = False
    else:
        op = "%" + t[-1]
    #PilaOp.append(t[-1])
    PilaOp.append(op)
    PTypes.append("int")

def p_paso1c(t):
    'paso1c :'
    #op = "%" + t[-1]
    if gv.minusFlag:
        op = "%-" + t[-1]
        gv.minusFlag = False
    else:
        op = "%" + t[-1]
    #PilaOp.append(t[-1])
    PilaOp.append(op)
    PTypes.append("float")

def p_paso1d(t):
    'paso1d :'
    PilaOp.append(t[-1])
    PTypes.append("bool")
			
def p_S(t):
    '''S : OPEN_SQUARE_BRACKET EXP CLOSE_SQUARE_BRACKET arrCall1
            | OPEN_SQUARE_BRACKET EXP CLOSE_SQUARE_BRACKET OPEN_SQUARE_BRACKET EXP CLOSE_SQUARE_BRACKET
			| modCall_paso1 modCall_paso2 OPEN_PARENTHESES SS'''
    #print("HOLIIIIIIIIIIIII"+t[-1])

def p_arrAddress(t):
    'arrAddress :'
    print("en el arrAddress: "+str(gv.currentId))
    gv.currentArrAddress = symtab.get_var_address(gv.currentScope,gv.currentId)

def p_arrCall1(t):
    'arrCall1 :'
    print("el id es: " + t[-4])
    gv.currentArrAddress = symtab.get_var_address(gv.currentScope,t[-4])
    pos = PilaOp.pop()
    posType = PTypes.pop()
    if isinstance(pos,str):
        if pos[0] == '%':
            pos = getCons(pos[1:])
            print("pos: " + str(pos))
    result_Type = sem_cube[operators_dict["+"]][var_types_dict[posType]][var_types_dict["int"]]
    if mem.checkSizeAvail(1, result_Type, "TEMP"):
        result = mem.nextAvail(result_Type)
        #print("simon wey " + str(result))
    else:
        raise Exception("Ran out of memory")
    #address1
    left_op = "%" + str(gv.currentArrAddress)
    # right_op = "%" + str(pos)
    ##############quad = ["+",left_op,pos,result]
    if mem.memorySize*6 <= pos < mem.memorySize*9 or pos == symtab.get_var_address(gv.currentScope,gv.currentId):
        quad = ["+",left_op,pos,result]
    else:
        quad = ["+",left_op,"%" + str(pos),result]
    gv.quadList.append(quad)
    gv.quadCount = gv.quadCount + 1#incrmenta cuenta de cuadruplos
    if mem.checkSizeAvail(1, result_Type, "TEMP"):
        result2 = mem.nextAvail(result_Type)
        #print("simon wey " + str(result))
    else:
        raise Exception("Ran out of memory")
    
    quad = ["ACC",result,[],result2]#Acceso a valor en result (result es una direccion)
    gv.quadList.append(quad)
    gv.quadCount = gv.quadCount + 1#incrmenta cuenta de cuadruplos

    PilaOp.append(result2)
    #PTypes.append(result_Type)
    if result_Type == 0:
        PTypes.append("int")
    elif result_Type == 1:
        PTypes.append("float")
    elif result_Type == 2:
        PTypes.append("bool")
    #print("appendeando en arrCall: "+str(gv.currentArrAddress+pos))
    #pos = mem.access(pos)
    #PilaOp.append(pos)
    #PilaOp.append(gv.currentArrAddress+pos)
    #PilaOp.append(pos)
    #PTypes.pop()
    quad = ["VER",pos,[],symtab.get_size(gv.currentScope,t[-4])]
    gv.quadList.append(quad)
    gv.quadCount = gv.quadCount + 1#incrmenta cuenta de cuadruplos

    #quad = ["+",pos,symtab.get_var_address(gv.currentScope,t[-4]),symtab.get_size(gv.currentScope,t[-4])]


def p_SS(t):
    '''SS : EXP modCall_paso3 SSS
            | EXP modCall_paso3 COMMA modCall_paso4 SS
			| SSS'''

def p_SSS(t):
    '''SSS : modCall_paso5 CLOSE_PARENTHESES modCall_paso6'''

def p_modCall_paso1(t):
    'modCall_paso1 :'
    #print(t[-1])
    if symtab.mod_exist(t[-1]) :
        gv.currentModCall = t[-1]
    else :
        raise Exception("ERROR: Calling inexistent module!! paso1")

def p_modCall_paso2(t):
    'modCall_paso2 :'
    quad = ["ERA", t[-2], [], []]
    gv.paramCount = 1
    gv.quadList.append(quad)
    gv.quadCount = gv.quadCount + 1

def p_modCall_paso3(t):
    'modCall_paso3 :'
    Argument = PilaOp.pop()
    ArgumentType = PTypes.pop()
    TL = symtab.get_param_type_list(gv.currentModCall)#jala lista de tipos de ese modulo
    if ArgumentType == TL[gv.paramCount-1] :
        quad = ["PARAM",Argument,[],gv.paramCount]
        gv.quadList.append(quad)
        gv.quadCount = gv.quadCount + 1
    else :
        raise Exception("ERROR: Incorrect parameter type!! paso3")

def p_modCall_paso4(t):
    'modCall_paso4 :'
    TL = symtab.get_param_type_list(gv.currentModCall)#jala lista de tipos de ese modulo
    if(gv.paramCount == len(TL)) :
        raise Exception("ERROR: Number of parameters is inconsistent!! paso1")
    else :
        gv.paramCount = gv.paramCount + 1

def p_modCall_paso5(t):
    'modCall_paso5 :'
    #verify last parameter points to null
    TL = symtab.get_param_type_list(gv.currentModCall)#jala lista de tipos de ese modulo
    if len(TL) == gv.paramCount :
        gv.paramCount = 0 #limpia para siguiente llamada
    else :
        raise Exception("ERROR: Number of parameters is inconsistent!! paso1")

def p_modCall_paso6(t):
    'modCall_paso6 :'
    #print("YA LLEGUE AL MODCALL DEL GOSUB")
    quad = ["GOSUB",gv.currentModCall,[],symtab.get_num_quad(gv.currentModCall)]
    gv.quadList.append(quad)
    gv.quadCount = gv.quadCount + 1
			
# def p_T(t):
#     '''T : OPEN_SQUARE_BRACKET EXP CLOSE_SQUARE_BRACKET
# 			| empty'''
			
# def p_U(t):
#     '''U : COMMA EXP U
# 			| CLOSE_PARENTHESES'''
			
# def p_EMPTY(t):
#     'empty :'
#     pass

def p_error(p):
    if p:
        #print("On line '%i' " % p.lexer.lineno + "syntax error at '%s'" % p.value)
        # get formatted representation of stack
        stack_state_str = ' '.join([symbol.type for symbol in parser.symstack][1:])

        print('Syntax error in input! Parser State:{} {} . {}'
            .format(parser.state,
                stack_state_str,
                p))
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
import os
parser = yacc.yacc()
fileName = input("Enter a file name \n")
file = open(fileName, "r")
code = ""
#Add all lines to one string for parsing
for line in file:
    try:
        code += line
    except EOFError:
        break

#Finally parse the input code
try:
    parser.parse(code)
finally:
    print("Parsing complete")
