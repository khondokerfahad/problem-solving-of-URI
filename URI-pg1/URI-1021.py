val = float(input())
point = (val - int(val))*100

print("NOTAS:")
print(f"{int(val/100)} nota(s) de R$ 100,00")
mny = val%100
print(f"{int(mny/50)} nota(s) de R$ 50,00")
mny = mny%50
print(f"{int(mny/20)} nota(s) de R$ 20,00")
mny = mny%20
print(f"{int(mny/10)} nota(s) de R$ 10,00")
mny = mny%10
print(f"{int(mny/5)} nota(s) de R$ 5,00")
mny = mny%5        
print(f"{int(mny/2)} nota(s) de R$ 2,00")
mny = mny%2

print("MOEDAS:")
print(f"{int(mny/1)} nota(s) de R$ 1,00")
mny%=1
print(f"{int(point/50)} de R$ 0.50")
point%=50
print(f"{int(point/25)} de R$ 0.25")
point%=25
print(f"{int(point/10)} de R$ 0.10")
point%=10
print(f"{int(point/5)} de R$ 0.05")
point%=5
print(f"{int(point/1)} de R$ 0.01")


