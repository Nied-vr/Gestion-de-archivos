# compras_por_medio_pago.py

# Definir el nombre del archivo
archivo_csv = "SalesJan2009.csv"

# Función para obtener los medios de pago únicos
def obtener_medios_pago():
    with open(archivo_csv, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        medios_pago = set()
        for linea in lineas[1:]:
            columnas = linea.strip().split(",")
            medios_pago.add(columnas[3])  # La columna del medio de pago está en la posición 3
        return list(medios_pago)  # Convertimos el conjunto en lista sin ordenar

# Función para contar compras por medio de pago
def compras_por_medio_pago(medio_pago):
    with open(archivo_csv, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        contador = 0
        for linea in lineas[1:]:
            columnas = linea.strip().split(",")
            if columnas[3] == medio_pago:
                contador += 1
        return contador

# Prueba del código
if __name__ == "__main__":
    medios_pago_disponibles = obtener_medios_pago()

    print("\nLista de medios de pago disponibles:")
    for medio in medios_pago_disponibles:
        print(f"- {medio}")

    # Validación para asegurar que el medio de pago ingresado existe en la lista
    while True:
        medio_pago = input("\nIngrese el método de pago a consultar: ")
        if medio_pago in medios_pago_disponibles:
            break
        print("❌ Medio de pago no encontrado. Inténtelo nuevamente.")

    print(f"\nCompras con {medio_pago}: {compras_por_medio_pago(medio_pago)}")
