# Programa que permite convertir pesos colombianos a dólares.
tasa_cambio = 0.00024

pesos_colombianos = float(input("Introduce la cantidad en pesos colombianos: "))

dolares = pesos_colombianos * tasa_cambio

print(pesos_colombianos, "pesos colombianos son aproximadamente", dolares, "dólares.")