elemento1 = input("Ingrese el primer elemento de la tupla: ")
elemento2 = input("Ingrese el segundo elemento de la tupla: ")
elemento3 = input("Ingrese el tercer elemento de la tupla: ")

mi_tupla = (elemento1, elemento2, elemento3)
print("Tupla creada:", mi_tupla)

print("Primer elemento de la tupla:", mi_tupla[0])
print("Último elemento de la tupla:", mi_tupla[-1])

a, b, c = mi_tupla
print("Valores desempaquetados:", a, b, c)
