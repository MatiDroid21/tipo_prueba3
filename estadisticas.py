import globales
import math # esto nos ayudara con los promedios.

def venta_mas_alta():
    todas_las_ventas = globales.leer_archivo_json("./ventas.json")
    todos_los_trabajadores = globales.leer_archivo_json("./trabajadores.json") #quiero intentar algo
    
    ventas_ordenadas = sorted(todas_las_ventas, key=lambda x: x["venta"], reverse=True)
    
    for venta in ventas_ordenadas[:1]:
        nombre_trabajador = ""
        for trabajador in todos_los_trabajadores:
            if trabajador['trabajador'] == venta['trabajador']:
                nombre_trabajador = trabajador['trabajador']
                
        print(f"{nombre_trabajador} -- {venta['venta']}")
        input("Presione Enter Para Continuar")
        
def venta_mas_baja():
    todas_las_ventas = globales.leer_archivo_json("./ventas.json")
    todos_los_trabajadores = globales.leer_archivo_json("./trabajadores.json") #quiero intentar algo
    
    ventas_ordenadas = sorted(todas_las_ventas, key=lambda x: x["venta"], reverse=False)
    
    for venta in ventas_ordenadas[:1]:
        nombre_trabajador = ""
        for trabajador in todos_los_trabajadores:
            if trabajador['trabajador'] == venta['trabajador']:
                nombre_trabajador = trabajador['trabajador']
                
        print(f"{nombre_trabajador} -- {venta['venta']}")
        input("Presione Enter Para Continuar")
        
def obtener_media():
    todas_las_ventas = globales.leer_archivo_json("./ventas.json")
    
    suma_ventas = 0
    cantidad_ventas = 0
    
    for venta in todas_las_ventas:
        suma_ventas += math.log(venta['venta'])
        cantidad_ventas += 1
    
    media_geometrica = math.exp(suma_ventas / cantidad_ventas)
    print(media_geometrica)
    return media_geometrica

def obtener_promedio():
    
    todas_las_ventas = globales.leer_archivo_json("./ventas.json")
    suma_ventas = 0
    cantidad_ventas = 0
    
    for venta in todas_las_ventas:
        suma_ventas += venta['venta']
        cantidad_ventas += 1
        
    promedio = suma_ventas / cantidad_ventas
    
    print(promedio)
    return promedio