from Preparacion import *

# Interaccion con el usuario
Mi_Tienda.presentacion()

continuar = True
while continuar:
    print("\n¿Desea comprar algo (escriba 1), ver el inventario (escriba 2), o salir (escriba 3)?")
     
    validado = False
    while validado == False:
        opcion = input("Ingrese opcion (Numero entero, 1 al 3): ")
        
        try: 
            opcion = int(opcion)
            if opcion > 0 and opcion < 4:
                validado = True
        except: pass # Se repite el bucle while
        
        
        
    match(opcion):
        case 1:
            objeto_a_comprar = input("ID del objeto que desea comprar: ")
            for prenda in Mi_Tienda.inventario.prendas:
                if str(prenda.id) == objeto_a_comprar:
                    # Si se encontro:
                    if Mi_Tienda.inventario.prendas[prenda.id-1].cantidad == 0:
                        print("Stock Agotado.")
                    else:
                        Mi_Tienda.inventario.prendas[prenda.id-1].cantidad -= 1 # 
                        print("Compra realizada con exito.")
                        
        
        case 2:
            Mi_Tienda.inventario.mostrar_inventario()
        
        case 3:
            continuar = False
            