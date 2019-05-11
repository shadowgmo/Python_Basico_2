'''
Suponga que un hospital abre la atención de pacientes muy temprano. Uno a uno personas van llegando al hospital.

Llega la primer persona y la secretaria apunta sus datos personas y la razón de la consulta.
'''

# Para definir la agenda del hospital
agenda_hospital = []

persona = ('Juan', 'Mora', '100103111,65', '81118811', 'dolor')

# agregamos una persona
agenda_hospital.append(persona)

# podemos revisar cual es el estatus de la agenda
#print(agenda_hospital)

# viene otra persona
persona = ('Ana', 'Jimenez', 32415116,50 , 46261266, 'consulta')
# agregamos otra persona
agenda_hospital.append(persona)

# podemos revisar cual es el estatus de la agenda
#print(agenda_hospital)

# suponga que vienen 5 personas mas
persona =[('Sofia',   'Alfaro',   32415116,   36 , 51161161, 'consulta'),
          ('Carlos',  'Sanchez',  33411151,   15 , 41655161, 'dolor'),
          ('Felipe',  'Perez',    12243151,   42 , 65151111, 'documento'),
          ('Melissa', 'Alvarado', 734114144,  10 , 87421312, 'dolor'),
          ('Pedro',   'Castro',   4372124141, 2 ,  99313131, 'dolor'),]

agenda_hospital.extend(persona)

# podemos revisar cual es el estatus de la agent
#print(agenda_hospital)

# notemos que la impresión en pantalla está un poco sucia... lo arreglamos
for paciente in agenda_hospital:
    print(paciente)


#1. Cuantos pacientes llegaron en total?
len(paciente)

#2. Cuantas personas llegaron por dolor?


#3. Suponga que se atienden con orden de prioridad por edad, empezando por el adulto mayor. Ordene la lista desde el más adulto al más joven


#4. Cuantos pacientes son mayores de edad? cuantos menores?


#5. Suponga que se atienden con orden de prioridad por gravedad de consulta, empezando por los que tienen dolor y luego por edad (mas viejo al joven), empezando por el adulto mayor. Ordene la lista empenzando por los que tienen mayor prioridad.


#6. Suponga que los que tienen dolor mueren :( Como queda la lista de pacientes vivos por atender ordenados por orden de edad desde el joven al viejo.





pass