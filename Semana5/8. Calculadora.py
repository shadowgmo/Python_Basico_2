'''
https://github.com/PythonClassRoom/PythonClassBook/wiki/Tarea-3-Calculadora
https://github.com/pythonclassroom/pythonclassbook/blob/master/tarea%203/CalculadoraBasica.py
Crear una calculadora
'''
class CalculadoraBasica:

    #creando metoo para asignar valores
    def capturar_valores(self, a, b):
        self.a = a
        self.b = b

    #metodo de suma
    def sumar(self):
        return self.a + self.b

    #metodo de resta
    def restar(self):
        return self.a - self.b

    #metodo de multiplicar
    def multiplicar(self):
        return self.a * self.b

    #metodo de dividir
    def dividir(self):
        return self.a / self.b

if __name__ == "__main__": #usa solo cuando se llame directamente este script
    miCalculadora =CalculadoraBasica()

    #quizas ocupamos un valor inicial en cero
    resultado = 0

    print('--Bienvevido a la calculadora básica--')
    operacion = input('Ingresa la función realizar \n '  \
                      '+  - * /')
    valor1= input('Ingresa el primer valor')
    valor1 = int(valor1)
    valor2 = input('Ingresa el segundo valor')
    valor2 = int(valor2)

    # Actuliza los valores en la instancia
    # miCalculadora
    miCalculadora.capturar_valores(valor1, valor2)

    if operacion == '+':
        resultado = miCalculadora.sumar()
    elif operacion == '-':
        resultado = miCalculadora.restar()
    elif operacion == '*':
        resultado = miCalculadora.multiplicar()
    elif operacion == '/':
        resultado = miCalculadora.dividir()
    else:
        pass
    print(f'El resultado de {operacion}',
          f' el número {valor1}',
          f' y el número {valor2}',
          f'es de {resultado}')