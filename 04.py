class Forma:
    def dibujar(self):
        print('Dibujando Forma')
        
class Color():
    def __init__(self, _color) -> None:
      self.color = _color
    def pintar(self):
        print(f'Pintando con {self.color}')


class CuadradoColorido(Forma, Color):
    def __init__(self, color) -> None:
        Forma.__init__(self)  # Llamada explícita al constructor de Forma
        Color.__init__(self, color)  # Llamada explícita al constructor de Color


cuadradoRojo = CuadradoColorido('Rojo')

cuadradoRojo.dibujar()
cuadradoRojo.pintar()