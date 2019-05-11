'''
...continua del Refactor 5.

5. Crecer el bebe en uno

'''

class bebe:
    def __init__(self,nombre,edad):
        self.bebe_nombre = nombre
        self.bebe_edad = edad

    def llora(self):
        print('buaaaaaaaa!')

    def respira(self):
        print('*heavy breathing meme*')

    def comer(self):
        print('nom nom nom nom nom')

    def dormir(self):
        print('*ronquidos*')

    def crecer(self, edad=1):
        if (self.bebe_edad + edad) > 14:
            self.vivo = False

        else:
            self.bebe_edad += edad
            self.vivo = True


mini_dude = bebe('Luis', 1)

print ('El bebe llora porque tiene hambre')
mini_dude.llora()
mini_dude.respira()
mini_dude.comer()

print ('El bebe llora porque tiene sueño')
mini_dude.llora()
mini_dude.respira()
mini_dude.dormir()

mini_dude.crecer(14)

print('Cual es el nombre del bebe?', mini_dude.bebe_nombre)

if mini_dude.vivo:
    print("tengo {} años".format(mini_dude.bebe_edad))
else:
    print('...Se murio... RIP')