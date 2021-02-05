kil_palia=int(input('ΠΟΣΑ ΧΙΛΙΟΜΕΤΡΑ ΕΙΧΕΣ ΣΤΟ ΠΡΟΗΓΟΥΜΕΝΟ SERVICE?'))
kil_nea=int(input('ΠΟΣΑ ΧΙΛΙΟΜΕΤΡΑ ΕΧΕΙΣ ΤΩΡΑ?'))
kil=kil_nea-kil_palia
if kil>15000:
    print()
    print('ΤΟ ΑΥΤΟΚΙΝΗΤΟ ΣΟΥ ΧΡΕΙΑΖΕΤΑΙ SERVICE...')
else:
    ypol=15000-kil
    print()
    print('ΜΠΟΡΕΙΣ ΝΑ ΚΑΝΕΙΣ ',ypol,' ΧΙΛ/ΤΡΑ ΜΕΧΡΙ ΤΟ ΕΠΟΜΕΝΟ SERVICE')
