
class Vehiculo:
    Color = None
    Ruedas = 0
    Puertas = 0
    def __init__(self, Color,Ruedas,Puertas):
        self.Color= Color
        self.Ruedas= Ruedas
        self.Puertas=Puertas
class Coche(Vehiculo):
    Velocidad = 0
    Cilindrada = 0
    def __init__(self,Color, Ruedas, Puertas, Velocidad, Cilindrada):
        #super(Coche,self).__init__()
        self.Color= Color
        self.Ruedas= Ruedas
        self.Puertas=Puertas
        self.Velocidad=Velocidad
        self.Cilindrada=Cilindrada
    def __repr__(self):
        return str(self.__dict__)

coche = Coche("color" , 4, 4, 120,125)
print(coche)