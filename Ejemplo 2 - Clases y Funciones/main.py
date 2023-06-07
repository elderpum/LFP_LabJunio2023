# EJEMPLO PRÁCTICO DE CLASES Y FUNCIONES

class funcionAritmetica:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Función encargada de sumar
    def suma(self):
        return self.a + self.b # -> 2 + 2 = 4
    
    # Función encargada de restar
    def resta(self):
        return self.a - self.b # -> 6 - 2 = 4
    
    # Función encargada de multiplicar
    def multiplicacion(self):
        return self.a * self.b # -> 4 * 2 = 8
    
    # Función encargada de dividir || a/b = resultado y b no tiene que ser 0
    def division(self):
        if self.b == 0:
            return 'Divisiones entre 0 no son posibles.'
        else:
            return self.a / self.b
        
    # Función encargada de trabajar potencias
    def potencia(self):
        return self.a**self.b # -> a^b
    
    def multiparametros(self, *args):
        # Devolución de la suma de todos los diferentes argumentos
        suma = 0
        # 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
        for i in args:
            suma += i # -> 45
        return suma
    
prueba = funcionAritmetica(5, 3)

# Probando las funciones
print('La suma entre los dos valores es de: '+ str(prueba.suma()))
print('La resta entre los dos valores es de: ' + str(prueba.resta()))
print('La multiplicación entre los dos valores es de: '
      + str(prueba.multiplicacion()))
print('La división entre los dos valores es de: ' + str(prueba.division()))
print('El resultado de la potencia es de: ' + str(prueba.potencia()))
print('La suma de los diferentes parámetros es de: ' + str(prueba.multiparametros(5,15,23,78,54,65468,1521,8568,4897,989)))