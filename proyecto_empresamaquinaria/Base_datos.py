class Api_BD:
    def __init__(self):
        self.Api_datos = []
    
    def guardar_empleado(self, obj_nuevo_empleado):
        self.Api_datos.append(obj_nuevo_empleado)
        
    def imprimir_Api(self):
        for empleado in self.Api_datos:
            print(empleado)
            
    def extender_Api(self, lista_empleados):
        self.Api_datos.extend(lista_empleados)



