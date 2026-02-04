from empleado_modelo import Empleado_modelo  
from Base_datos import Api_BD
from Api_BD_maquinas import Api_BD_maquinas

obj_Api= Api_BD()
obj_Api_maquinas = Api_BD_maquinas()
obj_Api_maquinas.imprimir_info()
print (obj_Api_maquinas.buscar_info())
obj_empleado = Empleado_modelo ("jonnatan" ,"Rueda" ,"1093591113","321-7297443")
obj_empleado2 = Empleado_modelo ("Carlos" ,"Perez" ,"52370510","321-7297444")
obj_empleado3 = Empleado_modelo ("Ana" ,"Gomez" ,"13717353","321-7297445")
obj_Api.guardar_empleado (obj_empleado2)
obj_Api.guardar_empleado (obj_empleado)
obj_Api.guardar_empleado (obj_empleado3)
obj_Api.imprimir_Api()