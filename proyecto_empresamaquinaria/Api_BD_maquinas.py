class Api_BD_maquinas:
    def __init__(self):
        self.api_maquinas = [
            ["codigo ","nombre maquina", "modelo maquina", "estado maquina"],
            ["cod 123","brazo mecanico","tx200 ","apagada"],
            ["cod 2034","banda transportadora","tx5000 ","requiere mantenimiento"],
            ["cod 3045","garra mecanica","px300 ","operativa"]
        ]
    
    
    
    def imprimir_info(self):
        for i in range(len(self.api_maquinas)):
            print(self.api_maquinas[i])
            
    def buscar_info(self):
        return self.api_maquinas[2][2]
   
    
