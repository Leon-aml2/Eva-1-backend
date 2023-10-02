from Tecno import Tecno
class TV(Tecno):
    def __init__(self, voltaje, eficiencia, precio, marca, pulgadas):
        super().__init__(voltaje, eficiencia, precio, marca)
        self.__pulgadas = pulgadas

    # getters y setters

    def get_pulgadas(self):
        return self.__pulgadas
    
    def set_pulgadas(self, pulgadas:int):
        self.__pulgadas = pulgadas
    
    # descuento
        
    def calcular_descuento(self,tupla_tv):
        # super().calcular_descuento(tupla_tv)
        pass
        
    #lista
    
    def revisar_televisores(lista_tv):
        if len(lista_tv)>0:
            vaina = [...,lista_tv]
            op = input("¿cotizar televisores? (s/n):  ")
            if op == "s":
                TV.cotizar_televisores(vaina)
            else:
                pass
        else:
            pass
        print(f"Televisores:     {vaina}")
        
    def cotizar_televisores(vaina):
        for j in vaina:
            j = 1
            lista_tv = vaina[j]
            cero =0
            for i in lista_tv:
                    tupla_tv = lista_tv[cero]            
                    desc_optimo = float(lista_tv[cero][2])
                    eficiencia_mas = lista_tv[cero][1]       
                    if eficiencia_mas == "a" or eficiencia_mas == "b":
                        descuento = desc_optimo-(desc_optimo*.5)
                    elif eficiencia_mas == "c" or eficiencia_mas == "d":
                        descuento = desc_optimo-(desc_optimo*.3)
                    elif eficiencia_mas == "e" or eficiencia_mas == "f":
                        descuento = desc_optimo-(desc_optimo*.1)
                    else:
                        ("carácter desconocido")
                    print(f"tv: {tupla_tv} y descuento ya incluido: {descuento}")
                    continuar = input("¿siguiente? (s/n):   ")
                    if continuar == "s":
                        cero+=1
                    else:
                        pass
                    
        

        
        