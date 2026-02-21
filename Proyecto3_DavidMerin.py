"""1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
de cada letra en la cadena. Los espacios no deben ser considerados."""

def diccionario(texto):
    frecuencias = {}

    for caracter in texto:
        if caracter == " ":
            continue  # ignoramos los espacios

        if caracter in frecuencias:
            frecuencias[caracter] += 1
        else:
            frecuencias[caracter] = 1

    return frecuencias

print(diccionario("Pablo clavo un clavito oh oh"))


"""2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()"""
def lista_doble(numeros):
    resultado = list(map(lambda x: x * 2, numeros))
    return resultado


lista = [5, 10, 15, 20]
print(lista_doble(lista))

"""3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo."""
def filtrar_palabras(lista_palabras, objetivo):
    resultado = []

    for palabra in lista_palabras:
        if objetivo in palabra:
            resultado.append(palabra)

    return resultado


palabras = ["mago", "magia", "mama", "mando"]
print(filtrar_palabras(palabras, "mag"))

"""4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()"""
def diferencia_valor_listas(lista1, lista2):
    resultado = list(map(lambda x, y: x - y, lista1, lista2))
    return resultado


lista1 = [1, 2, 2]
lista2 = [0, 2, 4]

print(diferencia_valor_listas(lista1, lista2))

"""5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
una tupla que contenga la media y el estado."""
def evaluar_notas(lista_numeros, nota_aprobado=5):
    media = sum(lista_numeros) / len(lista_numeros)

    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"

    return (media, estado)


notas = [3, 7, 5, 8]
print(evaluar_notas(notas))

"""6. Escribe una función que calcule el factorial de un número de manera recursiva."""
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

"""7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()"""
def tuplas_a_strings(lista_tuplas):
    resultado = list(map(lambda t: t[0] + " tiene " + str(t[1]) + " años", lista_tuplas))
    return resultado


personas = [("Ana", 20), ("Luis", 25), ("Marta", 30)]
print(tuplas_a_strings(personas))

"""8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
indicando si la división fue exitosa o no."""
try:
    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))

    resultado = numero1 / numero2

except ValueError:
    print("Error: debes introducir valores numéricos.")

except ZeroDivisionError:
    print("Error: no se puede dividir entre cero.")

else:
    print("División realizada correctamente.")
    print("Resultado:", resultado)

finally:
    print("Fin del programa.")

