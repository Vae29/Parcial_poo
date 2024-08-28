class Animales:
    def __init__(self,nombre,raza,edad,color):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
        self.color=color

mi_perro=Animales("Nacho","Mini Pincher","6 años","Negro")
print(type(mi_perro))
print(f"\n{mi_perro.nombre} \n{mi_perro.raza}\n{mi_perro.edad}\n{mi_perro.color}")

mi_gato=Animales("Tigger","Cola de Ardilla","1 año","Naranja atigrado")
print("////////////////////////////")
print(type(mi_gato))
print(f"\n{mi_gato.nombre}\n{mi_gato.raza}\n{mi_gato.edad}\n{mi_gato.color}")