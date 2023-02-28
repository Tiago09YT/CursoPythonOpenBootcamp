class Alumno:
    nombre = None
    nota = 0
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        #la nota, basada en una escala de 0 a 5
        #aprueba con 3 o mas
        if (nota>=3):
            print('Aprobo, su nota fue =',self.nota)
        else: 
            print('No aprobo, su nota fue =',self.nota)
    def __repr__(self):
        return str(self.__dict__)
    
santi = Alumno('Santi', 4)