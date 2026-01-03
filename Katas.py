from functools import reduce
import math

"""
1
Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. 
Los espacios no deben ser considerados.
"""
def contar_frecuencias(cadena):

    diccionario_frecuencias = {}

    for letra in cadena:
        if letra != " ":
            # Comprobamos si la letra ya es una clave en el diccionario
            if letra in diccionario_frecuencias:
                # Si existe, actualizamos su valor sumando 1
                diccionario_frecuencias[letra] += 1
            else:
                # Si no existe, la creamos con valor 1
                diccionario_frecuencias[letra] = 1
                
    return diccionario_frecuencias

# Prueba
texto_prueba = "hola mundo"
resultado = contar_frecuencias(texto_prueba)
print(f'== Kata 1: {resultado}')

"""
2
Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().
"""

lista = [1,3,5,7,9]

# Convertimos el resultado a list() porque map devuelve un objeto iterador
lista_doble = list(map(lambda x: x * 2, lista))

print(f'== Kata 2: {lista_doble}')

"""
3
Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. 
La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
"""

def filtrar_palabras(lista_palabras, objetivo):

    # Creamos una lista vacía para guardar las coincidencias
    coincidencias = []
    
    for palabra in lista_palabras:
        # El método .find() devuelve el índice donde empieza la subcadena.
        # Si devuelve -1, significa que NO encontró la palabra objetivo.
        if palabra.find(objetivo) != -1:
            coincidencias.append(palabra)
            
    return coincidencias

# Prueba de la función
lista_prueba = ["html", "css", "javascript", "python", "java"]
palabra_buscar = "java"

resultado = filtrar_palabras(lista_prueba, palabra_buscar)
print(f"== Kata 3: Palabras que contienen '{palabra_buscar}': {resultado}")


"""
4
Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().
"""

def calcular_diferencia(lista_a, lista_b):
    # La función map puede recibir múltiples iterables.
    # La lambda recibe dos argumentos (x, y) correspondientes a cada lista y devuelve la resta.
    resultado = list(map(lambda x, y: x - y, lista_a, lista_b))
    
    return resultado

# Prueba de la función
lista_1 = [10, 20, 30, 40]
lista_2 = [1, 2, 3, 4]

diferencia = calcular_diferencia(lista_1, lista_2)
print(f"== Kata 4: La diferencia entre las listas es: {diferencia}")

"""
5
Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5). 
La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. 
Si es así, el estado será "aprobado"; de lo contrario, "suspenso". La función debe devolver una tupla que contenga la media y el estado.
"""

def promedio_notas(lista_numeros, nota_aprobado=5):
    # Calculamos la suma de los números mediante un bucle for
    suma_total = 0
    for numero in lista_numeros:
        suma_total += numero
    
    # Calculamos la media (evitando dividir por cero si la lista está vacía)
    # Usamos len() para saber cuántos elementos hay.
    if len(lista_numeros) > 0:
        media = suma_total / len(lista_numeros)
    else:
        media = 0
        
    # Determinamos el estado usando un if
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
        
    # Devolvemos una tupla con la media y el estado
    return (media, estado)

# Prueba de la función

notas_alumno = [4, 6, 5, 7, 4]
resultado = promedio_notas(notas_alumno)
print(f"== Kata 5: Alumno: Media {resultado[0]} - Estado: {resultado[1]}")

"""
6
Escribe una función que calcule el factorial de un número de manera recursiva.
"""

def calcular_factorial(numero):

    # Si el número es 1 (o 0), el factorial es 1.
    if numero == 1 or numero == 0:
        return 1
    
    # Recursivo: Se llama a la función a sí misma con (numero - 1).
    # Multiplicamos el número actual por el resultado de la llamada recursiva.
    else:
        return numero * calcular_factorial(numero - 1)

# Prueba de la función con el número 5
# Cálculo esperado: 5 * 4 * 3 * 2 * 1 = 120
resultado = calcular_factorial(5)
print(f"== Kata 6: El factorial de 5 es: {resultado}")


"""
7
Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().
"""