"""9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()"""
def filtrar_mascotas(lista_mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

    resultado = list(filter(lambda mascota: mascota not in prohibidas, lista_mascotas))

    return resultado


mascotas = ["Perro", "Gato", "Mapache", "Loro", "Tigre", "Conejo"]
print(filtrar_mascotas(mascotas))

"""10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
excepción personalizada y maneja el error adecuadamente."""
class lista_vacia_error(Exception):
    pass


def calcular_promedio(lista_numeros):
    if len(lista_numeros) == 0:
        raise lista_vacia_error("La lista está vacía, no se puede calcular el promedio.")

    promedio = sum(lista_numeros) / len(lista_numeros)
    return promedio


try:
    numeros = [7, 8, 9]
    print("Promedio:", calcular_promedio(numeros))

except lista_vacia_error as e:
    print("Error:", e)

"""11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
adecuadamente."""
try:
    edad = int(input("Introduce tu edad: "))

    if edad < 0 or edad > 120:
        raise ValueError("La edad debe estar entre 0 y 120.")

except ValueError as e:
    print("Error:", e)

else:
    print("Edad registrada correctamente.")
    print("Tu edad es:", edad)

finally:
    print("Fin del programa.")

"""12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()"""
def longitud_palabras(frase):
    palabras = frase.split()

    resultado = list(map(lambda palabra: len(palabra), palabras))

    return resultado


frase = "Estoy haciendo cosas del master un viernes"
print(longitud_palabras(frase))

"""13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()"""
def letras_mayus_minus(caracteres):
    # Lo había hecho con set(caracteres), pero no mantenia el orden de las letras, así que:
    letras_unicas = []

    for letra in caracteres:
        if letra not in letras_unicas:
            letras_unicas.append(letra)

    return list(map(lambda letra: (letra.upper(), letra.lower()), letras_unicas))


iniciales = "viernes"
print(letras_mayus_minus(iniciales))

"""14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
función filter()"""
def filtrar_por_letra(lista_palabras, letra):
    resultado = list(filter(lambda palabra: palabra.startswith(letra), lista_palabras))
    return resultado


productos = ["manzana", "melón", "pera", "mango", "plátano"]
print(filtrar_por_letra(productos, "m"))

"""15. Crea una función lambda que sume 3 a cada número de una lista dada."""
def sumar_tres(lista_numeros):
    resultado = list(map(lambda numero: numero + 3, lista_numeros))
    return resultado


ventas = [10, 20, 30, 40]
print(sumar_tres(ventas))

"""16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
todas las palabras que sean más largas que n. Usa la función filter()"""
def palabras_mas_largas(frase, n):
    palabras = frase.split()

    resultado = list(filter(lambda palabra: len(palabra) > n, palabras))

    return resultado


texto = "Las katas de Python son entretenidas y laboriosas"
print(palabras_mas_largas(texto, 8))

"""17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
corresponde al número quinientos setenta y dos (572). Usa la función reduce()"""
from functools import reduce

def digitos_a_numero(lista_digitos):
    numero = reduce(lambda acumulado, digito: acumulado * 10 + digito, lista_digitos)
    return numero


codigo = [2, 0, 2, 6]
print(digitos_a_numero(codigo))

"""18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
90. Usa la función filter()"""
def filtrar_estudiantes(lista_estudiantes):
    resultado = list(filter(lambda estudiante: estudiante["calificacion"] >= 90, lista_estudiantes))
    return resultado


estudiantes = [
    {"nombre": "David", "edad": 36, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 88},
    {"nombre": "Ana", "edad": 42, "calificacion": 91},
    {"nombre": "Carlos", "edad": 35, "calificacion": 85}
]

print(filtrar_estudiantes(estudiantes))

"""19. Crea una función lambda que filtre los números impares de una lista dada."""
def filtrar_impares(lista_numeros):
    resultado = list(filter(lambda numero: numero % 2 != 0, lista_numeros))
    return resultado


numeros = [3, 15, 20, 33, 40, 99]
print(filtrar_impares(numeros))

"""20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
filter()"""
def filtrar_enteros(lista_mixta):
    resultado = list(filter(lambda valor: isinstance(valor, int), lista_mixta))
    return resultado


datos = [10, "David", 25, "es", 33, "viernes"]
print(filtrar_enteros(datos))

"""21. Crea una función que calcule el cubo de un número dado mediante una función lambda"""
def calculo_cubo(numero):
    cubo = lambda x: x ** 3
    return cubo(numero)


valor = 4
print(calculo_cubo(valor))

""""22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() ."""
from functools import reduce

def producto_total(lista_numeros):
    resultado = reduce(lambda acumulado, numero: acumulado * numero, lista_numeros)
    return resultado


cantidades = [3, 4, 10]
print(producto_total(cantidades))

"""23. Concatena una lista de palabras.Usa la función reduce() ."""
from functools import reduce

def concatenar_palabras(lista_palabras):
    resultado = reduce(lambda acumulado, palabra: acumulado + " " + palabra, lista_palabras)
    return resultado


palabras = ["la", "planta", "del", "escritorio", "necesita", "agua"]
print(concatenar_palabras(palabras))

"""24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() ."""
from functools import reduce

def diferencia_total(lista_numeros):
    resultado = reduce(lambda acumulado, numero: acumulado - numero, lista_numeros)
    return resultado


valores = [100, 90, 5, 4]
print(diferencia_total(valores))

"""25. Crea una función que cuente el número de caracteres en una cadena de texto dada."""
def contar_caracteres(texto):
    total = len(texto)
    return total


frase = "la planta del escritorio se ha muerto"
print(contar_caracteres(frase))

"""26. Crea una función lambda que calcule el resto de la división entre dos números dados."""
def calcular_resto(a, b):
    resto = lambda x, y: x % y
    return resto(a, b)


numero1 = 17
numero2 = 5
print(calcular_resto(numero1, numero2))

"""27. Crea una función que calcule el promedio de una lista de números."""
def calcular_promedio(lista_numeros):
    suma_total = sum(lista_numeros)
    cantidad = len(lista_numeros)

    promedio = suma_total / cantidad
    return promedio


produccion = [10, 10, 5, 30, 5, 0]
print(calcular_promedio(produccion))

"""28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada."""
def primer_duplicado(lista):
    vistos = set()

    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)

    return None


