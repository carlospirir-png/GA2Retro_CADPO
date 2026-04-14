#CADPO
#Retroalimentacion GA2

peso = input("¿CUal es tu peso en kg? ")
estatura = input("Cual es tu estatura en metros?")
imc = round(float(peso)/float(estatura)**2,2)
print("Tu indice de masa corporal es"+ str(imc))