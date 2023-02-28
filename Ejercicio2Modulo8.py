import pickle
class Vehiculo:
    def __init__(self, Color, Marca, Precio):
        self.Color = Color
        self.Marca = Marca
        self.Precio = Precio
    
coche = Vehiculo('Rojo','Ferrari', 200000)
file = open ('coche.bin','wb')
pickle.dump(coche,file)
file.close()

file = open('coche.bin','rb')
coche = pickle.load(file)
file.close()
print(f'Tenemos un carro de color {coche.Color.lower()} de marca {coche.Marca} y con un precio de {coche.Precio}') 
