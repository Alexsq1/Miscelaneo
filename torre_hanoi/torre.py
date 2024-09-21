#from collections import deque
#Implementación de pilas:
#lista con:
    #meter: .append()
    #ver: .peek()
    #sacar: .pop()

class Torre:

    def __init__(self, n):
        self.tamanno = n
        self.l = []
        for i in range(3):
            self.l.append([])

        i = n
        while i > 0:
            self.l[0].append(i)
            i -= 1

    def printState(self):
        print(self.l)

    def moverPieza(self, orig, dest):

        buffer = self.l[orig][-1]

        if len(self.l[dest]) == 0 or buffer < self.l[dest][-1]:
            self.l[dest].append(buffer)
            self.l[orig].pop()

        self.printState()


    def transpaso(self, numPiezas, orig, dest):

        if numPiezas == 1:
            self.moverPieza(orig, dest)

        else:
            otro = restante(orig, dest)
            self.transpaso(numPiezas - 1, orig, otro)

            self.moverPieza(orig, dest)

            self.transpaso(numPiezas - 1, otro, dest)

    def solve(self):
        self.transpaso(self.tamanno, 0, 2)




def restante(a, b):

    l = [0, 1, 2]
    l.remove(a)
    l.remove(b)
    return l[0]