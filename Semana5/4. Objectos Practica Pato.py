'''
Vamos a crear un pato
'''

class duck:
    def __init__(self,nombre):
        self.duck_nombre = nombre
    def quack(self):
        print('Quaaaack!')

    def walk(self):
        print('walks like a duck.')


#Nace un pato llamado donald
donald = duck('donald')
daisy = duck('daisy')
#donald dice quack y camina
donald.quack()
donald.walk()


print('Cual es tu nombre?', donald.duck_nombre)
print('Cual es tu nombre?', daisy.duck_nombre)