def convertir_tuplas_a_strings(lista_tuplas):
    # Usamos map() para aplicar una función a cada tupla de la lista.
    # Usamos una lambda que recibe la tupla 'tupla1' y usa " ".join(tupla1) para unir sus elementos.
    # Finalmente, convertimos el objeto map resultante a una lista con list().
    lista_resultante = list(map(lambda tupla1: " ".join(tupla1), lista_tuplas))
    
    return lista_resultante

# Prueba de la función
datos = [("Hola", "mundo"), ("Python", "me", "encanta"), ("Antonio", "mola")]

resultado = convertir_tuplas_a_strings(datos)
print(f"== Kata 7: Lista de strings: {resultado}")

"""
8
Escribe un programa que pida al usuario dos números e intente dividirlos. 
Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada y muestra un mensaje indicando si la división fue exitosa o no.
"""

def dividir_numeros():
    print("== Kata 8: ")
    
    # Iniciamos el bloque try para el código susceptible a errores
    try:
        # Pedimos los datos y los convertimos a número
        numero_1 = int(input("Introduce el primer número: "))
        numero_2 = int(input("Introduce el segundo número: "))
        
        # Intentamos realizar la división
        resultado = numero_1 / numero_2

    # Capturamos el error si el usuario introduce texto en lugar de números
    except ValueError:
        print("Error: Debes introducir números válidos.")

    # Capturamos el error si el usuario intenta dividir por 0
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")

    # El bloque else se ejecuta si NO hubo ningún error
    else:
        print(f"¡División correcta! El resultado es: {resultado}")

# Ejecutamos la función
dividir_numeros()


"""
9
Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España.
La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().
"""

def filtrar_mascotas_permitidas(lista_mascotas):
    # Definimos la lista de mascotas prohibidas
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

    # Definimos la función auxiliar que usará el filter.
    # Esta función debe devolver True si queremos quedarnos con la mascota y False si queremos eliminarla.
    def es_permitida(mascota):
        if mascota in prohibidas:
            return False 
        else:
            return True  

    # Aplicamos filter(función, iterable).
    # Pasamos nuestra función 'es_permitida' y la lista original.
    resultado_filtro = filter(es_permitida, lista_mascotas)

    # Convertimos el iterador resultante en una lista.
    lista_final = list(resultado_filtro)
    
    return lista_final

# Pruebas de la función
mis_mascotas = ["Perro", "Mapache", "Gato", "Tigre", "Hamster"]

resultado = filtrar_mascotas_permitidas(mis_mascotas)
print(f"== Kata 9: Mascotas permitidas: {resultado}")


"""
10
Escribe una función que reciba una lista de números y calcule su promedio. 
Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
"""

def promedio(lista):

    sumatorio = 0
    
    for num in lista:
        sumatorio += num
    
    # Intentamos realizar la división 
    try:
        # Si la lista está vacía se produce un error
        resultado = sumatorio / len(lista)
        return resultado

    # Capturamos el error específico de división por cero 
    except ZeroDivisionError:
        print("No se puede calcular el promedio de una lista vacía.")
        return 0


print("== Kata 10:")

# Caso 1: Lista con números
listanum = [1, 2, 3]
resultado = promedio(listanum)
print(f"Caso1 - Lista llena: {resultado}")

# Caso 2: Lista vacía (Para probar la excepción)
lista_vacia = []
resultado_error = promedio(lista_vacia)
print(f"Caso2 - Lista vacía: {resultado_error}")

"""
11
Escribe un programa que pida al usuario que introduzca su edad.
Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
"""

def verificar_edad():
    
    # Iniciamos try para capturar posibles errores de conversión
    try:
        edad = int(input("== Kata 11: Por favor, introduce tu edad: "))
        # Usamos 'or' dentro del if para detectar si la edad es menor que 0 o mayor que 120 
        if edad < 0 or edad > 120:
            print("Error: La edad introducida debe estar entre 0 y 120.")
        else:
            print(f"Tu edad es {edad} años.")

    # Capturamos el error específico cuando no se introduce un número
    except ValueError:
        print("Error: El valor introducido no es numérico.")

# Ejecutamos la función
verificar_edad()


"""
12
Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().
"""

