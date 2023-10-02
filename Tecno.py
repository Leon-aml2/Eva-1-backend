class Tecno:
    def __init__(self, voltaje, eficiencia, precio, marca):
        self.__voltaje = voltaje
        self.__precio = precio
        self.__marca = marca
        self.__eficiencia = eficiencia
        if eficiencia == "a" or "b":
            self.__descuento_eficiente = 0.5
        elif eficiencia == "c" or "d":
            self.__descuento_eficiente = 0.3
        elif eficiencia == "c" or "d":
            self.__descuento_eficiente = 0.1
        else:
            ("carácter desconocido")
    #getters

    def get_voltaje(self):
        return self.__voltaje
    
    def get_precio(self):
        return self.__precio
    
    def get_marca(self):
        return self.__marca
    
    def get_eficiencia(self):
        return self.__eficiencia
    
    #setters

    def set_voltaje(self, voltaje):
        self.__voltaje = voltaje
    
    def set_precio(self, precio):
        self.__precio = precio
    
    def set_marca(self, marca):
        self.__marca = marca
    
    def set_eficiencia(self, eficiencia):
        self.__eficiencia = eficiencia

    # def calcular_descuento(self,desc_optimo:float):
    #     desc_optimo = self.__precio - (self.__precio * self.__descuento_eficiente)
        
    #     return desc_optimo