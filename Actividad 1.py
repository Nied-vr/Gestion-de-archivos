# compras_por_pais.py

# Definir el nombre del archivo
archivo_csv = "SalesJan2009.csv"

# Función para obtener los países únicos en el archivo
def obtener_paises():
    with open(archivo_csv, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        paises = set()  # Usamos un conjunto para evitar duplicados
        for linea in lineas[1:]:
            columnas = linea.strip().split(",")
            paises.add(columnas[7])  # La columna del país está en la antepenúltima posición
        return list(paises)  # Convertimos el conjunto en lista sin ordenar

# Función para contar compras por país
def compras_por_pais(pais):
    with open(archivo_csv, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        contador = 0
        for linea in lineas[1:]:
            columnas = linea.strip().split(",")
            if columnas[7] == pais:
                contador += 1
        return contador

# Prueba del código
if __name__ == "__main__":
    paises_disponibles = obtener_paises()
    
    print("\nLista de países disponibles:")
    for pais in paises_disponibles:
        print(f"- {pais}")

    # Validación para asegurar que el país ingresado existe en la lista
    while True:
        pais = input("\nIngrese el país a consultar: ")
        if pais in paises_disponibles:
            break
        print("❌ País no encontrado. Inténtelo nuevamente.")

    print(f"\nCompras en {pais}: {compras_por_pais(pais)}")