def longitudes_palabras(frase):
    # Usamos .split() para obtener las palabras de la frase separadas por espacios.
    lista_palabras = frase.split()

    # Usamos map(funcion, lista)
    objeto_map = map(len, lista_palabras)
    
    # Convertimos a lista
    resultado = list(objeto_map)
    
    return resultado

texto = "Frase de prueba para Kata 12"

resultado_final = longitudes_palabras(texto)

print("== Kata 12: ")
print(f"Frase original: '{texto}'")
print(f"Longitudes: {resultado_final}")

"""
13
Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().
"""

def procesar_caracteres(caracteres):
    
    # Funcion auxiliar
    def crear_pareja(letra):
        return (letra.upper(), letra.lower())
    
    # Eliminar duplicados
    conjunto_letras = set(caracteres)

    resultado_map = map(crear_pareja, conjunto_letras)

    return list(resultado_map)

print(f'== Kata 13: {procesar_caracteres("AnTOniO")}')


"""
14
Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().
"""

def filtrar_letra(lista, letra):

    # Funcion auxiliar
    def empieza(palabra):

        if palabra[0] == letra:
            return True
        return False
    
    # Aplicamos filter usando esa función interna    
    resultado = filter(empieza,lista)
    return list(resultado)

lista = ["camion", "perro", "limon", "calamar"]


print(f'== Kata 14: : {filtrar_letra(lista,"c")}')

"""
15
Crea una función lambda que sume 3 a cada número de una lista dada.
"""

numeros = [1,2,3]

# Aplicamos la función a cada número de la lista
resultado = list(map(lambda x: x + 3, numeros))

print(f'== Kata 15: {resultado}')

"""
16
Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().
"""

def funcion(cadena,n):
    lista_palabras = cadena.split()
    resultado = list(filter(lambda x: len(x) > n, lista_palabras))
    return resultado

print(f'== Kata 16: {funcion("Como disfruto con Python", 4)}')


"""
17
Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().
"""

# Necesario importar funcion reduce()

def pegar(a, b):
    return a + b

lista = [5, 7, 2]

# Convertimos los números a texto
lista_a_texto = list(map(str, lista))

# Usamos reduce para unir
resultado_texto = reduce(pegar, lista_a_texto)

# Lo convertimos a número
resultado = int(resultado_texto)

print(f'== Kata 17: {resultado}')

"""
Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación) y
use filter para extraer a los estudiantes con una calificación mayor o igual a 90.
"""

# Lista de diccionarios
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 85},
    {"nombre": "Luis", "edad": 22, "calificacion": 95}, 
    {"nombre": "Marta", "edad": 21, "calificacion": 90}, 
    {"nombre": "Pedro", "edad": 19, "calificacion": 88}
]

def estudiante_90(estudiante):
    # Accedemos a la clave 'calificacion'
    if estudiante["calificacion"] >= 90:
        return True
    return False

# Aplicamos el filter
resultado = list(filter(estudiante_90,estudiantes))

print(f'== Kata 18: {resultado}')    


"""
19
Crea una función lambda que filtre los números impares de una lista dada.
"""

lista =  [1,2,3,4,5,6]

# Devolverá True si es impar
resultado = list(filter(lambda x: x % 2 != 0, lista))

print(f'== Kata 19: {resultado}')

"""
20
Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().
"""

lista = [1, 2, "a", "b"]

resultado = list(filter(lambda x: type(x) == int, lista))

print(f'== Kata 20: {resultado}')

"""
21
Crea una función que calcule el cubo de un número dado mediante una función lambda.
"""
# Recibiremos un dato(x) para elevarlo al cubo
resultado = lambda x: x ** 3

print(f'== Kata 21: {resultado(5)}')

"""
22
Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().
"""
# reduce() ya importada 

numeros = [1,2,3,4,5,6]

# Pasamos acumulador y numero a multiplicar
resultado = reduce(lambda acc, num: acc*num, numeros)

print(f'== Kata 22: {resultado}')

"""
23
Concatena una lista de palabras. Usa la función reduce().
"""
# reduce() ya importada 

lista_palabras = ["lista", "de", "palabras"]

