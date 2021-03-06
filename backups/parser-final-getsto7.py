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
	'trans' : 'TRANS_KEYWORD',
	'rotation' : 'ROTATION_KEYWORD',
	'stretch' : 'STRETCH_KEYWORD',
    #Not in the official document (yet) :
    'print' : 'PRINT_KEYWORD',
    'program' : 'PROGRAM_KEYWORD'
}
        #New tokens:
tokens = ['ID', 'EQX', 'EQY', 'CONS_STRING', 'CONS_INT', 
        'CONS_FLOAT', 'CONS_BOOL', 'RELOP',
        #Old tokens:
        'OPEN_BRACKET','CLOSE_BRACKET','OPEN_SQUARE_BRACKET','CLOSE_SQUARE_BRACKET', 'COMMA', 'POINT', 'PLUSOP', 'MINUSOP',
        'TIMESOP', 'DIVIDEOP', 'OPEN_PARENTHESES', 'CLOSE_PARENTHESES',
        'ARROW','TWO_POINTS', 'SEMICOLON', 'EQUALOP', 'CTE_I', 'CTE_F', 'STRING'] + list(reserved.values())
#New tokens:
#t_ID = r'[a-zA-Z_][a-zA-Z0-9]*' #Not needed since it's already been made below for LittleDuck
t_EQX = r'[[0-9]+\.[0-9]+] ["x^2"] [/] [[0-9]+\.[0-9]+]'
t_EQY = r'[[0-9]+\.[0-9]+] ["y^2"] [/] [[0-9]+\.[0-9]+]'
t_CONS_STRING = r'\".*\"'
t_CONS_INT = r'[0-9]+'
t_CONS_FLOAT = r'[0-9]+\.[0-9]+'
t_CONS_BOOL = r'true | false'
#t_RELOP = r'' #Not needed since it's already been made below for LittleDuck

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
t_ARROW = r'~'#flechita
t_TWO_POINTS = r':'
t_SEMICOLON = r';'
t_EQUALOP = r'='
t_RELOP = r'<(>)? | >'
#t_CTE_I = r'[0-9]+' #This was commented out since it is replaced by CONS_INT
#t_CTE_F = r'[0-9]+\.[0-9]+' #This was commented out since it is replaced by CONS_FLOAT
#t_STRING = r'\".*\"' #This was commented out since it is replaced by CONS_STRING

t_ignore = " \t" #Ignore whitespace

def t_ID(t):
    r'[A-Za-z]([A-Za-z]|[0-9])*'
    t.type = reserved.get(t.value, 'ID')
    return t


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

def p_PROGRAM(t):
    'PROGRAM : PROGRAM_KEYWORD ID SEMICOLON A' 
                                             
def p_A(t): 
    '''A : VARS B
            | B'''

def p_B(t):
    '''B : MODULE B
            | MODULE BLOCK
            | BLOCK'''
    
def p_VARS(t):
    'VARS : VAR_KEYWORD C'

def p_C(t):  
    '''C : ID D
            | ID OPEN_SQUARE_BRACKET EXP CLOSE_SQUARE_BRACKET D
			| ID OPEN_SQUARE_BRACKET EXP CLOSE_SQUARE_BRACKET OPEN_SQUARE_BRACKET EXP CLOSE_SQUARE_BRACKET D'''
			
def p_D(t):
    '''D : COMMA C
            | TWO_POINTS E'''
			
def p_E(t):
    '''E : TYPE_P F
            | TYPE_S F'''
			
def p_F(t):
    '''F : SEMICOLON C
            | SEMICOLON'''

def p_BLOCK(t):
    'BLOCK : OPEN_BRACKET G'
	
def p_G(t):
    '''G : STATEMENT CLOSE_BRACKET
            | STATEMENT G
            | CLOSE_BRACKET'''
			
def p_STATEMENT(t):
    '''STATEMENT : EXPRESSION_OP
            | ASSIGN
			| WRITE
			| FOR_LOOP
			| WHILE_LOOP
			| CONDIITON
            | F_CALL'''
			
def p_ASSIGN(t):
    'ASSIGN : ID H'
	
def p_H(t):
    '''H : ARROW EQUATION SEMICOLON
            | EQUALOP EXPRESSION SEMICOLON'''

def p_FOR_LOOP(t):
    'FOR_LOOP : FOR_LOOP_KEYWORD OPEN_PARENTHESES ID EQUALOP EXP SEMICOLON EXPRESSION SEMICOLON ID EQUALOP EXP CLOSE_PARENTHESES BLOCK'
	
def p_MODULE(t):
    'MODULE : ID OPEN_PARENTHESES I'
	
def p_I(t):
    '''I : ID TWO_POINTS J
            | L'''
			
def p_J(t):
    '''J : TYPE_P K
			| TYPE_S K'''

