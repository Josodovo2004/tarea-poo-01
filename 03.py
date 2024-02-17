class Animal():
    def __init__(self, __nombre, __edad) -> None:
        self.nombre = __nombre
        self.edad = __edad
    def hacer_sonido(self):
        print('aaaaaaaaa')

class Gato(Animal):
    def __init__(self, __nombre, __edad) -> None:
        super().__init__(__nombre, __edad)

    def hacer_sonido(self):
        print('Miau')

class Perro(Animal):
    def __init__(self, __nombre, __edad) -> None:
        super().__init__(__nombre, __edad)

    def hacer_sonido(self):
        print('Wof')

class Serpiente(Animal):
    def __init__(self, __nombre, __edad) -> None:
        super().__init__(__nombre, __edad)

    def hacer_sonido(self):
        print('ssssss')

motty = Gato('Motty', '3')
pluto = Perro('Pluto', '5')
mrSnake = Serpiente('Mr. Snake', '2')

motty.hacer_sonido()
pluto.hacer_sonido()
mrSnake.hacer_sonido()