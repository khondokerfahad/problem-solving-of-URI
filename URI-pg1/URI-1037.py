a = float(input())

if 0<=a and a<25:
    print("Intervalo [0,25]")
elif 25<=a and a<50:
    print("Intervalo (25,50]")
elif 50<=a and a<75:
    print("Intervalo (50,75]")
elif 75<=a and a<=100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")