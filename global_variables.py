# estructura para tener datos que vamos necesitando
class global_variables:
    def __init__(self):
        self.currentId = ""
        self.currentType = ""
        self.currentScope = "GLOBAL"
        self.currentSize = 1
        self.currentVarsTable = None
        self.currentModCall = "" #module call que se está haciendo
        self.quadList = []
        self.quadCount = 0 #contador de cuadruplos
        self.paramCount = 0 #contador de parametros
        self.saveCount = 0 #usado en el loop para guardar cuantos quads van
gv = global_variables()
