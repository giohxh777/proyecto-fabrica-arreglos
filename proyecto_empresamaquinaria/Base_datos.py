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


empleado_1 = "Empleado 1: jonnatan Rueda 1093591113 321-7297443"
empleado_2 = "Empleado 2: Carlos Perez 52370510 321-7297444"
empleado_3 = "Empleado 3: Ana Gomez 13717353 321-7297445"

empleados = [empleado_1, empleado_2, empleado_3]
empleados_adicionales = [empleado_2, empleado_3]

api = Api_BD()

for empleado in empleados:
    api.guardar_empleado(empleado)

print("Lista inicial:")
api.imprimir_Api()

api.guardar_empleado(empleado_1)
api.imprimir_Api()

api.extender_Api(empleados_adicionales)
api.imprimir_Api()

api.Api_datos.insert(0, empleado_3)
api.imprimir_Api()

api.Api_datos.pop(1)
api.imprimir_Api()

api.Api_datos.remove(empleado_2)
api.imprimir_Api()

print(f"Índice de empleado 3: {api.Api_datos.index(empleado_3)}")
print(f"Cantidad de empleado 3: {api.Api_datos.count(empleado_3)}")

api.Api_datos.sort()
api.imprimir_Api()

api.Api_datos.reverse()
api.imprimir_Api()





