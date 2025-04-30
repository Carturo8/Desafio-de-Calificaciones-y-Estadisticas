"""Desarrolla un programa en Python que gestione una serie de calificaciones y estadísticas de manera interactiva."""

def Validar_Calificacion(calificacion):
    """
    Función para validar una calificación.
    """
    while True:
        try:
            # Solicitar al usuario que ingrese una calificación
            valor = round(float(input(calificacion)), 2)
            # Validar que la calificación esté entre 0 y 100
            if 0 <= valor <= 100:
                return valor
            else:
                print("La calificación debe estar entre 0 y 100.")
        except ValueError:
            print("Entrada inválida. Ingresa un número válido.")

def Estado_de_Aprobacion(calificacion_inicial):
    """
    Función para determinar el estado de aprobación de un estudiante.
    """
    if calificacion_inicial >= 70:
        return "Aprobado"
    elif calificacion_inicial > 50 < 70:
        return "Regular"
    else:
        return "Reprobado"

lista_c = input("Ingresa las calificaciones separadas por comas: ")

def Validar_Lista_de_Calificaciones():
    """
    Función para obtener una lista de calificaciones.
    """
    lista:list[float] = []
    for i in range(1, 6, 1):
        # Validar la calificación
        calificaciones = Validar_Calificacion(f"Ingresa la calificación No.{i}: ")
        # Agregar la calificación a la lista
        lista.append(calificaciones)
    return lista

def Promedio_de_Calificaciones(lista):
    """
    Función para el promedio de una lista de calificaciones.
    """
    suma = float(sum(lista))
    promedio = round(float(suma / len(lista)), 2)
    return promedio

def Conteo_Calificaciones_Mayores(lista_calificaciones):
    """
    Función para almacenar y contar las calificaciones mayores a un valor de comparación.
    """
    calificaciones_mayores:list[float] = []
    cantidad_calificaciones_mayores:float = 0
    contador:int = 0
    while contador < len(lista_calificaciones):
        if lista_calificaciones[contador] > calificacion_de_comparacion:
            calificaciones_mayores.append(lista_calificaciones[contador])
            cantidad_calificaciones_mayores += 1
        contador += 1
    return calificaciones_mayores, cantidad_calificaciones_mayores

def Conteo_Calificaciones_Iguales(lista_calificaciones):
    """
    Función para contar las calificaciones iguales a un valor de comparación.
    """
    contador:int = 0
    for i in lista_calificaciones:
        if calificacion_de_comparacion == i:
            contador += 1
    return contador

calificacion_inicial = Validar_Calificacion("Ingresa la calificación inicial: ") # Validar la calificación inicial
estado_aprobacion = Estado_de_Aprobacion(calificacion_inicial) # Determinar el estado de aprobación
lista_calificaciones = Validar_Lista_de_Calificaciones() # Validar la lista de calificaciones
promedio = Promedio_de_Calificaciones(lista_calificaciones) # Calcular el promedio de las calificaciones
calificacion_de_comparacion = Validar_Calificacion("Ingresa la calificación para comparar: ") # Validar la calificación de comparación
calificaciones_mayores = Conteo_Calificaciones_Mayores(lista_calificaciones)[0] # Almacenar las calificaciones mayores a la calificación de comparación
cantidad_calificaciones_mayores = Conteo_Calificaciones_Mayores(lista_calificaciones)[1] # Contar las calificaciones mayores a la calificación de comparación
cantidad_calificaciones_iguales = Conteo_Calificaciones_Iguales(lista_calificaciones) # Contar las calificaciones iguales a la calificación de comparación

# Mostrar toda la información de las calificaciones
print(f"""=====================================
Información de las Calificaciones:
=====================================
- Calificación Inicial: {calificacion_inicial}
- Estado de Aprobación: {estado_aprobacion}
- Lista de Calificaciones: {lista_calificaciones}
- Promedio de las Calificaciones: {promedio}
- Calificación de Comparación: {calificacion_de_comparacion}
- Número de Calificaciones Mayores a {calificacion_de_comparacion}: {cantidad_calificaciones_mayores} ---> {calificaciones_mayores}
- Número de Calificaciones Iguales a {calificacion_de_comparacion}: {cantidad_calificaciones_iguales}""")