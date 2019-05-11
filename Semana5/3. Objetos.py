'''
La clase mas sencilla que se puede crear en Python es la siguiente:

class first:
    pass


https://github.com/PythonClassRoom/PythonClassBook/wiki/Programaci%C3%B3n-orientada-a-objectos

'''


class first:
    pass

a = first()

print (type(a))


####################################################################################################

class first:
    def __init__(self): #init, nos permite inicializar o controlar la inicializacion de los objetos, doble subraya
        print('Constructor ejecutado')

f=first()