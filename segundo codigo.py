mi_lista = []

for i in range(3):
    elemento = input(f"Ingrese el elemento {i+1} para añadir a la lista: ")
    mi_lista.append(elemento)
print("Lista después de append:", mi_lista)

indice = int(input("Ingrese la posición donde desea insertar un nuevo elemento (0 para el inicio): "))
elemento_insert = input("Ingrese el nuevo elemento para insertar: ")
mi_lista.insert(indice, elemento_insert)
print("Lista después de insert:", mi_lista)

ultimo_elemento = mi_lista.pop()
print("Lista después de pop:", mi_lista)
print("Elemento eliminado:", ultimo_elemento)

elemento_remove = input("Ingrese el elemento que desea eliminar de la lista: ")
mi_lista.remove(elemento_remove)
print("Lista después de remove:", mi_lista)

try:
    mi_lista.sort()
    print("Lista ordenada:", mi_lista)
except:
    print("No se puede ordenar la lista debido a la incompatibilidad de tipos.")
