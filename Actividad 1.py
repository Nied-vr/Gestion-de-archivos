def obtener_paises():
    with open("SalesJan2009.csv", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        paises = set()  
        for linea in lineas[1:]:
            columnas = linea.strip().split(",")
            paises.add(columnas[7])  
        return list(paises)  


def compras(pais):
    with open("SalesJan2009.csv", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        contador = 0
        for linea in lineas[1:]:
            columnas = linea.strip().split(",")
            if columnas[7] == pais:
                contador += 1
        return contador

paises_disponibles = obtener_paises()

print("\nLista de países disponibles:")
for pais in paises_disponibles:
    print(f"- {pais}")

while True:
    pais = input("\nIngrese el país a consultar: ")
    if pais in paises_disponibles:
        break
    print("País no encontrado. Vuelvalo a intentar.")

print(f"\nCompras en {pais}: {compras(pais)}")