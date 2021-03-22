years   = 0
city_A  = 30000
city_B  = 45000
a_Added = 0
b_Added = 0

while city_A<=city_B:
    years   += 1
    a_Added = (city_A*3)/100
    b_Added = (city_B*1)/100
    city_A  = city_A  +  a_Added
    city_B  = city_B  +  b_Added
    
print("ΠΛΗΘΥΣΜΟΣ ΠΟΛΗΣ A:", city_A)
print("ΠΛΗΘΥΣΜΟΣ ΠΟΛΗΣ B:", city_B)
print("ΤΑ ΧΡΟΝΙΑ ΠΟΥ ΠΕΡΑΣΝ ΕΙΝΑΙ: ", years)
