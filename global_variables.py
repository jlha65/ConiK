# estructura para tener datos que vamos necesitando
class global_variables:
    def __init__(self):
        self.currentId = ""
        self.currentType = ""
        self.currentScope = "GLOBAL"
        self.currentSize = 1
        self.currentVarsTable = None
        self.quadList = []
        self.quadCount = 0 #contador de cuadruplos
        self.paramCount = 0 #contador de parametros
gv = global_variables()
