'''
1. Crear una clase 'bebe'
2. Declarsr 4 acciones
        Respirar, comer, llorar, dormir
3. Simular un dia normal de un bebe
4. Ponerle nombre al bebe y preguntarle
'''


class bebe:
    def __init__(self,nombre):
        self.bebe_nombre = nombre
    def llora(self):
        print('buaaaaaaaa!')

    def respira(self):
        print('*heavy breathing meme*')

    def comer(self):
        print('nom nom nom nom nom')

    def dormir(self):
        print('*ronquidos*')


mini_dude = bebe('Luis')

print ('El bebe llora porque tiene hambre')
mini_dude.llora()
mini_dude.respira()
mini_dude.comer()

print ('El bebe llora porque tiene sueño')
mini_dude.llora()
mini_dude.respira()
mini_dude.dormir()

print('Cual es el nombre del bebe?', mini_dude.bebe_nombre)