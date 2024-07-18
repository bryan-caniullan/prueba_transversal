import random
import csv
import math
import os


archivo_csv = "sueldo.csv"

trabajadores = ["Juan Perez", "Maria Garcia", "Carlos lopez" , "Ana Martinez" , "Pedro Rodriguez" , "Laura Hernandez" , "Miguel Sanchez" , "Isabel Gomez" , "Francisco Dias" , "Elena Fernandez"]
sueldos={}

#1
def sueldos_aleatoreos():
    for trabajadores in trabajadores:
        sueldos[trabajadores]= random.randint(300000,2500000)
        print("los sueldos son ")

def lee_sueldos_aleatoreos():
    while True:
        sueldos = input('Ingrese sueldo ')
        if sueldos_aleatoreos(sueldos):
            return(sueldos)
        else:
            print('sueldo fuera del rango')      
#2
def clasificar_sueldos():
    if sueldos:
        menores_800k = {k: v for k, v in sueldos.items() if v < 800000}
        entre_800k_2000k = {k: v for k, v in sueldos.items()if 800000 <= v <= 2000000}
        superiores_2000k = {k: v for k, v in sueldos.items()if v > 2000000}
        print (f"sueldo menores a 800000 total: {len(menores_800k)}")
        for trabajador, sueldo in menores_800k.items():
            print(f"{trabajador}  ${sueldo}")
            print()
        print(f"sueldos entre 800000 y 2000000 total: {len(entre_800k_2000k)} ")
        for trabajador, sueldo in menores_800k.items():
            print()
        print(f"sueldos supe superiro a 2000000 total: {len(superiores_2000k)}")
        for trabajador, sueldo in menores_800k.items():
            print()
            total_sueldos = sum(sueldos.values())
            print(f"total sueldo: ${total_sueldos}\n")
    else:
        print("favor ingresa un sueldo")        



        

#3
def ver_estadisticas():
    if sueldos:
        sueldos_valores = list(sueldos.values())
        promedio = sum(sueldos_valores) / len(sueldos_valores)
        max_sueldo = max(sueldos_valores)
        min_sueldo = min(sueldos_valores)
        media_geometrica = math.exp(sum(math.long(sueldo)) for sueldo in sueldos_valores) / len(sueldos_valores)
        print("estadisticas: ")
        print(f" promedio: ${promedio:2f}")
        print(f" maximo: ${max_sueldo}")
        print(f" minimo: ${min_sueldo}")
        print(f" media geometrica: ${media_geometrica:.2f}")
    else:
        print("el sueldo no a sido ingresadoooo")    
#4
def reporte_sueldos():
    
    if sueldos:
        print("reporte de los sueldos")
        for trabajador, sueldo in sueldo.items():
            descuento_salud = sueldo *0.07
            descuento_afp = sueldo *0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            print(f"{trabajador} ${sueldo} ${descuento_salud:.2f} ${descuento_afp:.2f}")
            print(f"{trabajador}: ${sueldo}")
        print()
    else:
        print("asignar el sueldo ") 

def guardar_sueldos_csv():
    
    whit open(archivo_csv,mode="w" newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["nombre","sueldo"])
    for trabajador, sueldos in sueldos.items():
        writer.writerow([trabajador, sueldos])
        print(f"sueldos guradado en {archivo_csv}.\n")
def cargar_sueldos_csv():
    if os.path.exists(archivo_csv):
        whit open(archivo_csv, mode ="r") file:
        reader = csv.reader(file)       

      

#5


def menu_principal():
    while True:
        print("\nMenú Principal")
        print("1. asignar sueldo")
        print("2. clasificar sueldos")
        print("3. ver estadisticas")
        print("4. reportes de sueldos")
        print("5. salir del programa")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            sueldos_aleatoreos()
        elif opcion == "3":
            ver_estadisticas()
        elif opcion == "4":
            reporte_sueldos
        elif opcion == "5":
            print("has salido del programa ")
            break
        else:
            print("opcion incorrecta querido profesor ")
menu_principal()    

          
           

