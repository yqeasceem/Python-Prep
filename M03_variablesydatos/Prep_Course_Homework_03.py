#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:
tasaInteres = 7
print(tasaInteres)

# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:

print(type(8.5))

# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:

print(type(tasaInteres))

# 4) Crear una variable que contenga tu nombre

# In[2]:
nombreEstudiante = 'Martín'

# 5) Crear una variable que contenga un número complejo

# In[3]:
numeroComplejo = 5 + 6j

# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:
print(numeroComplejo)

# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:
pi = 3.1416

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:

noEsBoolean = 'True'
siEsBoolean = True

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:

print(type(noEsBoolean))
print(type(siEsBoolean))

# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:
suma = 25 + 25.9

# 11) Realizar una operación de suma de números complejos

# In[2]:
sumaComplejos = 123j + 132j

# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:
sumaRealYComplejo = 125.896 + 753j
print(sumaRealYComplejo)

# 13) Realizar una operación de multiplicación

# In[5]:
5 * 8

# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:
print(2 ** 8)

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:
cociente = 27 / 4
print(cociente)

# 16) De la división anterior solamente mostrar la parte entera

# In[9]:
parteEntera = 27 // 4
print(parteEntera)
# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
restoDivision = 27 % 4
print(restoDivision)
# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:
recomponerDivision = (4 * parteEntera) + restoDivision
print(recomponerDivision)

# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:
str1 = 'alfa'
str2 = 'numéricas'
str3 = ' 123'
print(str1 + str2 + str3)

# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:
seraCierto = "2" == 2
print(seraCierto)

# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:
seraCierto = int("2") == 2
print(seraCierto)
# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:
# Porque 3,8 no es un numero valido en Python, 3.8 si lo es.
a = float('3.8')
print(a)

# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:
valor = 3
valor -= 1
print(valor)

# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:

# Número 1 en binario
# 00000001
# Desplazamiento de 2 posiciones a la izquierda
# 00000100
# Este número binario: 00000100 en decimal es igual al número 4

print(1 << 2)

# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:
# print(2 + '2') No se puede realizar la suma de un entero y un string
print(2 + int('2'))

# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:
print('2'+ str(2))