numeros = [3, 7, 2, 5, 7, 9]
print(primer_duplicado(numeros))

"""29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
carácter '#', excepto los últimos cuatro."""
def enmascarar_dato(valor):
    texto = str(valor)

    if len(texto) <= 4:
        return texto

    parte_oculta = "#" * (len(texto) - 4)
    ultimos_cuatro = texto[-4:]

    return parte_oculta + ultimos_cuatro


dni = "12345678Z"
print(enmascarar_dato(dni))

"""30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
pero en diferente orden."""
def son_anagramas(palabra1, palabra2):
    p1 = sorted(palabra1.lower())
    p2 = sorted(palabra2.lower())

    return p1 == p2


print(son_anagramas("rosa", "amor"))
print(son_anagramas("monja", "jamon"))

"""31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
lanza una excepción."""
try:
    entrada = input("Introduce empleados separados por comas: ")
    empleados = [nombre.strip() for nombre in entrada.split(",")]

    empleado_buscar = input("Introduce el empleado que quieres verificar: ")

    if empleado_buscar in empleados:
        print("Empleado encontrado en el sistema.")
    else:
        raise ValueError("El empleado no está registrado.")

except ValueError as e:
    print("Error:", e)

finally:
    print("Proceso finalizado.")

"""32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
no trabaja aquí."""
def buscar_empleado(nombre_completo, lista_empleados):
    for empleado in lista_empleados:
        if empleado["nombre"] == nombre_completo:
            return empleado["puesto"]

    return "La persona no trabaja aquí."


empleados = [
    {"nombre": "Carlos Martínez", "puesto": "Jefe de Producción"},
    {"nombre": "Laura Sánchez", "puesto": "Responsable de Calidad"},
    {"nombre": "Javier Torres", "puesto": "Planificación"},
    {"nombre": "Elena Romero", "puesto": "Logística"}
]

print(buscar_empleado("Laura Sánchez", empleados))

"""33. Crea una función lambda que sume elementos correspondientes de dos listas dadas."""
def sumar_listas(lista1, lista2):
    resultado = list(map(lambda x, y: x + y, lista1, lista2))
    return resultado


produccion_linea1 = [120, 135, 150]
produccion_linea2 = [100, 110, 130]

print(sumar_listas(produccion_linea1, produccion_linea2))

"""34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
manipular la estructura del árbol."""
#CÓDIGO
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        indice = posicion - 1
        if indice < 0 or indice >= len(self.ramas):
            raise IndexError("Posición de rama no válida.")
        self.ramas.pop(indice)

    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }

# CASO DE USO 
arbol = Arbol()
arbol.crecer_tronco()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.nueva_rama()
arbol.nueva_rama()
arbol.quitar_rama(2)  

print(arbol.info_arbol())

"""36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
agregar dinero al saldo."""
# CÓDIGO
class UsuarioBanco:
    def __init__(self, nombre, saldo, tiene_cuenta):
        self.nombre = nombre
        self.saldo = saldo
        self.tiene_cuenta = tiene_cuenta

    def retirar_dinero(self, cantidad):
        if not self.tiene_cuenta:
            raise ValueError("El usuario no tiene cuenta corriente.")
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        if not self.tiene_cuenta or not otro_usuario.tiene_cuenta:
            raise ValueError("Ambos usuarios deben tener cuenta corriente.")
        if cantidad > otro_usuario.saldo:
            raise ValueError("El usuario origen no tiene saldo suficiente.")

        otro_usuario.saldo -= cantidad
        self.saldo += cantidad

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

# CASO DE USO
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

bob.agregar_dinero(20)

try:
    alicia.transferir_dinero(bob, 80)  # aquí falla porque Bob solo tiene 70
except ValueError as e:
    print("Transferencia fallida:", e)

