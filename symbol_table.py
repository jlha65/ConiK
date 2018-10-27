SYM_TABLE = dict()
GLOBAL = dict()

#lista de informacion de la variable
#   name|type|params|scope|table
a = ["example","int",[],2,[]]
b = ["joseLuis","float",[],2,a]

#GLOBAL["example"] = a
#GLOBAL["jl"] = b

SYM_TABLE["GLOBAL"] = GLOBAL

#print(SYM_TABLE["global"])

def add_variable(scope, id, data_type):

	if SYM_TABLE[scope]:
		#print(SYM_TABLE[scope])
		if id in SYM_TABLE[scope]:
			print("variable already declared in scope:: " + id)
		else:
			SYM_TABLE[scope][id] = dict()
			SYM_TABLE[scope][id]["type"] = data_type
	else:
		SYM_TABLE[scope][id] = dict()
		SYM_TABLE[scope][id]["type"] = data_type