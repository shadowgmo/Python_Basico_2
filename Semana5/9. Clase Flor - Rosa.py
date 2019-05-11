'''
https://github.com/PythonClassRoom/PythonClassBook/wiki/Python-Class:-use-case.-Flowers-and-roses.

Crear clase flor y clase rosa.
'''

# Define simple flower class
class flower(misc):
    def __init__(self, n_lemma=1, n_stigmas=1, n_filaments=1):
        self.n_lemma = n_lemma
        self.lemmas = [lemma() for i in range(self.n_lemma)]
        self.pedicel = pedicel()
        self.n_stigmas = n_stigmas
        self.stigmas = [stigma() for i in range(self.n_stigmas)]
        self.n_filaments = n_filaments
        self.filaments = [filament() for i in range(self.n_filaments)]

    def grow(self):
        print(f'The {self.__str__()} is growning')

    def dead(self):
        print(f'The {self.__str__()} was gone')

    def __add__(self, other):
        # In case of addition, create a self's like class instance
        a_flower = self.__class__()
        # Compose list of lemmas based on their sources, self and other objects
        a_flower.lemmas = self.lemmas[::2] + other.lemmas[1::2]
        a_flower.n_lemma = len(a_flower.lemmas)
        # filaments and stigmas as self has.
        a_flower.filaments = self.filaments
        a_flower.stigmas = self.stigmas
        return a_flower