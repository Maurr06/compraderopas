class prenda: # encapsulacion y abstraccion en las clases
    def __init__(self, nombre, precio, cantidad):
        self.id = inventario.ultimo
        inventario.ultimo += 1
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    def mostrar_info(self):
        print(f"\nID: {self.id}. \nNombre: {self.nombre}. \nPrecio: {self.precio}. \nCantidad: {self.cantidad}")

class RopaHombre(prenda): # Herencia
    def __init__(self, nombre, precio, cantidad, talle): #Polimorfismo
        super().__init__(nombre, precio, cantidad)
        self.talle = talle

class RopaMujer(prenda): 
    def __init__(self, nombre, precio, cantidad, color):
        super().__init__(nombre, precio, cantidad)
        self.color = color

class inventario:
    prendas = []
    ultimo = 1
    
    def agregar_prenda(self, ropa):
        self.prendas.append(ropa)
        # self.ultimo += 1 
        # No entiendo por que no funciona si hago esto. Si saco ultimo += 1 del init de prenda y uso aca, todos los ID salen 0
    
    def mostrar_inventario(self):
        for prenda in self.prendas:
            prenda.mostrar_info()

class tienda:
    def __init__(self, nombre, ubicacion, contacto, empleados, inventario):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.contacto = contacto
        self.empleados = empleados
        self.inventario = inventario
    
    def presentacion(self):
        print(f"Bienvenidos a {self.nombre}")



# Creacion del objeto de tipo inventario
mi_inventario = inventario()

# Creacion de la tienda en si. 
Mi_Tienda = tienda("TiendaDeEjemplo", "Av. Eusebio Ayala", "+595 (0981) 111-111", ["Maria", "Pedro", "Carlos"], mi_inventario)    


# Creacion de contenidos para el inventario

# Creacion de objetos de tipo ropahombre
kepi = RopaHombre("Kepi", 5000, 7, "M")
remera = RopaHombre("Remera mediana", 7500, 10, "M")
camisa = RopaHombre("Camisa grande", 4000, 5, "G")
pantalon = RopaHombre("Pantalon", 30000, 5, "XL")
champion = RopaHombre("Champion", 25000, 5, 45)

# Creacion de objetos de tipo ropamujer
vestido = RopaMujer("Vestido", 50000, 20, "Blanco")
falda = RopaMujer("Pollera larga", 25000, 15, "Negro")
tacones = RopaMujer("Tacones altos", 70000, 2, "Rojos")
aritos = RopaMujer("Aritos de oro", 120000, 2, "Dorado")
blusa = RopaMujer("Blusa comun", 40000, 50, "Azul Marino")


Mi_Tienda.inventario.agregar_prenda(kepi)
Mi_Tienda.inventario.agregar_prenda(remera)
Mi_Tienda.inventario.agregar_prenda(camisa)
Mi_Tienda.inventario.agregar_prenda(pantalon)
Mi_Tienda.inventario.agregar_prenda(champion)

Mi_Tienda.inventario.agregar_prenda(vestido)
Mi_Tienda.inventario.agregar_prenda(falda)
Mi_Tienda.inventario.agregar_prenda(tacones)
Mi_Tienda.inventario.agregar_prenda(aritos)
Mi_Tienda.inventario.agregar_prenda(blusa)



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
        except: pass
        
        
        
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
            