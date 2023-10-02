from Tecno import Tecno
class Scooter(Tecno):
    def __init__(self, voltaje, eficiencia, precio, marca,aro, velocidades, peso):
        super().__init__(voltaje, eficiencia, precio, marca)
        self.__aro = aro
        self.__velocidades = velocidades
        self.__peso = peso
            
    def get_aro(self):
        return self.__aro
    
    def get_velocidades(self):
        return self.__velocidades
    
    def get_peso(self):
        return self.__peso
    
    def set_aro(self,aro):
        self.__aro = aro
    
    def set_velocidades(self,velocidades):
        self.__velocidades = velocidades
        
    def set_peso(self,peso):
        self.__peso = peso

    def revisar_scooter(lista_scooter):
        if len(lista_scooter)>0:
            vaina = [...,lista_scooter]
            op = input("¿cotizar escooters? (s/n):  ")
            if op == "s":
                Scooter.cotizar_scooters(vaina)
            else:
                pass
        else:
            pass
        print(f"Scooters:     {vaina}")
        
    def cotizar_scooters(vaina):
        for j in vaina:
            j = 1
            lista_scooter = vaina[j]
            cero =0
            for i in lista_scooter:
                    tupla_scooter = lista_scooter[cero]            
                    desc_optimo = float(lista_scooter[cero][2])
                    peso_mas = float(lista_scooter[cero][6])
                    if peso_mas > 10:
                        costo_despacho = 300* peso_mas
                    eficiencia_mas = lista_scooter[cero][1]
                    if eficiencia_mas == "a" or eficiencia_mas == "b":
                        descuento = desc_optimo-(desc_optimo*.5)
                    elif eficiencia_mas == "c" or eficiencia_mas == "d":
                        descuento = desc_optimo-(desc_optimo*.3)
                    elif eficiencia_mas == "e" or eficiencia_mas == "f":
                        descuento = desc_optimo-(desc_optimo*.1)
                    else:
                        ("carácter desconocido")
                    print(f"tv: {tupla_scooter} y descuento ya incluido: {descuento} y costo total (más despacho): {costo_despacho+descuento}")
                    continuar = input("¿siguiente? (s/n):   ")
                    if continuar == "s":
                        cero+=1
                    else:
                        pass