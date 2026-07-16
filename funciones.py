def menu_principal():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    try:
        opcion = int(input("Que desea hacer ? : "))
        return opcion
    except ValueError:
        return -1

def val_codigo(codigo):
    return len(codigo.strip()) > 0
def val_nombre(nombre):
    return len(nombre.strip()) > 0
def val_cat(categoria):
    return len(categoria.strip()) > 0
def val_marca(marca):
    return len(marca.strip()) > 0
def val_peso(peso):
    try:
        valor = float(peso)
        return 0.0 <= valor
    except ValueError:
        return False
def val_import(importado):
    return len(importado.strip()) > 0
def val_cachorro(cachorro):
    return len(cachorro.strip()) > 0
def val_precio(precio):
    try:
        valor = int(precio)
        return valor > 0
    except ValueError:
        return False
def val_uni(unidades):
    try:
        valor = int(unidades)
        return valor > 0
    except ValueError:
        return False

def registro_prod(lista_prod):
        print("\n=== Registrar Producto ===")
        cod = input("Ingrese código del producto:  ")
        nom = input("Ingrese nombre: ")
        cat = input("Ingrese categoría: ")
        mar = input("Ingrese marca: ")
        pes = input("Ingrese peso (kg): ")
        imp = input("¿Es importado? (s/n): ")
        cac = input("¿Es para cachorro? (s/n): ")
        pre = input("Ingrese precio: ")
        uni = input("Ingrese unidades: ")
        if not val_codigo(cod):
            print("Error")
            return
        if not val_nombre(nom):
            print("Error")
            return
        if not val_cat(cat):
            print("Error")
            return
        if not val_marca(mar):
            print("Error")
            return
        if not val_peso(pes):
            print("Error")
            return
        if not val_import(imp):
            print("Error")
            return
        if not val_cachorro(cac):
            print("Error")
            return
        if not val_precio(pre):
            print("Error")
            return
        if not val_uni(uni):
            print("Error")
            return
        nuevo_prod = {
            "codigo" : cod.strip,
            "nombre" : nom.strip,
            "categoria" : cat.strip,
            "marca" : mar.strip,
            "peso" : float(pes),
            "importado" : imp.strip,
            "cachorro" : cac.strip,
            "precio" : int(pre),
            "unidades" : int(uni)
        }
        lista_prod.append(nuevo_prod)
        print("Producto añadido con exito")
    
def buscar_codigo(lista_prod, buscar_code):
    for i in range(len(lista_prod)):
        if lista_prod [i] ["codigo"].lower() == buscar_code.strip().lower():
            return i
    return -1
        