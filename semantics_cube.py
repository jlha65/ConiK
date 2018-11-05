import numpy as np

num_var_types = 3
num_operators = 14

#semantics_cube = np.full([num_operators,num_var_types,num_var_types], -1)

sem_cube = np.array([[[ 0,  1,  -1],
        [ 1,  1,  -1],
        [ -1,  -1,  -1]], # '+'

        [[ 0,  1, -1],
        [ 1,  1, -1],
        [-1, -1, -1]], # '-'

        [[ 0,  1, -1],
        [ 1,  1, -1],
        [-1, -1, -1]], # '*'

        [[ 0,  1, -1],
        [ 1,  1, -1],
        [-1, -1, -1]], # '/'

        [[ -1, -1, -1],
        [-1, -1, -1],
        [-1, -1,  2]], # 'and'

        [[ -1, -1, -1],
        [-1, -1, -1],
        [-1, -1,  2]], # 'or'

        [[ -1, -1, -1],
        [-1, -1, -1],
        [-1, -1,  2]], # 'not'

        [[  0, -1, -1],
        [ 1,  1, -1],
        [-1, -1,  2]], # '='

        [[  2,  2, -1],
        [ 2,  2, -1],
        [-1, -1,  2]], # '=='

        # [[ -1, -1, -1],
        # [-1, -1, -1],
        # [-1, -1, -1]], # '~'

        [[  2,  2, -1],
        [ 2,  2, -1],
        [-1, -1, -1]], # '<'

        [[  2,  2, -1],
        [ 2,  2, -1],
        [-1, -1, -1]], # '>'

       [[ 2,  2, -1],
        [ 2,  2, -1],
        [-1, -1, -1]]]) # '<>'

# The cube is going to be managed in the following way:

#        int    float    bool
#  int
# float
#  bool

# Var types will be as follows:

var_types_dict = {
    "int" : 0,
    "float" : 1,
    "bool" : 2
}

# The 3rd dimension will be: 

# +   -   *   /   and   or   not   =   ==   ~   <   >   <>

operators_dict = {
    #"PLUSOP" : 0,
	"+" : 0,
    #"MINUSOP" : 1,
	"-" : 1,
    #"TIMESOP" : 2,
	"*" : 2,
    #"DIVIDEOP" : 3,
	"/" : 3,
	"and" : 4,
	"or" : 5,
	"not" : 6,
    #"EQUALOP" : 7,
	"=" : 7,
    #"EQUALSOP" : 8,
	"==" : 8,
    #"LESSOP" : 9,
	"<" : 9,
    #"MOREOP" : 10,
	">" : 10,
    #"DIFFOP" : 11
	"<>" : 11
}

#For '+'
# sem_cube[var_types["int"]][var_types["int"]][operators["PLUSOP"]] = var_types["int"]


#print(sem_cube)
