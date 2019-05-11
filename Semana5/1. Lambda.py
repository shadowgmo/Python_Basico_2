a = [1,3,5,8,7,9,2]

f = lambda x : x*10

[f(i) for i in a] #usa el lambda en cada elemento de la lista

[(lambda x : x*10)(i) for i in a if i > 5]

########################################################################################

a = [1,3,5,8,7,9,2]
[i for i in a] #daria el mismo contenido, se aplica lo que se ocupa vs la primera "i"

f = lambda x : x*10

[f(i) for i in a] #usa el lambda en cada elemento de la lista

[(lambda x : x*10) (i) for i in a if i > 5]

#######################################################################################

a = [1,3,5,8,7,9,2]
[i for i in a] #daria el mismo contenido, se aplica lo que se ocupa vs la primera "i"

f = lambda x : x*10

[i*10 for i in a] #si es multiplicar por diez, esto seria lo mas sencillo para hacer

[(lambda x : x*10) (i) for i in a if i > 5]