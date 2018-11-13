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
    #Not in the official document (yet) :
    'print' : 'PRINT_KEYWORD',
    'program' : 'PROGRAM_KEYWORD',
    'x' : 'X_KEYWORD',
    'y' : 'Y_KEYWORD',
    '&' : 'POWER'
}
        #New tokens:
tokens = ['ID', 'EQPARABOLA', 'EQCIRCLE', 'EQELLIPSE', 'EQHYPERBOLA', 'CONS_STRING', 'CONS_INT', 
        'CONS_FLOAT', 'CONS_BOOL', 'RELOP',
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
#import vm
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

#cuScope = "GLOBAL"

def p_PROGRAM(t):
    'PROGRAM : goto_main PROGRAM_KEYWORD ID SEMICOLON A'
    gv.currentId = t[2] # guarda nombre del programa
    gv.currentType = "PROGRAM" # tipo de dato "PROGRAM"
    symtab.add_variable("GLOBAL",gv.currentId,gv.currentType,None,None)
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
    #vm.run(gv.quadList, symtab)    

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
    #print(gv.currentType)
    if mem.checkSizeAvail(size, gv.currentType, gv.currentScope) :
        memAddress = mem.add_var(gv.currentType, None, size, gv.currentScope)
        symtab.add_variable(gv.currentScope,gv.currentId,gv.currentType, size, memAddress)
    else :
        raise Exception("Memory size exceeded in variables declaration")
    #symtab.add_variable(cuScope,gv.currentId,gv.currentType)
    #####print("var name: " + gv.currentId)
    #####print("scope   : " + gv.currentScope)

def p_add_variableArr(t):
    'add_variableArr :'
    size = int(t[-2])
    if mem.checkSizeAvail(size, gv.currentType, gv.currentScope) :
        memAddress = mem.add_var(gv.currentType, None, size, gv.currentScope)    
        symtab.add_variable(gv.currentScope,gv.currentId,gv.currentType, size, memAddress)
    else :
        raise Exception("Memory size exceeded in variables declaration (1D ARRAY SIZE)")
    
def p_add_variableArr2(t):
    'add_variableArr2 :'
    size = int(t[-2]) * int(t[-5])
    if mem.checkSizeAvail(size, gv.currentType, gv.currentScope) :
        memAddress = mem.add_var(gv.currentType, None, size, gv.currentScope)
        symtab.add_variable(gv.currentScope,gv.currentId,gv.currentType, size, memAddress)
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

def p_V1(t):
    '''V1 : EXP modCall_paso3 W1
            | EXP modCall_paso3 COMMA modCall_paso4 V1
            | W1'''

def p_W1(t):
    '''W1 : modCall_paso5 CLOSE_PARENTHESES SEMICOLON modCall_paso6'''

			
def p_ASSIGN(t):
    '''ASSIGN : ID EQUALOP EXPRESSION SEMICOLON'''
    # ID ARROW EQUATION
    #result_Type = sem_cube[operators_dict[operator]][var_types_dict[left_type]][var_types_dict[right_type]]
    #print(t[1])
    lastType = PTypes.pop() #Get the type of the id (on the left side of the assign)
    result_Type = sem_cube[operators_dict["="]][var_types_dict[symtab.get_return_type(gv.currentScope,t[1])]][var_types_dict[lastType]] #Check if the assign is valid
    if result_Type != -1 :
        address = symtab.get_var_address(gv.currentScope,t[1])
        quad = ["=",PilaOp.pop(),[],address]
        #quad = ["=",PilaOp.pop(),[],t[1]]
        gv.quadList.append(quad)
        gv.quadCount = gv.quadCount + 1
    else:
        #print("Incompatible types for assign")
        raise Exception("Incompatible types " + lastType + " assigned to " + symtab.get_return_type(gv.currentScope,t[1]))

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
    'FOR_LOOP : FOR_LOOP_KEYWORD saveCount OPEN_PARENTHESES ASSIGN forJump EXPRESSION forExpression SEMICOLON ID EQUALOP EXP pop_exp CLOSE_PARENTHESES BLOCK forBack'

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
    print(t[-1])
    print(t[-2])
    print(t[-3])
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
    'PRINT : PRINT_KEYWORD OPEN_PARENTHESES M'
	
def p_M(t):
    '''M : EXPRESSION_OP CLOSE_PARENTHESES SEMICOLON
            | CONS_STRING CLOSE_PARENTHESES SEMICOLON'''
    quad = ["PRINT",[],[],t[1]]
    gv.quadList.append(quad)
    gv.quadCount = gv.quadCount + 1
			
def p_WHILE_LOOP(t):
    'WHILE_LOOP : WHILE_LOOP_KEYWORD OPEN_PARENTHESES EXPRESSION CLOSE_PARENTHESES BLOCK'
	
def p_PLOT(t):
    '''PLOT : PLOT_KEYWORD OPEN_PARENTHESES ID COMMA COLOR CLOSE_PARENTHESES SEMICOLON
            | PLOT_KEYWORD OPEN_PARENTHESES ID CLOSE_PARENTHESES SEMICOLON'''
	
def p_TRANSFORM(t):
    '''TRANSFORM : REFLECTION_KEYWORD
            | TRANS_KEYWORD
			| ROTATION_KEYWORD
			| STRETCH_KEYWORD'''
			
def p_F_CALL(t):
    'F_CALL : ID POINT TRANSFORM OPEN_PARENTHESES EXP CLOSE_PARENTHESES SEMICOLON'
	
def p_CONDITION(t):
    'CONDITION : IF_STATEMENT OPEN_PARENTHESES EXPRESSION CLOSE_PARENTHESES gotoFcond N'

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
    '''EXPRESSION_OP : EXPRESSION
            | ATTRIBUTE_2'''
			
def p_ATTR_2(t):
    '''ATTR_2 : CENTER_KEYWORD
            | FOCUS_KEYWORD
			| VERTEX_KEYWORD'''
			
def p_EXPRESSION(t):
    '''EXPRESSION : EXP RELOP paso8 EXP paso9
            | EXP'''

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
                #print("zag" + str(result_Type))
                if mem.checkSizeAvail(1, result_Type, "TEMP"):
                    result = mem.nextAvail(result_Type)
                    #print("simon wey " + str(result))
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
    '''FACTOR : OPEN_PARENTHESES paso6 EXPRESSION CLOSE_PARENTHESES paso7
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
            | TRUE_KEYWORD paso1d
            | FALSE_KEYWORD paso1d'''

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
    PilaOp.append(t[-1])
    PTypes.append("int")

def p_paso1c(t):
    'paso1c :'
    #print("la variable del paso 1 es: " + t[-1])
    #print("El type es: " + symtab.SYM_TABLE["GLOBAL"]["iii"]["type"])
    PilaOp.append(t[-1])
    PTypes.append("float")

def p_paso1d(t):
    'paso1d :'
    #print("la variable del paso 1 es: " + t[-1])
    #print("El type es: " + symtab.SYM_TABLE["GLOBAL"]["iii"]["type"])
    PilaOp.append(t[-1])
    PTypes.append("bool")
			
def p_S(t):
    '''S : OPEN_SQUARE_BRACKET EXP CLOSE_SQUARE_BRACKET
            | OPEN_SQUARE_BRACKET EXP CLOSE_SQUARE_BRACKET OPEN_SQUARE_BRACKET EXP CLOSE_SQUARE_BRACKET
			| modCall_paso1 modCall_paso2 OPEN_PARENTHESES SS'''
    print("HOLIIIIIIIIIIIII"+t[-1])

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
    quad = ["ERA", t[-1], [], []]
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
        print("On line '%i' " % p.lexer.lineno + "syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
import os
parser = yacc.yacc()
file = open("code.txt", "r")
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
