import os

def limpiar_pantalla():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

class Propiedad:
    def __init__(self, barrio, precio, tipo, ambientes, banos):
        self.barrio = barrio
        self.precio = precio
        self.tipo = tipo
        self.ambientes = ambientes
        self.banos = banos
    
    def mostrarPropiedad(self):
        raise NotImplementedError("Se implementa en las subclases")

class PropiedadEnVenta(Propiedad):
    def __init__(self, barrio, precio, tipo, ambientes, banos, cuotas, estado, entrega, anticipo):
        super().__init__(barrio, precio, tipo, ambientes, banos)
        self.cuotas = cuotas
        self.estado = estado
        self.entrega = entrega
        self.anticipo = anticipo
        self.__comision = 0.15

    def mostrarPropiedad(self):
        print(f"{self.tipo.title()} en venta en el hermoso barrio de {self.barrio} en {int(self.precio * (1 + self.__comision))} ARS. Cuenta con: \n")
        if self.ambientes > 1:
            print(f"{self.ambientes} ambientes")
        else:
            print(f"{self.ambientes} ambiente")
        print(f"Cantidad de baños: {self.banos}")
        print(f"Estado: {self.estado}")
        print("\nLos requisitos para la venta son: \n")
        print(f"Se puede financiar hasta en {self.cuotas} cuotas con un anticipo del {self.anticipo}")
        print(f"Entrega: {self.entrega}")
        print("-------------------------\n")

class PropiedadEnAlquiler(Propiedad):
    def __init__(self, barrio, precio, tipo, ambientes, banos, mascotasPermitidas, garantia, seguro, expensas, aumentos):
        super().__init__(barrio, precio, tipo, ambientes, banos)
        self.mascotasPermitidas = mascotasPermitidas
        self.garantia = garantia
        self.seguro = seguro
        self.expensas = expensas
        self.aumentos = aumentos
        self.__comision = 0.10

    def mostrarPropiedad(self):
        print(f"{self.tipo.title()} en alquiler en el hermoso barrio de {self.barrio} en {int(self.precio * (1 + self.__comision))} ARS. Cuenta con: \n")
        if self.ambientes > 1:
            print(f"{self.ambientes} ambientes")
        else:
            print(f"{self.ambientes} ambiente")
        print(f"Cantidad de baños: {self.banos}")
        print(f"Mascotas permitidas: {self.mascotasPermitidas}")
        print("\nLos requisitos del contrato son: \n")
        print("Garantía propietaria:", self.garantia)
        print("Seguro:", self.seguro)
        print("Expensas:", self.expensas)
        print("Aumentos:", self.aumentos)
        print("-------------------------\n")

def mostrarPropiedad(tipoPropiedad, ambientes, operacion):
    if tipoPropiedad == "1" or tipoPropiedad.lower() == "casa":
        tipoPropiedad = "casa"
    else:
        tipoPropiedad = "departamento"
    
    resultados = []
    
    if operacion == "alquiler":
        for propiedad in listadoEnAlquiler:
            if propiedad.tipo.lower() == tipoPropiedad.lower() and propiedad.ambientes == int(ambientes):
                resultados.append(propiedad)
        
        if resultados:
            print("** Propiedades encontradas:** \n")
            for propiedad in resultados:
                propiedad.mostrarPropiedad()
        else:
            print("No se encontraron propiedades que coincidan con los criterios de búsqueda.")
            print("-------------------------\n")
        menuContinuar()
    else: 
        for propiedad in listadoEnVenta:
            if propiedad.tipo.lower() == tipoPropiedad.lower() and propiedad.ambientes == int(ambientes):
                resultados.append(propiedad)
        
        if resultados:
            print("** Propiedades encontradas:** \n")
            for propiedad in resultados:
                propiedad.mostrarPropiedad()
        else:
            print("No se encontraron propiedades que coincidan con los criterios de búsqueda.")
            print("-------------------------\n")
        menuContinuar()

def menu():
    print("1- Consultar propiedades en venta")
    print("2- Consultar propiedades en alquiler")
    print("3- Agregar propiedad")
    print("4- Salir \n")
    
def menuAlquiler():
    print("¿Qué tipo de propiedad estás buscando? \n")
    print("1- Casa")
    print("2- Departamento \n")
    tipoPropiedad = input()
    print("¿Cuántos ambientes estás buscando? Ingrese un número: \n")
    ambientes = input()
    operacion = "alquiler"
    mostrarPropiedad(tipoPropiedad, ambientes, operacion)
    limpiar_pantalla()
     
