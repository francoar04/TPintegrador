# TPintegrador
tp integrador Camba, Carcano, Cisneros
# Gestión de Datos de Países en Python

# Descripción del programa
Aplicación interactiva en consola desarrollada en Python 3 para gestionar y analizar datos geográficos y demográficos de países leídos desde un archivo CSV. Permite realizar búsquedas por nombre, filtrados por diversos criterios, ordenamientos personalizados y cálculo de estadísticas generales.

# Instrucciones de uso
1. Asegurarse de tener el archivo `main.py` y el archivo `paises.csv` en el mismo directorio.
2. Abrir una terminal o consola de comandos en dicha carpeta.
3. Ejecutar el script con el siguiente comando:
   ```bash
   python main.py

# Ejemplos de Entrada-Salida

1. BUSQUEDA POR NOMBRE
ingresa: Argentina
salida: Nombre: Argentina | Población: 45376763 | Superficie: 2780400 km² | Continente: América

2. FILTRAR POR CONTINENTE
opción de filtro: 1 (continente)
continente: Europa
salida: Nombre: Alemania | Población: 83149300 | Superficie: 357022 km² | Continente: Europa

3. ORDENAR PAISES POR POBLACIÓN
opción de filtro: 2(rango de población)
Población mínima: 10000000
Población máxima: 100000000
salida:                 
Nombre: Argentina | Población: 45376763 | Superficie: 2780400 km² | Continente: América
Nombre: Alemania | Población: 83149300 | Superficie: 357022 km² | Continente: Europa
Nombre: Australia | Población: 25687041 | Superficie: 7692024 km² | Continente: Oceanía

4. MOSTRAR CARACTERISTICAS
opción de filtro: 4
salida: País con mayor población: Brasil (213993437)
País con menor población: Australia (25687041)
Promedio de población: 99390157.50
Promedio de superficie: 3454273.00
Cantidad de países por continente:
 - América: 2
 - Asia: 1
 - Europa: 1
 - África: 1
 - Oceanía: 1