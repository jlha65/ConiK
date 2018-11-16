SYM_TABLE = dict()
GLOBAL = dict()

#cuScope = "GLOBAL"

#lista de informacion de la variable
#   name|type|params|scope|table


SYM_TABLE["GLOBAL"] = GLOBAL

#print(SYM_TABLE["global"])

def add_variable(scope, id, data_type, size, address):
	print("Adding variable to var table: ")
	print("Scope: " + str(scope))
	print("Id: " + str(id))
	print("data_type: " + str(data_type))
	print("size: " + str(size))
	print("address: " + str(address))

	if not SYM_TABLE["GLOBAL"]: #First variable
		SYM_TABLE[scope][id] = dict()
		#SYM_TABLE[cuScope][id] = dict()
		SYM_TABLE[scope][id]["#type"] = data_type
		SYM_TABLE[scope][id]["#size"] = size
		SYM_TABLE[scope][id]["#address"] = address
		#SYM_TABLE[cuScope][id]["type"] = data_type
    #if scope in SYM_TABLE:
	elif SYM_TABLE[scope]:
	#if SYM_TABLE[cuScope]:
		#print(SYM_TABLE[scope])
		if id in SYM_TABLE[scope]:
		#if id in SYM_TABLE[cuScope]:
			raise Exception("variable already declared in scope: " + id)
		else:
			SYM_TABLE[scope][id] = dict()
			#SYM_TABLE[cuScope][id] = dict()
			SYM_TABLE[scope][id]["#type"] = data_type
			SYM_TABLE[scope][id]["#size"] = size
			SYM_TABLE[scope][id]["#address"] = address
			#SYM_TABLE[cuScope][id]["type"] = data_type
	else:
		SYM_TABLE[scope][id] = dict()
		SYM_TABLE[scope][id]["#type"] = data_type
		
def add_module(id,return_type):

	if id in SYM_TABLE:
		raise Exception("module already declared:: " + id)
	else:
		SYM_TABLE[id] = dict()
		SYM_TABLE[id]["return"] = return_type

def add_num_param(scope):
	SYM_TABLE[scope]["#params"] = len(SYM_TABLE[scope]) - 1

def add_num_vars(scope):
	SYM_TABLE[scope]["#vars"] = len(SYM_TABLE[scope]) - SYM_TABLE[scope]["#params"] - 1

#add to a function the number of quad where it starts
def add_num_quad(scope, quadCount):
	SYM_TABLE[scope]["#quad"] = quadCount
#get from a function the number of quad where it starts
def get_num_quad(scope):
	return SYM_TABLE[scope]["#quad"]

def add_param_type_list(scope, tlist):
	SYM_TABLE[scope]["#typeList"] = tlist
def get_param_type_list(scope):
	return SYM_TABLE[scope]["#typeList"]

def get_return_type(scope, id):
	if id in SYM_TABLE[scope]:
		return SYM_TABLE[scope][id]["#type"]
	elif id in SYM_TABLE["GLOBAL"]:
		return SYM_TABLE["GLOBAL"][id]["#type"]
	else:
		raise Exception("There is no \"" + id + "\" variable in this scope")

def get_size(scope, id):
	return SYM_TABLE[scope][id]["#size"]

def mod_exist(scope):
	if scope in SYM_TABLE:
		return SYM_TABLE[scope]
	else:
		raise Exception("There is no \"" + scope + "\" scope")

def get_var_address(scope,id):
	print(SYM_TABLE)
	if id in SYM_TABLE[scope]:
		return SYM_TABLE[scope][id]["#address"]
	elif id in SYM_TABLE["GLOBAL"]:
		return SYM_TABLE["GLOBAL"][id]["#address"]
	else:
		raise Exception("There is no \"" + id + "\" variable in this scope")