def p_L(t):
    'L : CLOSE_PARENTHESES BLOCK'

def p_K(t):
    '''K : COMMA I
			| CLOSE_PARENTHESES BLOCK'''
	
	
def p_COLOR(t):
    '''COLOR : RED_KEYWORD
            | ORANGE_KEYWORD
			| YELLOW_KEYWORD
			| GREEN_KEYWORD
			| BLUE_KEYWORD
			| PURPLE_KEYWORD'''
			
def p_TYPE_S(t):
    '''TYPE_S : PARABOLA_KEYWORD
            | ELLIPSE_KEYWORD
			| HYPERBOLA_KEYWORD
			| CIRCLE_KEYWORD'''
			
def p_TYPE_P(t):
    '''TYPE_P : INT_KEYWORD
            | FLOAT_KEYWORD
			| BOOL_KEYWORD'''
			
def p_WRITE(t):
    '''WRITE : PRINT
            | PLOT'''
			
def p_PRINT(t):
    'PRINT : PRINT_KEYWORD OPEN_PARENTHESES M'
	
def p_M(t):
    '''M : EXPRESSION_OP CLOSE_PARENTHESES SEMICOLON
            | CONS_STRING CLOSE_PARENTHESES SEMICOLON'''
			
def p_WHILE_LOOP(t):
    'WHILE_LOOP : WHILE_LOOP_KEYWORD OPEN_PARENTHESES EXPRESSION CLOSE_PARENTHESES BLOCK'
	
def p_PLOT(t):
    'PLOT : PLOT_KEYWORD OPEN_PARENTHESES ID COMMA COLOR CLOSE_PARENTHESES SEMICOLON'
	
def p_TRANSFORM(t):
    '''TRANSFORM : REFLECTION_KEYWORD
            | TRANS_KEYWORD
			| ROTATION_KEYWORD
			| STRETCH_KEYWORD'''
			
def p_F_CALL(t):
    'F_CALL : ID POINT TRANSFORM OPEN_PARENTHESES EXP CLOSE_PARENTHESES SEMICOLON'
	
def p_CONDITION(t):
    'CONDIITON : IF_STATEMENT OPEN_PARENTHESES EXPRESSION CLOSE_PARENTHESES BLOCK N'
	
def p_N(t):
    '''N : ELSE_STATEMENT BLOCK
            | empty'''
			
def p_EXPRESSION_OP(t):
    '''EXPRESSION_OP : EXPRESSION
            | ATTRIBUTE_2'''
			
def p_ATTR_2(t):
    '''ATTR_2 : CENTER_KEYWORD
            | FOCUS_KEYWORD
			| VERTEX_KEYWORD'''
			
def p_EXPRESSION(t):
    'EXPRESSION : EXP O'
	
def p_O(t):
    '''O : RELOP EXP
            | empty'''
			
def p_EXP(t):
    '''EXP : ATTRIBUTE P
            | TERM P'''
			
def p_P(t):
    '''P : PLUSOP EXP
			| MINUSOP EXP
            | empty'''
			
def p_TERM(t):
    '''TERM : ATTRIBUTE Q
            | FACTOR Q'''
			
def p_Q(t):
    '''Q : TIMESOP TERM
			| DIVIDEOP TERM
            | empty'''
			
def p_ATTR(t):
    '''ATTR : AREA_KEYWORD
			| PERIMETER_KEYWORD
			| EXC_KEYWORD
            | RADIUS_KEYWORD'''
			
def p_FACTOR(t):
    '''FACTOR : OPEN_PARENTHESES EXPRESSION CLOSE_PARENTHESES
			| PLUSOP VAR_CONS
			| MINUSOP VAR_CONS
            | VAR_CONS'''
			
def p_EQUATION(t):
    'EQUATION : EQX R EQY EQUALOP CONS_FLOAT'
	
def p_R(t):
    '''R : PLUSOP
			| MINUSOP'''
			
def p_ATTRIBUTE(t):
    'ATTRIBUTE : ID POINT ATTR'
	
def p_ATTRIBUTE_2(t):
    'ATTRIBUTE_2 : ID POINT ATTR_2'
	
def p_VAR_CONS(t):
    '''VAR_CONS : ID
			| ID S
			| CONS_INT
            | CONS_FLOAT'''
			
def p_S(t):
    '''S : OPEN_SQUARE_BRACKET EXP CLOSE_SQUARE_BRACKET T
			| OPEN_PARENTHESES EXP U'''
			
def p_T(t):
    '''T : OPEN_SQUARE_BRACKET EXP CLOSE_SQUARE_BRACKET
			| empty'''
			
def p_U(t):
    '''U : COMMA EXP U
			| CLOSE_PARENTHESES'''
			
def p_EMPTY(t):
    'empty :'
    pass

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
