#HERENCIA

class Animal:
    def __init__(self, especie):
        self.especie= especie
    
    def hacersonido (self):
        return "sonido desconocido"
    
class Gato (Animal) : #gato hereda animal
    def hacersonido(self):
        return "miau"
    
class Perro (Animal): #perro hereda animal
    def hacersonido(self):
        return "guau"
            
gato1= Gato ("Felino")
perro1= Perro ("Canino")

print (gato1.hacersonido())     #imprime Miau
print (perro1.hacersonido())    #imprime Guau

class Figura:
    def __init__(self, color):
        self.color= color
    
    def area (self):
        pass

class Cuadrado (Figura):
    def __init__(self, lado, color):
        super(). __init__(color)
        self.lado= lado

    def area (self):
        return self.lado ** 2

class Circulo (Figura):
    def __init__(self, radio, color):
        super().__init__(color)
        self.radio= radio

    def area(self):
        return 3.14159 * self.radio ** 2


mi_cuadrado= Cuadrado (5, "Rojo")
mi_circulo= Circulo (3, "Azul") 


print (f"Area del cuadrado: {mi_cuadrado.area()} unidades cuadradas ")
print (f"Area del circulo: {mi_circulo.area()} unidades cuadradas ")



class Humano:
    def __init__(self, genero):
        self.genero= genero
    
    def particularidad (self):
        return "particularidad desconocida"
    
class Hombre (Humano) : 
    def particularidad (self):
        return "pelo corto"
    
class Mujer (Humano): 
    def particularidad (self):
        return "pelo largo"
            
hombre1= Hombre ("Humamno")
mujer1= Mujer ("Humano")

print (hombre1.particularidad())
print (mujer1.particularidad())


class Coche: 
    def __init__(self, marca, modelo):
        self.marca: marca
        self.modelo: modelo
        self.velocidad: 0

    def acelerar( self, incremento):
        self.velocidad += incremento

        print (f"el coche {self.marca} {self.modelo} freno a {self.velocidad} km/h." )
    
    def frenar(self , decremento ):
        self.velocidad -= decremento

        print (f"el coche {self.marca} {self.modelo} freno a {self.velocidad} km/h.")

class Toyota (Coche): 
    def __init__(self, toyota, corolla):
        self.marca= toyota
        self.modelo= corolla
        self.velocidad= 100 

class Ford (Coche):
    def __init__(self, ford, mustang):
        self.marca= ford
        self.modelo= mustang
        self.velocidad= 150

coche1= Toyota (Coche)
coche2= Ford (Coche)





