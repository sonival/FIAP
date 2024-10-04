#python-m pip install numpy
import random 
import numpy as np

class Cliente:
    def __init__(self, registro, nome, totalClientes):
        self.nome = "Cliente" + str(registro)
        self.demdandas = {i: random.randint(5, 20) for i in range(1,totalClientes+1)}
        self.distancias = {i: random.randint(5, 20) for i in range(1,totalClientes+1)}
        #np.random.randint(10, 100, size=(len(clientes_grande) + 1, len(clientes_grande) + 1))
        self.registro =registro


def main():
    cliente1 = Cliente(1,"Cliente",20)
    print(cliente1.nome)
    print("Demandas: %s" % cliente1.demdandas)

    print("Demandas: %s" % cliente1.distancias)
    for i in cliente1.demdandas:
        print(cliente1.demdandas.get(i))


if __name__ == "__main__":
    main()