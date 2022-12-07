class Perro:
    def __init__(self, nombre, color) -> None:
        self.nombre = nombre
        self.color = color
    def ladrar(self):
        print(f'El perro {self.nombre} está ladrando')
    def contar(self, str):
        print(f'El perro {self.nombre} nos quiere contar que {str}')

perro1 = Perro('pepe', 'rojo')

prro1 = Perro('pepe', 'rojo')
perro3 = Perro('Rober', 'azul')
perro1.ladrar()
perro3.ladrar()
perro1.contar('Se ha despetado de buen humor')
perro3.contar('Se ha levantado con el pie izquierdo')