#CADPO
#Retroalimentacion

cantidad = float(input("Cantidad a invertir? "))
interes = float(input("Interes porcentual anual? "))
años = int (input("AÑOS?"))
print("Capital Final:" + str(round(cantidad *(interes/100+1)**años,2)))
