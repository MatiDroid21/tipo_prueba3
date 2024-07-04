import globales
import ventas
import estadisticas
import time
import os

os.system("cls")
def menu_estadisticas():
    while True:
        print("<=== Menu Estadisticas ===>")
        print("1. Mostrar Venta Más Alta")
        print("2. Mostrar Venta Más Baja")
        print("3. Promedio Ventas")
        print("4. Media Geométrica")
        print("5. Volver")
        
        opcion_estadisticas = globales.seleccionar_opcion(5)
        
        if opcion_estadisticas == 1:
            print("=== Venta Más Alta ===")
            estadisticas.venta_mas_alta()
        elif opcion_estadisticas == 2:
            print("=== Venta Más Baja ===")
            estadisticas.venta_mas_baja()
        elif opcion_estadisticas == 3:
            print("=== Promedio ===")
            estadisticas.obtener_promedio()
        elif opcion_estadisticas == 4:
            print("=== Media Geométrica ===")
            estadisticas.obtener_media()
        elif opcion_estadisticas == 5:
            return

def menu():
   while True:
        print("<=== Menu ===>")
        print("1. Precargar ventas")
        print("2. Estadisticas")
        print("3. Salir")
        print("---------------")
        opcion = globales.seleccionar_opcion(3)
        if opcion == 1:
            ventas.asignar_ventas_aleatorias()
        elif opcion == 2:
            menu_estadisticas()
        elif opcion == 3:
            print("Finalizando Programa ...")
            time.sleep(2) # para que el programa no cierre de golpe.
            return 
    

if __name__ == "__main__":
    menu()