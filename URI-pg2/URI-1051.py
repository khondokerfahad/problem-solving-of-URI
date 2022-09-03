salary = float(input())

if 0.00<=salary and salary<=2000.00:
    print("Isento")
elif 2000.01<=salary and salary<=3000.00:
    res = salary-2000
    print(f"R$ {(res*0.08):.2f}")
elif 3000.01<=salary and salary<=4500.00:
    res = salary-3000
    print(f"R$ {((res*0.18)+(1000*0.08)):.2f}")
elif salary>4500.00:
    res = salary-4500
    print(f"R$ {((res*0.28)+(1500*0.18)+(1000*0.08)):.2f}")