from Nodizador import Nodizador


def main():
    listaSeguimiento = ['S', 'S', 'a', 'S', 'A', 'A', 'a', 'A', 'A', 'A', 'b', 'A', 'B', 'B', 'λ']
    listaSeguimiento2 = ['S', 'S', 'L', 'S', 'R', 'L', 'ab', 'R', 'cd']
    listaSeguimiento3 = ['S', 'S', 'a', 'S', 'B', 'B', 'b', 'B', "B'", "B'", 'S', 'S', 'a', 'S', 'B', 'B', 'b', 'B', "B'", "B'", 'λ']
    listaSeguimiento4 = ['S', 'S', 'a', 'S', 'B', 'B', 'b', 'B', "B'", "B'" , 'λ']
    nodizador = Nodizador(listaSeguimiento4)
    nodizador.mostrarNodos()
    nodizador.mostrarArbol()


if __name__ == "__main__":
    main()


