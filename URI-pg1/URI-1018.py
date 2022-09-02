val = int(input())

print(val)
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
print(f"{int(mny/1)} nota(s) de R$ 1,00")