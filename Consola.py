from Tecno import Tecno
class Consola(Tecno):
    def __init__(self, voltaje, eficiencia, precio, marca,nombre_consola,version):
        super().__init__(voltaje, eficiencia, precio, marca)
        self.__nombre_consola = nombre_consola
        self.__version = version
        if version.lower()=="lite":
            self.__descuento_version = .05
            
    def get_nombre_consola(self):
        return self.__nombre_consola
    
    def get_version(self):
        return self.__version
    
    def set_nombre_consola(self,nombre_consola):
        self.__nombre_consola = nombre_consola
        
    def set_version(self,version):
        self.__version = version

    def revisar_consolas(lista_consola):
        if len(lista_consola)>0:
            vaina = [...,lista_consola]
            op = input("¿cotizar consolas? (s/n):  ")
            if op == "s":
                Consola.cotizar_consolas(vaina)
            else:
                pass
        else:
            pass
        print(f"Consolas:     {vaina}")
        
    def cotizar_consolas(vaina):
        for j in vaina:
            j = 1
            lista_consola = vaina[j]
            cero =0
            for i in lista_consola:
                    tupla_consola = lista_consola[cero]            
                    desc_optimo = float(lista_consola[cero][2])                    
                    eficiencia_mas = lista_consola[cero][1]  
                    if eficiencia_mas == "a" or eficiencia_mas == "b":
                        descuento = desc_optimo-(desc_optimo*.5)
                    elif eficiencia_mas == "c" or eficiencia_mas == "d":
                        descuento = desc_optimo-(desc_optimo*.3)
                    elif eficiencia_mas == "e" or eficiencia_mas == "f":
                        descuento = desc_optimo-(desc_optimo*.1)
                    else:
                        ("carácter desconocido")
                    version_mas = lista_consola[cero][5]
                    if version_mas == "lite":
                        mini_descuento = descuento-(descuento*.05)
                        print(f"tv: {tupla_consola} y descuento ya incluido: {mini_descuento}")
                    else:
                        print(f"tv: {tupla_consola} y descuento ya incluido: {descuento}")
                    continuar = input("¿siguiente? (s/n):   ")
                    if continuar == "s":
                        cero+=1
                    else:
                        pass
    