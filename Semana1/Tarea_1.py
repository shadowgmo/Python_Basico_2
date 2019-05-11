print ('test')

import math
pi = math.pi

my_variable = "*"


stringvalue = pi
[
print ('* %.9s' % (stringvalue),
       '** %.8s ' % (stringvalue),
       '*** %.7s ' % (stringvalue),
       '**** %.6s ' % (stringvalue),
       '***** %.5s' % (stringvalue),
       '****** %.4s' % (stringvalue))
]

[
print (my_variable*1,'%.9s' % (stringvalue),
       my_variable*2,'%.8s ' % (stringvalue),
       my_variable*3,'%.7s ' % (stringvalue),
       my_variable*4,'%.6s ' % (stringvalue),
       my_variable*5,'%.5s' % (stringvalue),
       my_variable*6,'%.4s' % (stringvalue))
]



print('\n \n')
#Necesito definir '*' como caracter y no como formula matematica

#Test1:
#Para intentar sumar un asterisco en cada linea.
print("Test1")

def doubleChar(str):
    result = ''
    for char in str:
        result += "*" * 5
        return result

print(doubleChar("asterisco"))

print('\n')
#Test2:
#Para intentar sumar un asterisco en cada linea.
print("Test2")

value="abc"
finalMessage=""
for x in range(0,len(value)):
    if ord(value[x]) in range(97,123):
        finalMessage+=(chr(((ord(value[x])-96)%26)+97))
    elif ord(value[x]) in range(65,91):
        finalMessage+=(chr(((ord(value[x])-64)%26)+65))
    else:
        finalMessage+=value[x]
print(finalMessage)
print

print('\n')
#Test3:
#Para intentar sumar un asterisco en cada linea.
print ("Test3")

m = 1
m = m + 3
print(m)

print('\n')
#Test4:
#Para intentar sumar un asterisco en cada linea.
print ("Test4")

"1".replace('1','*')
u = (1*1)+1
print(u)


print('\n')

