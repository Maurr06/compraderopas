from Preparacion import *

# Interaccion con el usuario
Mi_Tienda.presentacion()

continuar = True
while continuar:
    print("""
        \nSeleccione opcion:
        1. Ver el inventario de la tienda
        2. Añadir objetos a su carrito
        3. Ver su carrito
        4. Comprar lo que hay en su carrito 
        5. Salir""")
     
    validado = False
    while validado == False:
        opcion = input("Ingrese opcion (Numero entero, 1 al 5): ")
        print()
        try: 
            opcion = int(opcion)
            if opcion > 0 and opcion < 6:
                validado = True
        except: pass # Se repite el bucle while
        
        
        
    match(opcion):
        case 1:
            Mi_Tienda.inventario.mostrar_inventario()
                        
        case 2:
            objeto_a_comprar = input("ID del objeto que desea añadir al carrito: ")
            for prenda in Mi_Tienda.inventario.prendas:
                if str(prenda.id) == objeto_a_comprar:
                    # Si se encontro:
                    if Mi_Tienda.inventario.prendas[prenda.id-1].cantidad == 0:
                        print("Stock Agotado.")
                    else:
                        Cliente_1.carrito.añadir_a_carrito(prenda)
                        Mi_Tienda.inventario.prendas[prenda.id-1].cantidad -= 1 # 
                        print(f"Añadido {prenda.nombre} al carrito.")
        
        case 3:
            Cliente_1.carrito.mostrar_carrito()
            
        case 4:
            Cliente_1.carrito.productos.clear()
            print("Compra realizada.")
        
        case 5:
            continuar = False
            