def menuCompra():
    print("¿Qué tipo de propiedad estás buscando? \n")
    print("1- Casa")
    print("2- Departamento \n")
    tipoPropiedad= input()
    print("¿Cuántos ambientes estás buscando? \n")
    ambientes= input()
    operacion = "compra"
    mostrarPropiedad(tipoPropiedad, ambientes, operacion)
    limpiar_pantalla()
    
def cargarPropiedad():
    print("¿Qué tipo de operación es? \n")
    print("1- Alquiler")
    print("2- Venta \n")
    operacion = input("Ingrese el número correspondiente a la operación: ")

    if operacion == "1":
        nuevaPropiedad = PropiedadEnAlquiler(
            input("Ingrese el barrio: \n"),
            int(input("Ingrese el precio: \n")),
            input("Ingrese si es casa o departamento: \n"),
            int(input("Cantidad de ambientes: \n")),
            int(input("Cantidad de baños: \n")),
            input("¿Acepta mascotas?: \n"),
            input("Ingrese la garantía que acepta: \n"),
            input("Ingrese el seguro que acepta: \n"),
            int(input("Indique el valor de las expensas actuales: \n")),
            input("¿Cada cuanto realizará los aumentos? \n")
        )
        listadoEnAlquiler.append(nuevaPropiedad)
    else:
        nuevaPropiedad = PropiedadEnVenta(
            input("Ingrese el barrio: \n"),
            int(input("Ingrese el precio: \n")),
            input("Ingrese si es casa o departamento: \n"),
            int(input("Cantidad de ambientes: \n")),
            int(input("Cantidad de baños: \n")),
            int(input("Cantidad de cuotas: \n")),
            input("¿En qué estado se encuentra la propiedad? \n"),
            input("Fecha de entrega: \n"),
            input("Indique el porcentaje del anticipo: \n")
        )
        listadoEnVenta.append(nuevaPropiedad)
        
    menuContinuar()

def menuContinuar():
    continuar = input("¿Deseas realizar otra operación? Escribe si/no \n")
    if continuar.lower() == "si":
        menu()
    else:
        print("Gracias por visitarnos :)")
        exit()

def main(): 
    i=0
    while i==0:
        print("Bienvenido al portal inmobiliario Netprop \n")
        menu()
        opcion = input("¿Qué tipo de operación desea realizar? \n")
        if opcion == "1": 
            menuCompra()
        elif opcion == "2":
            menuAlquiler()
        elif opcion == "3":
            cargarPropiedad()
        elif opcion == "4":
            print("Gracias por tu visita.")
            exit()
        else: 
            print("Por favor, elegí una opción válida.")

listadoEnVenta = [
    PropiedadEnVenta("Caballito", 90000, "casa", 2, 1, 24, "a estrenar", "inmediata", "30%"),
    PropiedadEnVenta("Caballito", 150000, "departamento", 3, 1, 12, "usada", "inmediata", "20%"),
    PropiedadEnVenta("Villa Crespo", 100000, "casa", 2, 1, 36, "a estrenar", "6 meses", "35%"),
    PropiedadEnVenta("Villa Crespo", 120000, "departamento", 2, 1, 18, "usada", "inmediata", "30%"),
    PropiedadEnVenta("Palermo", 300000, "casa", 4, 3, 24, "a estrenar", "Noviembre 2025", "40%")
]
listadoEnAlquiler = [
    PropiedadEnAlquiler("Caballito", 200000, "casa", 2, 1, "si", "garantía propietaria", "seguro de caución", 20000, "Trimestral"),
    PropiedadEnAlquiler("Caballito", 220000, "departamento", 2, 1, "no", "garantía bancaria", "seguro de caución", 15000, "Trimestral"),
    PropiedadEnAlquiler("Villa Crespo", 240000, "casa", 3, 1, "si", "garantía propietaria", "seguro de caución", 45000, "Anual"),
    PropiedadEnAlquiler("Palermo", 320000, "departamento", 1, 1, "no", "garantía bancaria", "seguro de caución", 70000, "Anual"),
    PropiedadEnAlquiler("Palermo", 450000, "departamento", 3, 2, "si", "garantía propietaria", "seguro de caución", 50000, "Semestral")
]

main()
