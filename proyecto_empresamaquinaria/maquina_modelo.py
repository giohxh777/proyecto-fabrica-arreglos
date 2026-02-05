class Api_BD_maquinas:
    def __init__(self, codigo, nombre_maquina, modelo_maquina, estado_maquina):
        self.codigo = codigo
        self.nombre_maquina = nombre_maquina    
        self.modelo_maquina = modelo_maquina
        self.estado_maquina = estado_maquina
        
        self.api_maquinas = [
            ["codigo ","nombre maquina", "modelo maquina", "estado maquina"],
            ["cod 123","brazo mecanico","tx200 ","apagada"],
            ["cod 2034","banda transportadora","tx5000 ","requiere mantenimiento"],
            ["cod 3045","garra mecanica","px300 ","operativa"]
        ]
        
    def set_codigo_maquina(self, nuevo_codigo):
        self.codigo = nuevo_codigo
        
    def get_codigo_maquina(self):
        return self.codigo
    
    def set_nombre_maquina(self, nuevo_nombre):
        self.nombre_maquina = nuevo_nombre
    
    def get_nombre_maquina(self):
        return self.nombre_maquina
    
    def set_modelo_maquina(self, nuevo_modelo):
        self.modelo_maquina = nuevo_modelo
        
    def get_modelo_maquina(self):
        return self.modelo_maquina
    
    def set_estado_maquina(self, nuevo_estado):
        self.estado_maquina = nuevo_estado
        
    def get_estado_maquina(self):
        return self.estado_maquina
    
    def imprimir_info(self):
        for i in range(len(self.api_maquinas)):
            print(self.api_maquinas[i])
