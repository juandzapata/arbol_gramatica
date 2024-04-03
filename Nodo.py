class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.padre: Nodo
        self.hijos: Nodo = []
    
    def agregar_hijo(self, nodo):
        self.hijos.append(nodo)
        nodo.padre = self
    