# Pasamos acumulador y palabras a concatenar (añadimos espacio entre palabras)
resultado = reduce(lambda acc, palabra: acc + " " + palabra,lista_palabras )

print(f'== Kata 23: {resultado}')


"""
24
Calcula la diferencia total en los valores de una lista. Usa la función reduce().
"""
# reduce() ya importada 

lista_numeros = [20, 8, 3 ]

# Pasamos acumulador y números a restar
resultado = reduce(lambda acc, num: acc - num, lista_numeros)

print(f'== Kata 24: {resultado}')


"""
25
Crea una función que cuente el número de caracteres en una cadena de texto dada.
"""

def contar_caracteres(cadena):
    return len(cadena)

# Cuenta caracteres incluyendo espacios
cadena = "Lista de caracteres a contar"

print(f'== Kata 25: {contar_caracteres(cadena)}')


"""
26
Crea una función lambda que calcule el resto de la división entre dos números dados.
"""
# Calculamos el resto con %
resultado = lambda x,y: x%y

print(f'== Kata 26: {resultado(100,8)}')


"""
27
Crea una función que calcule el promedio de una lista de números.
"""

def promedio(lista):

    # Inicializamos la variable suma_numeros para sumar los numeros
    suma_numeros = 0

    # Añadimos los numeros de la lista_num a suma_numeros
    for num in lista:
        suma_numeros += num
    return suma_numeros/len(lista) # Devuelve la suma de los números entre el total de números

lista_num = [1,2,3,4,5,6]

print(f'== Kata 27: {promedio(lista_num)}')


"""
28
Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
"""

def duplicado(lista):
    # Creamos una lista vacía para almacenar los elementos ya iterados 
    vistos = [] 

    # Iteramos por cada elemento del iterable 
    for num in lista:
        
        # Usamos count() para verificar si el elemento ya existe en la lista "vistos
        if vistos.count(num) > 0:
            return num # Devolvemos el valor duplicado 
        else:
            # Si no está duplicado, lo agregamos al final de la lista 
            vistos.append(num)


lista_ejemplo = [1, 2, 3, 4, 4, 5, 6]
print(f'== Kata 28: {duplicado(lista_ejemplo)}')


"""
29
Crea una función que convierta una variable en una cadena de texto y 
enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.
"""

def enmascarar_variable(variable):
    # Convertimos la cadena a texto 
    cadena = str(variable)
    resultado = ""
    
    # Usamos enumerate para obtener el índice (i) y el carácter 
    for i, caracter in enumerate(cadena):
        # Si la posición está antes de los últimos 4 caracteres 
        if i < len(cadena) - 4:
            resultado += "#" # Añadimos el símbolo de máscara 
        else:
            resultado += caracter # Si es de los últimos 4, añadimos el original
            
    return resultado 

# Ejemplo de uso:
print(f'== Kata 29: {enmascarar_variable("123456789")}')

"""
30
Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
"""

def es_anagrama(palabra1, palabra2):
    # Convertimos ambas palabras a minúsculas
    p1 = palabra1.lower()
    p2 = palabra2.lower()
    
    # Si son exactamente la misma palabra, no cumplen la condición de "diferente orden"
    if p1 == p2:
        return False
    
    # Convertimos las palabras en listas de caracteres 
    lista1 = list(p1)
    lista2 = list(p2)
    
    # Ordenamos las listas y comparamos si son iguales
    return sorted(lista1) == sorted(lista2)

print("== Kata 30:")
print(f"¿Es anagrama Roma-Amor? {es_anagrama('Roma', 'Amor')}") 
print(f"¿Es anagrama Hola-Hola? {es_anagrama('Hola', 'Hola')}") 


"""
31
Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista.
Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.
"""

print("== Kata 31:")

def buscar_nombre(lista_nombres, nombre_a_buscar):
    if nombre_a_buscar in lista_nombres:
        # Imprimimos el siguiente mensaje si se encuentra el nombre
        print(f"{nombre_a_buscar} fue encontrado en la lista.")
    else:    
        # Lanzamos una excepción si no se encuentra el nombre
        raise ValueError(f"Error: El nombre '{nombre_a_buscar}' no existe en esta lista.")

