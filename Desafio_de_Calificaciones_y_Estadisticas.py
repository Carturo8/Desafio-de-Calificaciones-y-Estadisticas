"""Desarrolla un programa en Python que gestione una serie de calificaciones y estadísticas de manera interactiva."""

def validar_calificacion(mensaje):
    """
    Función para validar una calificación.
    """
    while True:
        try:
            # Solicitar al usuario que ingrese una calificación
            calificacion = round(float(input(mensaje)), 2)
            # Validar que la calificación esté entre 0 y 100
            if 0 <= calificacion <= 100:
                return calificacion
            else:
                print("La calificación debe estar entre 0 y 100. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Ingresa un número válido.")

def validar_calificacion_inicial(mensaje):
    """
    Función para validar una calificación y determinar su estado.
    """
    while True:
        try:
            # Solicitar al usuario que ingrese una calificación
            calificacion = round(float(input(mensaje)), 2)
            # Validar que la calificación esté entre 0 y 100
            if 0 <= calificacion <= 100:
                # Determinar el estado de la calificación
                if calificacion >= 70:
                    print(f"La calificación {calificacion} es válida y su estado es: Aprobado")
                elif 50 < calificacion < 70:
                    print(f"La calificación {calificacion} es válida y su estado es: Requiere nivelación")
                else:
                    print(f"La calificación {calificacion} es válida y su estado es: Reprobado")
                return calificacion
            else:
                print("La calificación debe estar entre 0 y 100. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Ingresa un número válido.")

def procesar_lista_de_calificaciones(lista):
    """
    Función que procesa una lista de calificaciones ingresadas por el usuario.
    Permite corregir calificaciones inválidas y asegura que todas estén en el rango 0-100.
    """
    lista_c: str = input(lista)
    lista_f: list[float] = []
    numero_temporal: str = ""
    numeros_incorrectos: list[str] = []
    caracteres_permitidos = "0123456789."

    # Procesar la entrada inicial
    for caracter in lista_c:
        if caracter == ',' or caracter == ';':
            if numero_temporal:
                try:
                    numero = round(float(numero_temporal), 2)
                    if 0 <= numero <= 100:
                        lista_f.append(numero)
                    else:
                        print(f"Advertencia: La calificación {numero} está fuera del rango 0-100")
                        numeros_incorrectos.append(numero_temporal)
                except ValueError:
                    print(f"Advertencia: '{numero_temporal}' no es un número válido")
                    numeros_incorrectos.append(numero_temporal)
                numero_temporal = ""
        else:
            if caracter in caracteres_permitidos:
                numero_temporal += caracter

    # Procesar el último número
    if numero_temporal:
        try:
            numero = round(float(numero_temporal.strip()), 2)
            if 0 <= numero <= 100:
                lista_f.append(numero)
            else:
                print(f"Advertencia: La calificación {numero} está fuera del rango 0-100")
                numeros_incorrectos.append(numero_temporal.strip())
        except ValueError:
            print(f"Advertencia: '{numero_temporal.strip()}' no es un número válido")
            numeros_incorrectos.append(numero_temporal.strip())

    # Solicitar corrección de números incorrectos
    if numeros_incorrectos:
        for numero in numeros_incorrectos:
            calificacion_corregida = validar_calificacion(f"La calificación '{numero}' es incorrecta. Ingresa una calificación válida: ")
            lista_f.append(calificacion_corregida)
    return lista_f

def calcular_promedio(lista_de_calificaciones):
    """
    Función para calcular el promedio de una lista de calificaciones.
    """
    # Validar que la lista no esté vacía
    if not lista_de_calificaciones:
        return 0.0

    suma: float = 0.0
    for calificacion in lista_de_calificaciones:
        suma += calificacion

    return round(suma / len(lista_de_calificaciones), 2)

def contar_calificaciones_mayores(lista_de_calificaciones, valor_de_comparacion):
    """
    Función para almacenar y contar las calificaciones mayores a un valor de comparación.
    """
    calificaciones_mayores:list[float] = []
    cantidad_calificaciones_mayores:float = 0
    contador:int = 0
    while contador < len(lista_de_calificaciones):
        if lista_de_calificaciones[contador] > valor_de_comparacion:
            calificaciones_mayores.append(lista_de_calificaciones[contador])
            cantidad_calificaciones_mayores += 1
        contador += 1
    return calificaciones_mayores, cantidad_calificaciones_mayores

def contar_calificaciones_iguales(lista_de_calificaciones, valor_de_comparacion):
    """
    Función para contar las calificaciones iguales a un valor de comparación.
    """
    contador:int = 0
    for i in lista_de_calificaciones:
        if valor_de_comparacion != i:
            continue
        contador += 1
    return contador

# Validar la calificación inicial
calificacion_inicial = validar_calificacion_inicial("Ingresa una calificación numérica (0-100): ")

# Validar la lista de calificaciones
lista_calificaciones = procesar_lista_de_calificaciones("\nIngresa calificaciones (0-100) separadas por comas: ")
print(f"\nLa lista de calificaciones es: {lista_calificaciones}")

# Calcular el promedio de las calificaciones
promedio = calcular_promedio(lista_calificaciones)
print(f"El promedio de las calificaciones es: {promedio}")

# Validar el valor de comparación
valor_de_comparacion = validar_calificacion("\nIngresa un valor numérico (0-100) para comparar: ")

# Almacenar y contar las calificaciones mayores al valor de comparación
calificaciones_mayores = contar_calificaciones_mayores(lista_calificaciones, valor_de_comparacion)[0]
cantidad_calificaciones_mayores = contar_calificaciones_mayores(lista_calificaciones, valor_de_comparacion)[1]
print(f"\nNúmero de Calificaciones Mayores a {valor_de_comparacion}: {cantidad_calificaciones_mayores} ---> {calificaciones_mayores}")

# Contar las calificaciones iguales a la calificación de comparación
cantidad_calificaciones_iguales = contar_calificaciones_iguales(lista_calificaciones, valor_de_comparacion)
print(f"Número de calificaciones iguales a {valor_de_comparacion}: {cantidad_calificaciones_iguales}")