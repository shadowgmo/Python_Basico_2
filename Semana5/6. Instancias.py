'''
https://github.com/PythonClassRoom/PythonClassBook/wiki/Creaci%C3%B3n-de-una-instancia

'''

class Animal:
    def __init__(self, e, a):
        self.especie = e
        self.edad = a

    def correr(self):
        print('Soy un {}. '
              'Estoy corriendo'.format(self.especie))

    def crecer(self, edad=0):
        if (self.edad + edad) > 14:
            self.vivo = False

        else:
            self.edad += edad
            self.vivo = True

perro = Animal('perro', 3)
perro.crecer(10)
perro.crecer(2)

if perro.vivo:
    print("hola soy un {} "
          "tengo {} años".format(perro.especie,
                            perro.edad))
else:
    print('...Me morí... RIP')

