class Persona:
    def __init__(self,nombre,edad,estatura,peso,ocupacion):
        self.nombre=nombre
        self.edad=edad
        self.estatura=estatura
        self.peso=peso
        self.ocupacion=ocupacion

isabella=Persona("Isabella","19","1,59","60kg","Estudiante")
valery=Persona("Valery","17", "1,61", "55kg","Estudiante")

print(type(isabella))
print(f"{isabella.nombre}\n{isabella.edad}\n{isabella.estatura}\n{isabella.peso}\n{isabella.ocupacion}")

print("////////////////////////////")
print(type(valery))
print(f"{valery.nombre}\n{valery.edad}\n{valery.estatura}\n{valery.peso}\n{valery.ocupacion}")