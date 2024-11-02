class tienda:
    def __init__(self, nombre, ubicacion, contacto, empleados, inventario):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.contacto = contacto
        self.empleados = empleados
        self.inventario = inventario
    
    def presentacion(self):
        print(f"Bienvenidos a {self.nombre}")

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
    

class producto: # encapsulacion y abstraccion en las clases
    def __init__(self, nombre, precio, cantidad):
        self.id = inventario.ultimo
        inventario.ultimo += 1
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    def mostrar_info(self):
        print(f"\nID: {self.id}. \nNombre: {self.nombre}. \nPrecio: {self.precio}. \nCantidad: {self.cantidad}")

class Ropa(producto): # Herencia
    def __init__(self, nombre, precio, cantidad, talle, color): #Polimorfismo
        super().__init__(nombre, precio, cantidad)
        self.talle = talle
        self.color = color
        
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talle: {self.talle}.")
        print(f"Color: {self.color}.")
        
        
class sombrero(Ropa): # Herencia
    def __init__(self, nombre, precio, cantidad, talle, color, forma): #Polimorfismo
        super().__init__(nombre, precio, cantidad, talle, color)
        self.forma = forma
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Forma: {self.forma}.")

class pantalon(Ropa):
    def __init__(self, nombre, precio, cantidad, talle, color, TipoDeTela): #Polimorfismo
        super().__init__(nombre, precio, cantidad, talle, color)
        self.TipoDeTela = TipoDeTela
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de tela: {self.TipoDeTela}.")

class camisa(Ropa):
    def __init__(self, nombre, precio, cantidad, talle, color, cantidadbotones): #Polimorfismo
        super().__init__(nombre, precio, cantidad, talle, color)
        self.cantidadbotones = cantidadbotones
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cantidad de botones: {self.cantidadbotones}.")

class zapato(Ropa):
    def __init__(self, nombre, precio, cantidad, talle, color, tacon): #Polimorfismo
        super().__init__(nombre, precio, cantidad, talle, color)
        self.tacon = tacon
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Es tacon (Si o no): {self.tacon}.")

class vestido(Ropa):
    def __init__(self, nombre, precio, cantidad, talle, color, corte): #Polimorfismo
        super().__init__(nombre, precio, cantidad, talle, color)
        self.corte = corte
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Corte de tipo: {self.corte}.")

class blusa(Ropa):
    def __init__(self, nombre, precio, cantidad, talle, color, estilo): #Polimorfismo
        super().__init__(nombre, precio, cantidad, talle, color)
        self.estilo = estilo
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Estilo: {self.estilo}.")



# Creacion del inventario
mi_inventario = inventario()

# Creacion de la tienda en si. 
Mi_Tienda = tienda("TiendaDeEjemplo", "Av. Eusebio Ayala", "+595 (0981) 111-111", ["Maria", "Pedro", "Carlos"], mi_inventario)    


# Creacion de contenidos para el inventario

# Creacion de objetos de tipo Ropa
kepi = sombrero("Kepi", 5000, 7, "M", "blanco", "Cono truncado")
camisa = camisa("Camisa grande", 4000, 5, "G", "Beige", 5)
pantalon = pantalon("Pantalon", 30000, 5, "XL", "Negro", "Tela Jean")
champion = zapato("Champion", 25000, 5, 45, ["Blanco", "Negro", "Rojo"], "No")

vestido = vestido("Vestido", 50000, 20, "G", "Blanco", "Corte Bustier")
falda = Ropa("Pollera larga", 25000, 15, "M", "Negro")
blusa = blusa("Blusa comun", 40000, 50, "P", "Azul Marino", "Veraniego")
tacones = zapato("Tacones altos", 70000, 2, 31, "Rojos", "Si")


Mi_Tienda.inventario.agregar_prenda(kepi)
Mi_Tienda.inventario.agregar_prenda(camisa)
Mi_Tienda.inventario.agregar_prenda(pantalon)
Mi_Tienda.inventario.agregar_prenda(champion)

Mi_Tienda.inventario.agregar_prenda(vestido)
Mi_Tienda.inventario.agregar_prenda(falda)
Mi_Tienda.inventario.agregar_prenda(blusa)
Mi_Tienda.inventario.agregar_prenda(tacones)

if __name__ == "__main__":
    print("Si esto se imprimio, el modulo se ejecuto correctamente.")
