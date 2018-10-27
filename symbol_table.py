SYM_TABLE = dict()
GLOBAL = dict()

#cuScope = "GLOBAL"

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
	#if SYM_TABLE[cuScope]:
		#print(SYM_TABLE[scope])
		if id in SYM_TABLE[scope]:
		#if id in SYM_TABLE[cuScope]:
			print("variable already declared in scope:: " + id)
		else:
			SYM_TABLE[scope][id] = dict()
			#SYM_TABLE[cuScope][id] = dict()
			SYM_TABLE[scope][id]["type"] = data_type
			#SYM_TABLE[cuScope][id]["type"] = data_type
	else:
		SYM_TABLE[scope][id] = dict()
		SYM_TABLE[scope][id]["type"] = data_type
		
def add_module(id,return_type):

	if id in SYM_TABLE:
		print("module already declared:: " + id)
	else:
		SYM_TABLE[id] = dict()
		SYM_TABLE[id]["return"] = return_type