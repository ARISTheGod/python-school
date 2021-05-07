def bubble(array):
    N=len(array)
    for i in range(1,N,1):
        for j in range(N-1,i-1,-1):
            if array[j]>array[j-1]:
                tax=True
                continue
            else:
                tax=False
                break
        if tax==False:
            break
          
#                array[j],array[j-1]=array[j-1],array[j]
    return tax
#_______________________________________________
lista=[5,8,9,10,11]
taxinomisi=bubble(lista)
if taxinomisi==True:
    print('Η ΛΙΣΤΑ ΕΙΝΑΙ ΣΕ ΑΥΞΟΥΣΑ ΣΕΙΡΣ')
else:
    print('Η ΛΙΣΤΑ ΔΕΝ ΕΙΝΑΙ ΣΕ ΑΥΞΟΥΣΑ ΣΕΙΡΑ')
