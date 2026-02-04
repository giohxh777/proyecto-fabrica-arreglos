class Empleado_modelo:
    def __init__(self,nombre,apellido,cedula,celular):
        self.nombre_empleado=nombre
        self.aplellido_empleado=apellido 
        self.cedula_empleado= cedula
        self.telefono_empleado=celular
        
    def set_nombre_empleado(self, nuevo_nombre):
        self.nombre_empleado= nuevo_nombre
        
    def get_nombre_empleado(self):
        return self.nombre_empleado
    
    def set_apellido_empleado(self, nuevo_apellido):
        self.aplellido_empleado= nuevo_apellido
        
    def get_apellido_empleado(self):
        return self.aplellido_empleado
    
    def set_cedula_empleado(self, nueva_cedula):
        self.cedula_empleado= nueva_cedula
        
    def get_cedula_empleado(self):
        return self.cedula_empleado
    
    def set_telefono_empleado(self, nuevo_telefono):
        self.telefono_empleado= nuevo_telefono
        
    def get_telefono_empleado(self):
        return self.telefono_empleado
    
    def ver_info(self):
        info="nombre Empleado: " + self.nombre_empleado + " apellido empleado: " + self.aplellido_empleado
        info= info + ", Cedula: " + self.cedula_empleado + ", Telefono: " + self.telefono_empleado
        return info
        
        