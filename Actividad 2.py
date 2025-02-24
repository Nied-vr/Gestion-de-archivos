def obtener_medios_de_pago():
    with open("SalesJan2009.csv", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        medios_de_pago = set()
        for linea in lineas[1:]:
            columnas = linea.strip().split(",")
            medios_de_pago.add(columnas[3])
        return list(medios_de_pago)

def compras_por_medio_pago(medio_de_pago):
    with open("SalesJan2009.csv", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        contador = 0
        for linea in lineas[1:]:
            columnas = linea.strip().split(",")
            if columnas[3] == medio_de_pago:
                contador += 1
        return contador

medios_de_pago_disponibles = obtener_medios_de_pago()

print("\nLista de medios de pago disponibles:")
for medio in medios_de_pago_disponibles:
    print(f"- {medio}")

while True:
    medio_de_pago = input("\nIngrese el método de pago a consultar: ")
    if medio_de_pago in medios_de_pago_disponibles:
        break
    print("Medio de pago no encontrado. Vuelvalo a intentar")

print(f"\nCompras con {medio_de_pago}: {compras_por_medio_pago(medio_de_pago)}")