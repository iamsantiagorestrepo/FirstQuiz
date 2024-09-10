# Este programa muestra el nuevo salario para el proximo año

salario_actual = float(input("Introduce el salario mínimo actual: "))

incremento_porcentaje = 4.2

incremento = salario_actual * (incremento_porcentaje / 100)

nuevo_salario = salario_actual + incremento

print("El nuevo salario mínimo para el próximo año es:", nuevo_salario)