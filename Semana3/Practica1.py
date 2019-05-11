'''
Listas de compras
Verduras    ->     Papas, Cebolla, Ajo, Tomate
Frutas      ->     Piña, Naranja, Sandia
Carnes      ->     Mortadela, Pollo, Costilla de cerdo
Limpieza    ->     Jabon, Cloro, Shampoo

1. Crear listas de las categorias
2. Crear lista de compras
3. Cuantos articulos voy a comprar?
4. Agregar a la lista de verduras: chile, y a la lista de frutas: mango. Verificar efecto en la lista general
5. Utilizando pasos 1, 2, 4.
'''

#Respuesta 1
Verduras = ['papas', 'cebolla', 'ajo', 'tomate']
Frutas = ['piña', 'naranja', 'sandia']
Carnes = ['mortadela', 'pollo', 'costilla de cerdo']
Limpieza = ['jabon', 'cloro', 'shampoo']

#Respuesta 2
Lista_de_compras = [Verduras, Frutas, Carnes, Limpieza]

'''
#Respuesta 3
#Evaluate Expression ->
#   for categoria in Lista_de_compras
#   print (categoria)

#   for categoria in Lista_de_compras
#   print (categoria, type(categoria))

#   for categoria in Lista_de_compras
#   print (categoria, len(categoria))

#   cantidad = 0
#   for categoria in Lista_de_compras
#   len(categoria)

#   cantidad = 0
#   for categoria in Lista_de_compras:
#   cantidad += len(categoria)


#Aplanar las listas, mismo nivel
mi_lista = []
for categoria in Lista_de_compras:
    mi_lista.extend(categoria)
print (len(mi_lista))


mi_lista = []
for categoria in Lista_de_compras:
    mi_lista.extend(categoria)
    print(mi_lista)
print (len(mi_lista))
'''

#Respuesta 4
#uso de append

'''
#Respuesta 5

Verduras.clear()

mi_lista = []
for categoria in Lista_de_compras:
    mi_lista.extend(categoria)
    print(mi_lista)
print (len(mi_lista))

'''

pass