# --- PRUEBA DEL CÓDIGO ---
try:
    nombres_input = input("Nombres separados por coma (sin espacios): ").split(",")
    buscar = input("Nombre a buscar: ")
    
    buscar_nombre(nombres_input, buscar)

except ValueError as e:
    print(e)


"""
32
Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista y devuelva el 
puesto del empleado si se encuentra; de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
"""


def buscar_empleado(diccionario_nombres,nombre_a_buscar):

    # Estructura condicional 'if' para verificar si el nombre existe en el diccionario
    if nombre_a_buscar in diccionario_nombres:
        return f'{nombre_a_buscar} trabaja como: {diccionario_nombres[nombre_a_buscar]}'
    else:    
        return f'{nombre_a_buscar} NO trabaja aquí'
    
# Creamos 'diccionario_nombres' con pares clave-valor
diccionario_nombres = {
    "Marta": "Administradora de Sistemas",
    "Juan": "Técnico de Redes",
    "Manuel": "Especialista en Seguridad",
    "Luisa": "Desarrolladora Python"
}

print("== Kata 32:")

# Con el input capturamos el nombre que el usuario escribe, usamos capitalize para evitar errores de escritura de usuario con mayúsuculas y minúsculas
nombre_a_buscar = input("Introduzca el nombre del empleado a buscar: ").capitalize()

# Mostramos por pantalla el resultado que devuelve el return
print(buscar_empleado(diccionario_nombres,nombre_a_buscar))


"""
33
Crea una función lambda que sume elementos correspondientes de dos listas dadas.
"""

lista1 = [1,2,3]
lista2 = [4,5,6]

# Usamos map() con una lambda que recibe dos parámetros (x, y)
# map aplica la lambda a cada par de elementos (1+4, 2+5, 3+6)
resultado = list(map(lambda x,y: x + y, lista1, lista2))

print(f'== Kata 33: {resultado}')

"""
34
Clase Arbol
"""

class Arbol:
    # 1a. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    # 1b. Implementar el método crecer_tronco para aumentar la longitud en una unidad
    def crecer_tronco(self):
        self.tronco += 1

    # 1c. Implementar el método nueva_rama para agregar una rama de longitud 1
    def nueva_rama(self):
        self.ramas.append(1)

    # 1d. Implementar el método crecer_ramas para aumentar en una unidad todas las ramas
    def crecer_ramas(self):
        # Recorremos la lista para actualizar cada valor individualmente
        for i in range(len(self.ramas)):
            self.ramas[i] += 1

    # 1e. Implementar el método quitar_rama para eliminar una rama en una posición específica
    def quitar_rama(self, posicion):
        # Usamos pop para eliminar por índice
        if posicion < len(self.ramas):
            self.ramas.pop(posicion)

    # 1f. Implementar el método info_arbol para devolver la información técnica
    def info_arbol(self):
        return (f"Longitud Tronco: {self.tronco}\n"
                f"Número de ramas: {len(self.ramas)}\n"
                f"Longitud de las ramas: {self.ramas}")

# --- CASOS DE USO ---

# a. Crear un árbol.
mi_arbol = Arbol()

# b. Hacer crecer el tronco una unidad.
mi_arbol.crecer_tronco()

# c. Añadir una nueva rama.
mi_arbol.nueva_rama()

# d. Hacer crecer todas las ramas una unidad.
mi_arbol.crecer_ramas()

# e. Añadir dos nuevas ramas.
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()

# f. Retirar la rama situada en la posición 2.
mi_arbol.quitar_rama(2)

# g. Obtener información sobre el árbol.
print("== Kata 34: ")

print(mi_arbol.info_arbol())

