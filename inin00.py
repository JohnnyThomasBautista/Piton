# Comentario de una sola línea

'''
Comentarios de varias líneas
'''

"""
También se puede hacer esto 
Para comentar varias lineas
"""

# Tipos de variables
# No es necesario colocar que tipo de variable
enteros = 5
flotante = 3.1415926539
cadena = "Este es el Python"
booleana = True
complejo = 3 + 4j

# Asignación múltiple de variables
x, y, z = 1, 2, 3
# Asignación de variables iguales
x = y = z = "Naranja"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Entrada de datos
# se utiliza la función input()
variable = input("Aquí va un bonito mensaje: ")
# y el dato se guarda como un string

# para poder "forzar" a la variable a tomar algún datos
# entonces se usa un especie de "cast"
variableEntera = int(input("Ingresa un valor entero: "))
variableFlotante = int(input("Ingresa un valor flotante: "))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Salida de Datos
# Utilizar la función print()
print("Esta es una salida de datos")

# Para mostrar variables
print(entero)

# Sin embargo si se desea mostrar variables junto con cadenas de texto
# existen varias formas:

# 1.-Concatenar cadenas de texto
# Utilizar el "cast" str() para convertir el valor a texto
print("Valor entero: " + str(entero))

# 2.-Usar identificadores como en C
print("Un valor flotante %.3f" %flotante)

# 3.-Utilizar el método format() para cadenas
# Los números seguidos de :, indican el número de casillas
# que serán asignadas para cada número (esto es muy útil para tablas)
print("Un valor entero {:4}, un valor flotante {:4.3}".format(enteros, flotante))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Operaciones
'''
 +		suma
 -		resta
 *		multiplicación
 /		división
 %		módulo
 **		exponente
 //		división floor
 
 &		AND
 |		OR
 ~		NOT
 ^		XOR
 >>		Desplazamiento bits a la derecha
 <<		Desplazamiento bits a la izquierda
 
 and	y
 or		o
 not	no 
 
'''