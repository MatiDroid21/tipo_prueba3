import globales
import random

def asignar_ventas_aleatorias():
    trabajadores = globales.leer_archivo_json("./trabajadores.json") # cargamos a los trabajadores. 
    ventas = globales.leer_archivo_json("./ventas.json") # cargamos las ventas
    
    for i in range(10): #10 por las cantidad de ventas solicitadas
        try:
            trabajador = random.choice(trabajadores)['trabajador']
            venta = random.randint(1500000, 5000000)
            
            nueva_venta = {
                "trabajador":trabajador,
                "venta":venta
            }
            ventas.append(nueva_venta)
        except:
           print("Algo paso perro")
    globales.guardar_archivo_json("ventas.json",ventas)
    print("Ventas Cargadas. ")
    input("Presione Enter para continuar.")