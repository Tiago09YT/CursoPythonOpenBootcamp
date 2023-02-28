class Alumno:
    nombre = None
    nota = 0
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        #la nota, basada en una escala de 0 a 5
        #aprueba con 3 o mas
       
    def imprimir(self):
            print("Nombre:",self.nombre,";Nota: ", self.nota)
    def resultado(self):
            if (self.nota>=3):
                print('Aprobo, su nota fue =',self.nota)
            else: 
                print('No aprobo, su nota fue =',self.nota)
    
santi = Alumno('Santi', 4)
santi.imprimir()
santi.resultado()