try:
    alicia.retirar_dinero(50)  
except ValueError as e:
    print("Retirada fallida:", e)

print("Saldo Alicia:", alicia.saldo)
print("Saldo Bob:", bob.saldo)

"""37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
de la función procesar_texto ."""
# CÓDIGO
def contar_palabras(texto):
    palabras = texto.split()
    conteo = {}

    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1

    return conteo


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)


def eliminar_palabra(texto, palabra):
    palabras = texto.split()
    palabras_filtradas = [p for p in palabras if p != palabra]
    return " ".join(palabras_filtradas)


def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)

    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])

    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])

    else:
        raise ValueError("Opción no válida.")


# CASO DE USO
texto = "produccion calidad produccion logistica calidad produccion"

print("Contar:")
print(procesar_texto(texto, "contar"))

print("\nReemplazar:")
print(procesar_texto(texto, "reemplazar", "produccion", "fabricacion"))

print("\nEliminar:")
print(procesar_texto(texto, "eliminar", "calidad"))

"""38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario."""
try:
    entrada = input("Introduce la hora (HH:MM): ")

    partes = entrada.split(":")
    hora = int(partes[0])
    minutos = int(partes[1])

    if hora < 0 or hora > 23 or minutos < 0 or minutos > 59:
        raise ValueError("Hora no válida.")

    if 6 <= hora < 12:
        momento = "Es de mañana."
    elif 12 <= hora < 20:
        momento = "Es de tarde."
    else:
        momento = "Es de noche."

    print(momento)

except (ValueError, IndexError):
    print("Formato incorrecto. Usa HH:MM.")

finally:
    print("Programa finalizado.")

"""39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica."""
try:
    nota = float(input("Introduce la nota del alumno (0-100): "))

    if nota < 0 or nota > 100:
        raise ValueError("La nota debe estar entre 0 y 100.")

    if nota <= 69:
        calificacion = "Insuficiente"
    elif nota <= 79:
        calificacion = "Bien"
    elif nota <= 89:
        calificacion = "Muy bien"
    else:
        calificacion = "Excelente"

    print("Calificación:", calificacion)

except ValueError as e:
    print("Error:", e)

finally:
    print("Programa finalizado.")

"""40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
"triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura)."""
import math

def calcular_area(figura, datos):

    if figura == "rectangulo":
        base, altura = datos
        area = base * altura

    elif figura == "circulo":
        (radio,) = datos
        area = math.pi * radio ** 2

    elif figura == "triangulo":
        base, altura = datos
        area = (base * altura) / 2

    else:
        raise ValueError("Figura no válida.")

    print(f"El área del {figura} es: {area:.2f}") #le he añadido este print para que no apareciera directamente el área calculada
    return area


calcular_area("rectangulo", (10, 5))
calcular_area("circulo", (7,))
calcular_area("triangulo", (8, 4))

"""41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
monto final de una compra en una tienda en línea, después de aplicar un descuento."""
try:
    precio_original = float(input("Introduce el precio original del artículo (€): "))

    if precio_original <= 0:
        raise ValueError("El precio debe ser mayor que 0.")

    tiene_cupon = input("¿Tienes cupón? (si/no): ").lower()

    # para hacerlo más realista, le he añadido que en lugar de poner el precio de descuento, tengas que escribir el código del cupón:
    cupones = {
        "DESC10": 10,
        "DESC20": 20,
        "PROMO15": 15
    }

    if tiene_cupon == "si":
        codigo = input("Introduce el código del cupón: ").upper()

        if codigo in cupones:
            descuento = cupones[codigo]
            precio_final = precio_original - descuento

            if precio_final < 0:
                precio_final = 0

            print(f"Cupón aplicado: -{descuento} €")
            print(f"Precio final: {precio_final:.2f} €")
        else:
            print("Código no válido. Precio sin descuento.")
            print(f"Precio final: {precio_original:.2f} €")

    elif tiene_cupon == "no":
        print(f"Precio final sin descuento: {precio_original:.2f} €")

    else:
        print("Respuesta no válida.")

except ValueError as e:
    print("Error:", e)

finally:
    print("Proceso finalizado.")

## GRACIAS!! 