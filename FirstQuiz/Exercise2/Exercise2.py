#Este programa da el resultado de las siguientes comparaciones
a = 7
b = 3

resultado_a = a != b
resultado_b = a == b
resultado_c = a > b
resultado_d = (a + b) < 2
resultado_e = (a > 7) and (b == 3)
resultado_f = (a < 7) or (b == 3)
resultado_g = (a < 7) or (b != 3)

print(f"a. a != b → {resultado_a}")
print(f"b. a == b → {resultado_b}")
print(f"c. a > b → {resultado_c}")
print(f"d. (a + b) < 2 → {resultado_d}")
print(f"e. (a > 7) and (b == 3) → {resultado_e}")
print(f"f. (a < 7) or (b == 3) → {resultado_f}")
print(f"g. (a < 7) or (b != 3) → {resultado_g}")