class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"El coche {self.marca} {self.modelo} aceleró a {self.velocidad} km/h.")

    def frenar(self, decremento):
        self.velocidad -= decremento
        print(f"El coche {self.marca} {self.modelo} frenó a {self.velocidad} km/h.")
# Crear objetos de la clase Coche
coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Ford", "Mustang")

# Interactuar con los objetos
coche1.acelerar(30)
coche2.acelerar(45)
coche1.frenar(10)
coche2.frenar(15)
