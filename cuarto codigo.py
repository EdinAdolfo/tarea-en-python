direccion = {}
for i in range(5):
    if i == 0:
        clave = "calle"
    elif i == 1:
        clave = "zona"
    elif i == 2:
        clave = "ciudad"
    elif i == 3:
        clave = "numero_casa"
    else:
        clave = "codigo_postal"
    
    valor = input(f"Ingrese el valor para '{clave}': ")
    direccion[clave] = valor

print("\nDirección completa ingresada:", direccion)

clave_busqueda = input("\nIngrese la clave para obtener su valor (calle, zona, ciudad, numero_casa, codigo_postal): ")
valor = direccion.get(clave_busqueda)
print(f"Valor obtenido con get para '{clave_busqueda}': {valor}")

copia_direccion = direccion.copy()
print("\nCopia de la dirección:", copia_direccion)

claves_adicionales = ["pais", "provincia", "referencia"]
valor_comun = input("\nIngrese un valor común para los datos adicionales (como 'Guatemala' o 'Desconocido'): ")
nueva_direccion = dict.fromkeys(claves_adicionales, valor_comun)
print("Nuevo diccionario con datos adicionales creado con fromkeys:", nueva_direccion)

direccion.clear()
print("\nDiccionario original después de clear (limpiado):", direccion)
