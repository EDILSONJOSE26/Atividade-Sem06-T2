def ten(x):   
 if x in"A,E,I,O,U":
    return"vogal"
 elif"B"<=x<="Z":
    return"consoante"
 elif"0"<=x<="99999":
    return"número"
 else:
    return"símbolo"
letra = input("").upper()
letra = ten(letra)
print("{0}".format(letra))




