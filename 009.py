# BY ARIS ΒΑΘΜΟΛΟΓΙΑ ΤΟΥ ΜΑΘΗΤΗ
athroisma   = 0
lista=[0,0,0,0,0,0] # POSA ATOMA

for i in range(0,(len(lista))):
    lista[i]  = int(input("ΔΩΣΕ ΤΗΝ ΒΑΘΜΟΛΟΓΙΑ ΤΟΥ "  "ου ΜΑΘΗΤΗ:"))
    athroisma = athroisma + lista[i]
    print(i)

lista.sort()
print("Ο ΜΙΚΡΟΤΕΡΟΣ ΒΑΘΜΟΣ ΕΙΝΑΙ :", (lista[0]))
print("Ο ΜΕΓΑΛΥΤΕΡΟΣ ΒΑΘΜΟΣ ΕΙΝΑΙ :", (lista[(len(lista)-1)]))
print("Ο ΜΕΣΟΣ ΟΡΟΣ ΒΑΘΜΟΛΟΓΙΑΣ ΕΙΝΑΙ :", (athroisma / len(lista)))
