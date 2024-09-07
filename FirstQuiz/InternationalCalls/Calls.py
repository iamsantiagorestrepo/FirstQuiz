##Programa que calcula el costo total de una llamada##

destino = input("Ingresa el destino de la llamada:")
duracion = float(input("Ingrese la duracion en minutos de la llamada:"))

if destino == "Estados Unidos":
    costo_por_minuto = 900
elif destino == "Canadá":
    costo_por_minuto = 800
elif destino == "Europa":
    costo_por_minuto = 950
elif destino == "Resto del mundo":
    costo_por_minuto = 1250
else:
    print("Destino no válido. Por favor, elige uno de los destinos listados.")

if costo_por_minuto > 0:
            costo_total = costo_por_minuto * duracion

if duracion > 15:
    costo_total *= 0.80

print (f"El costo total de la llamada es: {costo_total}")