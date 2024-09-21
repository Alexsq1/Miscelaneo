#Se codifica una torre de Hanoi con una lista de pilas


#P0: 123456
#P1: 0
#P2: 0

#Los discos se ordenan de menor a mayor,
#como si fuera cuánto peso




import torre

th = 1
th = torre.Torre(6)

th.printState()
th.solve()
th.printState()


