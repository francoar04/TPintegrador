import csv
import os

def cargar_datos_csv(ruta_archivo):
    paises = []
    if not os.path.exists(ruta_archivo):
        print(f"Error: El archivo '{ruta_archivo}' no existe.")
        return paises

    archivo = open(ruta_archivo, mode='r', encoding='utf-8')
    lector = csv.DictReader(archivo)
    for fila in lector:
        pob_str = fila['poblacion'].strip()
        sup_str = fila['superficie'].strip()
        
        if pob_str.isdigit() and sup_str.isdigit():
            paises.append({
                'nombre': fila['nombre'].strip(),
                'poblacion': int(pob_str),
                'superficie': int(sup_str),
                'continente': fila['continente'].strip()
            })
        else:
            print("Error de formato en una línea del CSV. Registro omitido.")
    archivo.close()

    return paises

def solicitar_entero_positivo(mensaje):
    while True:
        entrada = input(mensaje).strip()
        if entrada.isdigit():
            return int(entrada)
        print("Entrada inválida. Ingrese un número entero positivo.")

def mostrar_paises(lista):
    if not lista:
        print("No hay países para mostrar.")
        return
    for p in lista:
        print(f"Nombre: {p['nombre']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km² | Continente: {p['continente']}")

def buscar_pais(paises):
    nombre = input("Ingrese el nombre del país a buscar: ").strip().lower()
    resultados = [p for p in paises if nombre in p['nombre'].lower()]
    mostrar_paises(resultados)

def filtrar_paises(paises):
    print("1. Por Continente\n2. Por Rango de Población\n3. Por Rango de Superficie")
    opcion = input("Seleccione filtro (1-3): ").strip()
    resultados = []

    if opcion == "1":
        cont = input("Ingrese continente: ").strip().lower()
        resultados = [p for p in paises if p['continente'].lower() == cont]
    elif opcion == "2":
        min_p = solicitar_entero_positivo("Población mínima: ")
        max_p = solicitar_entero_positivo("Población máxima: ")
        resultados = [p for p in paises if min_p <= p['poblacion'] <= max_p]
    elif opcion == "3":
        min_s = solicitar_entero_positivo("Superficie mínima: ")
        max_s = solicitar_entero_positivo("Superficie máxima: ")
        resultados = [p for p in paises if min_s <= p['superficie'] <= max_s]
    else:
        print("Opción inválida.")
        return

    mostrar_paises(resultados)

def ordenar_paises(paises):
    print("1. Por Nombre\n2. Por Población\n3. Por Superficie")
    criterio = input("Seleccione criterio (1-3): ").strip()
    mapa = {"1": "nombre", "2": "poblacion", "3": "superficie"}

    if criterio not in mapa:
        print("Criterio inválido.")
        return

    print("1. Ascendente\n2. Descendente")
    sentido = input("Seleccione sentido (1-2): ").strip()
    if sentido not in ["1", "2"]:
        print("Sentido inválido.")
        return

    reverso = sentido == "2"
    ordenados = sorted(paises, key=lambda x: x[mapa[criterio]], reverse=reverso)
    mostrar_paises(ordenados)

def mostrar_estadisticas(paises):
    if not paises:
        print("No hay datos.")
        return

    mayor_pob = max(paises, key=lambda x: x['poblacion'])
    menor_pob = min(paises, key=lambda x: x['poblacion'])
    prom_pob = sum(x['poblacion'] for x in paises) / len(paises)
    prom_sup = sum(x['superficie'] for x in paises) / len(paises)

    conteo_cont = {}
    for p in paises:
        conteo_cont[p['continente']] = conteo_cont.get(p['continente'], 0) + 1

    print(f"País con mayor población: {mayor_pob['nombre']} ({mayor_pob['poblacion']})")
    print(f"País con menor población: {menor_pob['nombre']} ({menor_pob['poblacion']})")
    print(f"Promedio de población: {prom_pob:.2f}")
    print(f"Promedio de superficie: {prom_sup:.2f}")
    print("Cantidad de países por continente:")
    for c, cant in conteo_cont.items():
        print(f" - {c}: {cant}")

def menu():
    paises = cargar_datos_csv("paises.csv")
    if not paises:
        return

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Buscar país por nombre")
        print("2. Filtrar países")
        print("3. Ordenar países")
        print("4. Mostrar estadísticas")
        print("5. Salir")

        op = input("Opción: ").strip()
        if op == "1":
            buscar_pais(paises)
        elif op == "2":
            filtrar_paises(paises)
        elif op == "3":
            ordenar_paises(paises)
        elif op == "4":
            mostrar_estadisticas(paises)
        elif op == "5":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()