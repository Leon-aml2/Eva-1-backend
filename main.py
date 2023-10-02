from Tecno import Tecno
from Tv import TV
from Consola import Consola
from Scooter import Scooter

lista_tv = []
lista_consola = []
lista_scooter = []

def menu():
    opcion = "s"
    while opcion == "s":
        
        print("Referencie UNA OPCIÓN DEL MENÚ")
        print("1: Registrar")
        print("2: Cotizar")
        op = input("(NUMBER 1 OR 2 )    ")
        if op.lower()=="1" or op.lower()=="2":
            menu_menu(int(op))
        else:
            print("Por favor, coloque una opción que si exista")
        
        print("¿Continuar...?")
        opcion = input("(s = si / n = no)   ")
        

def menu_menu(opcion:int):
    if opcion == 1:
        apartado_registro()
    else:
        apartado_cotiza()
        
def apartado_registro():
    print("Bienvenido al apartado de registro")
    print("¿Qué componente desea ingresar?")
    print("1: TV")
    print("2: Consola")
    print("3: Scooter")
    op = input("(NUMBER 1 OR 2 OR 3 )    ")
    if op.lower()=="1":
        registrar_TV()
    elif op.lower()=="2":
        registrar_consola()
    elif op.lower()=="3":
        registrar_scooter()
    else:
        print("Por favor, coloque una opción que si exista")


#Tecno

def registrar_TV():
    print("Registro de Televisión activado!!")
    
    opcion = "s"
    while opcion == "s":
    
        print("")
        voltage = int(input("Ingrese el Voltaje:    "))
        if voltage > 100 and voltage != str:
            pass
        else:
            print("Función desconocida")
        print("")
        #eficiencia
        efficiency = input("Ingrese el Eficiencia (minúscula):  ")
        if efficiency.lower() == "a" or efficiency.lower() == "b" or efficiency.lower() == "c" or efficiency.lower() == "d" or efficiency.lower() == "e" or efficiency.lower() == "f" and efficiency != "":
            efficiency.lower()
            pass
        else:
            print("Función desconocida")
        print("")
        price = float(input("Ingrese el Precio:    "))
        if price != 0 and price != str:
            pass
        else:
            print("Función desconocida")
        print("")
        #marca
        brand = input("Ingrese el Marca:    ")
        if brand != 0 and brand != "":
            pass
        else:
            print("Función desconocida")
        print("")
        inch = int(input("Ingrese Pulgadas: "))
        if inch != str and 20 <= inch:
            pass
        
        tupla_tv = TV(voltage,efficiency,price,brand,inch)
        lista_tv.append((tupla_tv.get_voltaje(),tupla_tv.get_eficiencia(),tupla_tv.get_precio(),tupla_tv.get_marca(),tupla_tv.get_pulgadas()))
        # cotizar_TV(lista_tv)
        
        # TV.cotizar_televisores(lista_tv)
        
        opcion = input("Desea continuar ingresando (s/n):    ")
        if opcion == "s":
            op= input("¿Desea revisar el(los) producto(os) hasta el momento integrado? (s/n): ")
            if op == "s":
                TV.revisar_televisores(lista_tv)
            else:
                opcion == "s"
        else:
            TV.revisar_televisores(lista_tv)
            
    return lista_tv


