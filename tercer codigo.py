mi_conjunto = set()

for i in range(3):
    elemento = input(f"Ingrese el elemento {i+1} para agregar al conjunto: ")
    mi_conjunto.add(elemento)
print("Conjunto después de add:", mi_conjunto)

elemento_remove = input("Ingrese el elemento que desea eliminar del conjunto: ")
mi_conjunto.remove(elemento_remove)
print("Conjunto después de remove:", mi_conjunto)

otro_conjunto = set()
for i in range(3):
    elemento = input(f"Ingrese el elemento {i+1} para agregar al otro conjunto: ")
    otro_conjunto.add(elemento)

union = mi_conjunto.union(otro_conjunto)
print("Unión de los conjuntos:", union)

interseccion = mi_conjunto.intersection(otro_conjunto)
print("Intersección de los conjuntos:", interseccion)
