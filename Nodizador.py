from Nodo import Nodo



class Nodizador:
    def __init__(self, datos: list[str]):
        self.datos = datos
        self.nodos: Nodo = []
        self.nodizar()
    
    def nodizar(self):
        del self.datos[0]
        self.nodizarRaiz()
        for i in range(len(self.datos)):
            i *= 2
            if i + 1 >= len(self.datos):
                break
            
            salir = False
            nodoPadre: Nodo = self.buscarNodo(self.datos[i])
            if self.datos[i + 1] == 'λ':
                for nodos in reversed(self.nodos):
                    for hijo in nodos.hijos:
                        if hijo.dato == self.datos[i]:
                            nodoPadre = hijo
                            nodo = Nodo(self.datos[i + 1])
                            nodo.padre = nodoPadre
                            nodoPadre.agregar_hijo(nodo)
                            self.nodos.append(nodo)
                            salir = True
                            break
                    if salir:
                        break
                if salir:
                    break

            if salir:
                break

            if nodoPadre is not None and len(nodoPadre.hijos) < 2:
                nodo = Nodo(self.datos[i + 1])
                nodo.padre = nodoPadre
                nodoPadre.agregar_hijo(nodo)
                self.nodos.append(nodo)
            elif nodoPadre is not None and len(nodoPadre.hijos) == 2:
                nodo: Nodo = Nodo(self.datos[i])
                bandera = False
                for nodoHijo in nodoPadre.hijos:
                    if nodoHijo.dato == nodo.dato:
                        nodo = nodoHijo
                        nodoHijo = Nodo(self.datos[i + 1])
                        nodoHijo.padre = nodo
                        self.nodos.append(nodoHijo)
                        nodo.agregar_hijo(nodoHijo)
                        bandera = True
                        
                
                if not bandera:
                    if nodoPadre.padre is None:
                        nodoPadre = self.buscarComoHijo(nodo)
                        if nodoPadre is not None:
                            for hijo in nodoPadre.hijos:
                                if hijo.dato == nodo.dato:
                                    nodo = hijo

                        nodo.padre = nodoPadre
                        nodoHijo = Nodo(self.datos[i + 1])
                        nodoHijo.padre = nodo
                        self.nodos.append(nodoHijo)
                        nodo.agregar_hijo(nodoHijo)
                    else:
                        for nodo in self.nodos:
                            for hijo in nodo.hijos:
                                if hijo.dato == nodoPadre.dato:
                                    if hijo != nodoPadre:
                                        nodoPadre = hijo
                                        nodoHijo = Nodo(self.datos[i + 1])
                                        nodoHijo.padre = nodoPadre
                                        nodoPadre.agregar_hijo(nodoHijo)
                                        self.nodos.append(nodoHijo)

            else:
                nodoPadre = Nodo(self.datos[i])
                nodoAbuelo = self.buscarComoHijo(nodoPadre)
                if nodoAbuelo is not None:
                    nodoPadre.padre = nodoAbuelo
                else:
                    nodoPadre.padre = nodoPadre
                self.nodos.append(nodoPadre)
                nodo = Nodo(self.datos[i + 1])
                nodo.padre = nodoPadre
                nodoPadre.agregar_hijo(nodo)
                self.nodos.append(nodo)
        
        
    
    def buscarComoHijo(self, nodoBuscado):
        for nodo in self.nodos:
            for hijo in nodo.hijos:
                if hijo.dato == nodoBuscado.dato:
                    return nodo
        return None
                
    def nodizarRaiz(self):
        nodo = Nodo(self.datos[0])
        nodo.padre = None
        self.nodos.append(nodo)

    def buscarNodo(self, dato):
        for nodo in self.nodos:
            if nodo.dato == dato:
                return nodo
        return None

    def mostrarNodos(self):
        for nodo in self.nodos:
            if nodo.padre is None:
                print(f"{nodo.dato} es la raíz")
            if nodo.hijos:
                print(f"{nodo.dato} tiene los siguientes hijos: {', '.join(hijo.dato for hijo in nodo.hijos)}")
            print()
            

    def mostrarArbol(self):
        self.mostrarArbolRecursivo(self.nodos[0])

    def mostrarArbolRecursivo(self, nodo, nivel = 0):
        print(' ' * nivel * 3 + '|--' + nodo.dato)
        if nodo.hijos:
            for hijo in nodo.hijos:
                self.mostrarArbolRecursivo(hijo, nivel + 1)
        