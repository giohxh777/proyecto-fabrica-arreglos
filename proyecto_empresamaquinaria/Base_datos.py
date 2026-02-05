class Api_BD:
    def __init__(self):
        self.Api_datos = []
    
    def guardar_empleado(self, obj_nuevo_empleado):
        self.Api_datos.append(obj_nuevo_empleado)
        
    def imprimir_Api(self):
        for empleado in self.Api_datos:
            print(empleado.ver_info())
            
    def extender_Api(self, lista_empleados):
        self.Api_datos.extend(lista_empleados)
        
    def insertar_empleado(self, posicion, obj_nuevo_empleado):
        self.Api_datos.insert(posicion, obj_nuevo_empleado)
        
    def eliminar_empleado_por_indice(self, indice):
        self.Api_datos.pop(indice)
        
    def remover_empleado_por_cedula(self, cedula):
        for empleado in self.Api_datos:
            if empleado.get_cedula_empleado() == cedula:
                self.Api_datos.remove(empleado)
        
    def obtener_indice_empleado(self, cedula):
        for i, empleado in enumerate(self.Api_datos):
            if empleado.get_cedula_empleado() == cedula:
                return i
        return -1
        
    def contar_empleados(self):
        return len(self.Api_datos)
        
    def ordenar_empleados_por_nombre(self):
        nombres = []
        for empleado in self.Api_datos:
            nombres.append(empleado.get_nombre_empleado())
        nombres.sort()
        empleados_ordenados = []
        for nombre in nombres:
            for empleado in self.Api_datos:
                if empleado.get_nombre_empleado() == nombre:
                    empleados_ordenados.append(empleado)
                    break
        self.Api_datos = empleados_ordenados
        
    def invertir_orden_empleados(self):
        self.Api_datos.reverse()
        
    def buscar_empleado_por_cedula(self, cedula):
        for empleado in self.Api_datos:
            if empleado.get_cedula_empleado() == cedula:
                return empleado
        return None
        
    def obtener_todos_empleados(self):
        return self.Api_datos






