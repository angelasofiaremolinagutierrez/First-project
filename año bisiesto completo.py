#probar con los valores de: 1, 5, 500, 800, 1204,1900, 1999, 2000, 2016, 2019
year = input("Ingrese el año: ")
year_number = float(year)
year_in_4 = year_number/4
n_int = int(year_in_4)
n_float = float(year_in_4)
substraction = n_float - n_int
if substraction == 0 :
    if year_number % 100 == 0:
        if year_number % 400 == 0:
            print("Año bisiesto&quot")
        else:
            print("Año de 365 días")
    else:
        print ("Año bisiesto")
else:
    print ("Año de 365 días&quot")