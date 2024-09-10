#Este programa muestra el promedio del estudiante, su clasificación de rendimiento y el monto final a pagar por la matrícula

nota1 = float(input("Ingresa la primera nota de 1 a 5: "))
nota2 = float(input("Ingresa la segunda nota de 1 a 5: "))
nota3 = float(input("Ingresa la tercera nota de 1 a 5: "))
nota4 = float(input("Ingresa la cuarta nota de 1 a 5: "))

costo_matricula = float(input("Introduce el costo total de la matrícula: "))

promedio = (nota1 + nota2 + nota3 + nota4) / 4


if 4 <= promedio <= 5:
    calificacion = "Excelente"
    descuento = 0.20
elif 3 <= promedio < 4:
    calificacion = "Bien"
    descuento = 0.00
else:
    calificacion = "Deficiente"
    descuento = 0.00


costo_final = costo_matricula * (1 - descuento)


print(f"Promedio del estudiante: {promedio:}")
print(f"Calificación de rendimiento: {calificacion}")
print(f"Monto final a pagar por la matrícula: ${costo_final:}")