"""
35
Clase UsuarioBanco
"""
class UsuarioBanco:
    # 1a. Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
    def __init__(self, nombre, saldo, tiene_cuenta):
        self.nombre = nombre
        self.saldo = saldo
        self.tiene_cuenta = tiene_cuenta

    # 1b. Implementar retirar_dinero para sustraer saldo, lanzando error si no es posible
    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            # Lanzamos una excepción si el saldo es insuficiente
            raise ValueError(f"Error: {self.nombre} no tiene saldo suficiente.")
        self.saldo -= cantidad

    # 1c. Implementar transferir_dinero desde otro usuario, lanzando error en caso de fallo
    def transferir_dinero(self, cantidad, otro_usuario):
        # Primero verificamos si el usuario que envía tiene dinero
        if cantidad > otro_usuario.saldo:
            raise ValueError(f"¡Error!: {otro_usuario.nombre} no tiene suficiente dinero para transferir.")
        
        # Restamos al que envía y sumamos al que recibe (self)
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad
        print(f"Transferencia de {cantidad} de {otro_usuario.nombre} a {self.nombre} completada.")

    # 1d. Implementar agregar_dinero para aumentar el saldo del usuario
    def agregar_dinero(self, cantidad):
        self.saldo += cantidad


# --- CASOS DE USO ---

print("== Kata 35: ")

# a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# b. Agregar 20 unidades al saldo de Bob
bob.agregar_dinero(20)

# c. Transferir 80 unidades de Bob a Alicia
try:
    alicia.transferir_dinero(80, bob)
except ValueError as e:
    print(e)  # Error porque Bob solo tiene 70

# d. Retirar 50 unidades del saldo de Alicia
try:
    alicia.retirar_dinero(50)
    print(f"Saldo final de Alicia: {alicia.saldo}")
except ValueError as e:
    print(e)


"""
36
procesar_texto
"""

# 1a. Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.
def contar_palabras(texto):
    palabras = texto.split()
    frecuencias = {}
    for p in palabras:
        # Usamos get() para evitar errores si la palabra no existe aún
        frecuencias[p] = frecuencias.get(p, 0) + 1
    return frecuencias

# 1b. Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.
def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

# 1c. Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
def eliminar_palabra(texto, palabra):
    # Reemplazamos la palabra por texto vacío
    return texto.replace(palabra, "").replace("  ", " ").strip()

# 1d. Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.
def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    
    elif opcion == "reemplazar":
        # args[0] es la palabra original, args[1] es la nueva
        return reemplazar_palabras(texto, args[0], args[1])
    
    elif opcion == "eliminar":
        # args[0] es la palabra a eliminar
        return eliminar_palabra(texto, args[0])
    
    else:
        return "Opción no válida"

# --- CASO DE USO ---

print("== Kata 36: ")

texto_ejemplo = "python es genial y Antonio es un crack"

print("Texto ejemplo: 'python es genial y Antonio es un crack'")

# a. Verificar conteo
print("Conteo:", procesar_texto(texto_ejemplo, "contar"))

# b. Verificar reemplazo
print("Reemplazo:", procesar_texto(texto_ejemplo, "reemplazar", "genial", "increíble"))

# c. Verificar eliminación
print("Eliminación:", procesar_texto(texto_ejemplo, "eliminar", "es"))


"""
37
Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.
"""
print("== Kata 37: ")

try:
    # Pedimos la hora al usuario
    entrada = input("Introduzca la hora (formato HH:MM): ")

    # Dividimos y extraemos los datos de la hora y los minutos
    partes = entrada.split(":")
    
    # Validamos que el usuario haya puesto los dos puntos
    if len(partes) != 2:
        raise ValueError("Formato incorrecto. Debe usar ':' para separar hora y minutos.")

    # Convertimos a entero
    hora = int(partes[0])
    minutos = int(partes[1])

    # Validamos los rangos numéricos
    if not (0 <= hora <= 23):
        raise ValueError(f"La hora '{hora}' no es válida. Debe estar entre 0 y 23.")
    
    if not (0 <= minutos <= 59):
        raise ValueError(f"Los minutos '{minutos}' no son válidos. Deben estar entre 00 y 59.")

    # 4. Si todo es correcto, ejecutamos el if
    if 6 <= hora <= 11:
        print(f"A las {hora:02d}:{minutos:02d} es de día.")
    elif 12 <= hora <= 18:
        print(f"A las {hora:02d}:{minutos:02d} es de tarde.")
    elif (0 <= hora <= 5) or (19 <= hora <= 23):
        print(f"A las {hora:02d}:{minutos:02d} es de noche.")

