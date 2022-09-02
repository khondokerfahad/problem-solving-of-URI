import math
input = map(float, input().split(" "))

a , b , c = input

d = (b*b) - 4*a*c

if(d < 0 or a == 0.0):
    print("Impossivel calcular")
else:
    d = math.sqrt(d)
    cal1 = ((-b)+d) / (2*a)
    cal2 = ((-b)-d) / (2*a)
    print(f"R1 = {cal1:.5f}\nR2 = {cal2:.5f}")