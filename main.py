import funciones as fn

def main():
    lista_productos = []
    while True:
        fn.menu_principal()
        opcion = fn.leer_opcion()
        
        if opcion == 1:
            print("1")
        elif opcion == 2:
            print("2")
        elif opcion == 3:
            print("3")
        elif opcion == 4:
            fn.registro_prod(lista_productos)
        elif opcion == 5:
            eliminar = input("Que producto desea eliminar? :").lower()
            posicion = fn.buscar_codigo(lista_productos, eliminar)
            if posicion != -1:
                lista_productos.pop(posicion)
                print("producto eliminado")
            else:
                print(f"No se encontro el producto {eliminar}")
        elif opcion == 6:
            print("Programa finalizado.")
            break
        else:
            return
if __name__ == "__main__":
    main()