except ValueError as e:
    # Capturamos cualquier error (letras, formato o rangos fuera de límite)
    print(f"ERROR: {e}")

except Exception as e:
    # Capturamos cualquier otro error inesperado
    print(f"Ha ocurrido un error inesperado: {e}")

    """
38
Calificacion alumno
"""
print("== Kata 38: ")

try:
    # Pedimos la calificación al usuario
    nota = int(input("Introduce la calificación numérica (0-100): "))

    # Validamos que la nota esté en el rango permitido
    if nota < 0 or nota > 100:
        print("Error: La calificación debe estar entre 0 y 100.")
    
    else:
        # Aplicamos el if
        if 0 <= nota <= 69:
            resultado = "insuficiente"
        elif 70 <= nota <= 79:
            resultado = "bien"
        elif 80 <= nota <= 89:
            resultado = "muy bien"
        else: # Equivale a 90 - 100
            resultado = "excelente"

        # Mostramos el resultado final
        print(f"Con una nota de {nota}, la calificación es: {resultado}")

except ValueError:
    # Captura errores si el usuario no introduce un número entero
    print("Error: Por favor, introduce un número entero válido.")

"""
39
Figura y datos
"""
print("== Kata 39: ")

def calcular_area(figura, datos):
    # Comprobamos si la figura es un rectángulo
    if figura == "rectangulo":
        # Desempaquetamos la tupla: el primer valor es ancho y el segundo es alto
        ancho, alto = datos
        return ancho * alto
        
    # Comprobamos si la figura es un círculo
    elif figura == "circulo":
        # Para el círculo, la tupla solo tiene un valor: el radio
        radio = datos[0]
        # Fórmula: PI * radio al cuadrado
        return math.pi * (radio ** 2)
        
    # Comprobamos si la figura es un triángulo
    elif figura == "triangulo":
        # Desempaquetamos la tupla en base y altura
        base, altura = datos
        # Fórmula: (base * altura) / 2
        return (base * altura) / 2
        
    # Si la figura no coincide con ninguna de las anteriores
    else:
        return "Figura no soportada"

# --- CASO DE USO ---

# Calculamos el área de un rectángulo de 10x5
print(f"Área del Rectángulo: {calcular_area('rectangulo', (10, 5))}")

# Calculamos el área de un círculo de radio 7 (mostramos solo 2 decimales)
print(f"Área del Círculo: {calcular_area('circulo', (7,)):.2f}")

# Calculamos el área de un triángulo de base 8 y altura 4
print(f"Área del Triángulo: {calcular_area('triangulo', (8, 4))}")

"""
40
Tienda online
"""
print("== Kata 40: ")

try:
    # a. Solicitar al usuario el precio original de un artículo
    precio_original = float(input("Introduce el precio original del artículo: "))

    # b. Preguntar si tiene un cupón de descuento (respuesta sí o no)
    tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").lower().strip()

    # Inicializamos el precio final con el original por defecto
    precio_final = precio_original

    # f. Usar estructuras de control de flujo (if, elif, else)
    if tiene_cupon == "sí" or tiene_cupon == "si":
        # c. Si la respuesta es sí, solicitar el valor del cupón
        valor_cupon = float(input("Introduce el valor del cupón de descuento: "))
        
        # d. Aplicar el descuento siempre que el valor sea válido (mayor a cero)
        if valor_cupon > 0:
            if valor_cupon <= precio_original:
                precio_final = precio_original - valor_cupon
            else:
                # Si el cupón es mayor al precio, el artículo queda a 0
                precio_final = 0
                print("El cupón cubre el total de la compra.")
        else:
            print("Cupón no válido (debe ser mayor a 0). Se mantiene el precio original.")

    elif tiene_cupon == "no":
        print("No se aplicará ningún descuento.")

    else:
        print("Opción no reconocida. Se procederá sin descuento.")

    # e. Mostrar el precio final de la compra
    print("\n--- Resumen de Compra ---")
    print(f"Precio inicial: {precio_original:.2f}€")
    print(f"Precio final a pagar: {precio_final:.2f}€")

except ValueError:
    print("Error: Por favor, introduce valores numéricos válidos para los precios.")