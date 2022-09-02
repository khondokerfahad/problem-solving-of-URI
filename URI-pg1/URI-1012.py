val_input = list(map(float, input().split(" ")))
a , b , c = val_input

pi = 3.14159
res_triangle = (1/2)*a*c
res_circle = pi*c*c
res_trapezio = (a+b)/2*c
res_quadrado = b*b
res_retangulo = a*b

print(f"TRIANGULO: {res_triangle:.3f}\nCIRCULO: {res_circle:.3f}\nTRAPEZIO: {res_trapezio:.3f}\nQUADRADO: {res_quadrado:.3f}\nRETANGULO: {res_retangulo:.3f}")