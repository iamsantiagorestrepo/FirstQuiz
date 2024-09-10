#Este programa muestra el promedio del estudiante, su clasificación de rendimiento y el monto final a pagar por la matrícula

nota1 = float(input("Ingresa la primer nota de 1 a 5: "))
nota2 = float(input("Ingresa la segunda nota de 1 a 5: "))
nota3 = float(input("Ingresa la tercer nota de 1 a 5: "))
nota4 = float(input("Ingresa la cuarta nota de 1 a 5: "))

costo_matricula = float(input("Introduce el costo total de la matrícula: "))

promedio = (nota1 + nota2 + nota3 + nota4) / 4

if promedio <= 4:
    descuento = 0.20

costo_final = costo_matricula * 0.80

print(f"Promedio del estudiante: {promedio}")
print(f"Monto final a pagar de matrícula: ${costo_final}")