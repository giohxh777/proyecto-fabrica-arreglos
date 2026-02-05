from empleado_modelo import Empleado_modelo  
from Base_datos import Api_BD
from Api_BD_maquinas import Api_BD_maquinas

obj_Api = Api_BD()
obj_Api_maquinas = Api_BD_maquinas()

obj_Api_maquinas.imprimir_info()
print(obj_Api_maquinas.buscar_info())

obj_empleado = Empleado_modelo("Jonnatan", "Rueda", "1093591113", "321-7297443")
obj_empleado2 = Empleado_modelo("Carlos", "Perez", "52370510", "310-3328600")
obj_empleado3 = Empleado_modelo("Ana", "Gomez", "13717353", "321-9214833")

obj_Api.guardar_empleado(obj_empleado)
obj_Api.guardar_empleado(obj_empleado2)
obj_Api.guardar_empleado(obj_empleado3)
obj_Api.imprimir_Api()

obj_empleado4 = Empleado_modelo("Camila", "Cuellar", "1091973885", "321-5893022")
obj_Api.guardar_empleado(obj_empleado4)
obj_Api.imprimir_Api()

obj_Api.insertar_empleado(0, Empleado_modelo("Maria", "Sanchez", "87654321", "321-9876543"))
obj_Api.imprimir_Api()

obj_Api.obtener_indice_empleado("52370510")
obj_Api.contar_empleados()

obj_Api.ordenar_empleados_por_nombre()
obj_Api.imprimir_Api()

obj_Api.invertir_orden_empleados()
obj_Api.imprimir_Api()


