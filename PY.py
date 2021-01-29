while True:
    while True:
        try:
            x=int(input('DOSE TON 1o ARITHMO:'))
        except ValueError:
            continue
        break
    while True:
        try:
            y=int(input('DOSE TON 2o ARITHMO:'))
        except ValueError:
            continue
        break
    print("1.prosthesi")
    print("2.afairesi")
    print("3.ginomeno")
    print("4.piliko")
    print("5.ypoloipo")
    print("6. exodos")
    print("")
    while True:
        try:
            ui = int(input('CHOOSE A NUMMER:'))
        except ValueError:
            continue
        break
    print("")
    if ui == 1:
        prosthesi=x+y
        print("apotelesma: ",prosthesi)
        break
    elif ui == 2:
        afairesi=x-y
        print("apotelesma: ",afairesi)
        break
    elif ui == 3:
        ginomeno=x*y
        print("apotelesma: ",ginomeno)
        break
    elif ui == 4:
        piliko=x/y
        print("apotelesma: ",piliko)
        break
    elif ui == 5:
        ypoloipo=x%y
        print("apotelesma: ",ypoloipo)
        break
    elif ui == 6:
        break
    else:
        continue
