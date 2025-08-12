class MaquinaJoyeria:
    def __init__(self, marca, modelo, tipo_material, encendida=False):
        self.__marca = marca
        self.__modelo = modelo
        self.__tipo_material = tipo_material 
        self.__encendida = encendida
    
    def get_marca(self):
        return self.__marca
    def get_modelo(self):
        return self.__modelo
    def get_tipo_material(self):
        return self.__tipo_material
    def get_encendida(self):
        return self.__encendida
    def set_marca(self, encendida ):
        self.__encendida=encendida

    def encender(self):
        if not self.encendida:
            self.encendida = True
            print("La máquina de joyería ha sido encendida.")
        else:
            print("La máquina ya está encendida.")

    def apagar(self):
        if self.encendida:
            self.encendida = False
            print("La máquina de joyería ha sido apagada.")
        else:
            print("La máquina ya está apagada.")

    def fabricar_joya(self, tipo_joya):
        if not self.encendida:
            print("Error: La máquina está apagada. Enciéndela para fabricar joyas.")
            return
        print(f"Fabricando una joya de tipo {tipo_joya} con material {self.__tipo_material}.")

    def __str__(self):
        estado = "Encendida" if self.encendida else "Apagada"
        return f"Máquina de Joyería {self.__marca} {self.__modelo} ({self.__tipo_material}) - {estado}"