def registrar_consola():
    opcion = "s"
    while opcion == "s":
    
        print("")
        voltage = int(input("Ingrese el Voltaje:    "))
        if voltage > 100 and voltage != str:
            pass
        else:
            print("Función desconocida")
        print("")
        efficiency = input("Ingrese el Eficiencia (minúscula):  ")
        if efficiency.lower() == "a" or efficiency.lower() == "b" or efficiency.lower() == "c" or efficiency.lower() == "d" or efficiency.lower() == "e" or efficiency.lower() == "f" and efficiency != "":
            efficiency.lower()
            pass
        else:
            print("Función desconocida")
        print("")
        price = float(input("Ingrese el Precio:    "))
        if price != 0 and price != str:
            pass
        else:
            print("Función desconocida")
        print("")

        brand = input("Ingrese el Marca:    ")
        if brand != 0 and brand != "":
            pass
        else:
            print("Función desconocida")
        print("")
        name_console = input("Ingrese Nombre de la consola: ")
        if price != 0 and price != "":
            pass
        print("")
        versions = input("Ingrese Versión: ")
        if price != 0 and price != "":
            pass
        
        tupla_consola = Consola(voltage,efficiency,price,brand,name_console,versions)
        lista_consola.append((tupla_consola.get_voltaje(),tupla_consola.get_eficiencia(),tupla_consola.get_precio(),tupla_consola.get_marca(),tupla_consola.get_nombre_consola(),tupla_consola.get_version()))
        
        opcion = input("Desea continuar ingresando (s/n):    ")
        if opcion == "s":
            op= input("¿Desea revisar el(los) producto(os) hasta el momento integrado? (s/n): ")
            if op == "s":
                Consola.revisar_consolas(lista_consola)
            else:
                opcion == "s"
        else:
            Consola.revisar_consolas(lista_consola)
            
    return lista_consola

#para cotizar, ¿hay que definir el tipo de dato?; cotizar_TV(opcion:float)
def cotizar_TV(lista_tv):
    TV.revisar_televisores(lista_tv)

def cotizar_consola(lista_consola):
    Consola.revisar_consolas(lista_consola)


def apartado_cotiza():
    print("Bienvenido al apartado de Venta y Consulta de Precios")
    print("¿Qué componente desea cotizar?")
    print("1: TV")
    print("2: Consola")
    print("3: Scooter")
    op = input("(NUMBER 1 OR 2 OR 3)    ")
    if op.lower()=="1":
        cotizar_TV()
    elif op.lower()=="2":
        cotizar_consola()
    elif op.lower()=="3":
        cotizar_scooter()
    else:
        print("Por favor, coloque una opción que si exista")

#Sport

def registrar_bicicleta():
    pass

def registrar_scooter():
    print("Registro de Scooter activado!!")
    
    opcion = "s"
    while opcion == "s":
    
        print("")
        voltage = int(input("Ingrese el Voltaje:    "))
        if voltage > 100 and voltage != str:
            pass
        else:
            print("Función desconocida")
        print("")
        #eficiencia
        efficiency = input("Ingrese el Eficiencia (minúscula):  ")
        if efficiency.lower() == "a" or efficiency.lower() == "b" or efficiency.lower() == "c" or efficiency.lower() == "d" or efficiency.lower() == "e" or efficiency.lower() == "f" and efficiency != "":
            efficiency.lower()
            pass
        else:
            print("Función desconocida")
        print("")
        price = float(input("Ingrese el Precio:    "))
        if price != 0 and price != str:
            pass
        else:
            print("Función desconocida")
        print("")
        #marca
        brand = input("Ingrese el Marca:    ")
        if brand != 0 and brand != "":
            pass
        else:
            print("Función desconocida")
        print("")
        hoop = int(input("Ingrese N° Aro: "))
        if hoop != str and hoop !=0:
            pass
        print("")
        weight = float(input("Ingrese Peso: "))
        if weight != str and 20 <= weight:
            pass
        print("")
        speeds = int(input("Ingrese Cantidad de velocidades: "))
        if speeds >= 0 and 6 <= speeds:
            pass
        
        tupla_scooter= Scooter(voltage,efficiency,price,brand,hoop,speeds,weight)
        lista_scooter.append((tupla_scooter.get_voltaje(),tupla_scooter.get_eficiencia(),tupla_scooter.get_precio(),tupla_scooter.get_marca(),tupla_scooter.get_aro(),tupla_scooter.get_velocidades(),tupla_scooter.get_peso()))

        opcion = input("Desea continuar ingresando (s/n):    ")
        if opcion == "s":
            op= input("¿Desea revisar el(los) producto(os) hasta el momento integrado? (s/n): ")
            if op == "s":
                Scooter.revisar_scooter(lista_scooter)
            else:
                opcion == "s"
        else:
            Scooter.revisar_scooter(lista_scooter)
            
    return lista_scooter

def cotizar_bicicleta():
    pass

def cotizar_scooter(lista_scooter):
    Scooter.revisar_scooter(lista_scooter)


print("Bienvenido")
menu()