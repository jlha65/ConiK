# estructura para tener datos que vamos necesitando
class global_variables:
    def __init__(self):
        self.currentId = ""
        self.currentType = ""
        self.currentScope = "GLOBAL"
        self.currentSize = 1
        self.currentVarsTable = None
        self.currentModCall = "" #module call que se esta haciendo
        self.quadList = []
        self.quadCount = 0 #contador de cuadruplos
        self.paramCount = 0 #contador de parametros
        self.saveCount = 0 #usado en el loop para guardar cuantos quads van
        self.counterVm = 0 #apuntador de cuadruplos de VM
        self.currentQuad = [] #list of quads for the ENDPROC to return to
        self.nextModule = "" #next module to be visited, used for PARAM OpCode
        self.flagReturn = False #checks if there is a return in a module
        self.retValue = 0 #value or address that is returned
        self.currentArrAddress = 0
        self.currentArrAddressL = 0
        self.minusFlag = False # Para numeros negativos
        self.flagColor = False #Para el plot, color o no?
        self.plotName = "" #Para el plot, guarda nombre
        self.plotColor = "" #Para plot, guarda el color
gv = global_variables()
