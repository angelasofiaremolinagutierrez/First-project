n1 = input("Ingrese la primera nota: ")
n2 = input("Segunda nota: ")
n3 = input ("Tercera nota: ")
n4 = input ("Cuarta nota: ")
n5 = input ("Quinta nota: ")

n1_float=float(n1)
n2_float=float(n2)
n3_float=float(n3)
n4_float=float(n4)
n5_float=float(n5)

n1_10 = n1_float*0.1
n2_15 = n2_float*0.15
n3_25 = n3_float*0.25
n4_15 = n4_float*0.15
n5_35 = n5_float*0.35

nota_final = (n1_10) + (n2_15) + (n3_25)+ (n4_15)+ (n5_35)

if nota_final >=3 and nota_final <= 5 :
    if nota_final >= 4.5 :
        print("Felitaciones, aprobó con una nota alta de: "+ str(nota_final))

    else:
        print("Aprobó con:"+ str(nota_final))

else:
    if nota_final < 3 and nota_final > 2:
        print ("Su nota final fue: "+ str(nota_final) + " Reprobó, debe habilitar.")

    else:
        nota_final <= 2 and nota_final >= 0
        print ("Su nota final fue: "+ str(nota_final) + ". Reprobó y no puede habilitar")