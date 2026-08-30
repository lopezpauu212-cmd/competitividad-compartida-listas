class RutaTuristica:
    def __init__(self, codigo, nombre, enfoque, duracion):
        self.codigo = codigo
        self.nombre = nombre
        self.enfoque = enfoque
        self.duracion = duracion

    def __str__(self):
        return f"[{self.codigo}] {self.nombre} - {self.enfoque} - {self.duracion}"


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo

    def mostrar(self):
        actual = self.cabeza
        if actual is None:
            print("No hay rutas turisticas registradas todavia")
            return
        print("Rutas turisticas registradas:")
        while actual is not None:
            print("-", actual.dato)
            actual = actual.siguiente


lista_rutas = ListaDoble()

lista_rutas.insertar(RutaTuristica("RT01", "Ruta del Rio Bogota", "Ecoturismo", "1 dia"))
lista_rutas.insertar(RutaTuristica("RT02", "Ruta Cultural Gualiva", "Cultural", "2 dias"))
lista_rutas.insertar(RutaTuristica("RT03", "Ruta Sabana Centro", "Agroturismo", "1 dia"))

lista_rutas.mostrar()
