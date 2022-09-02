code , quantity = map(int , input().split(" "))
res = 0

if code == 1:
    res = quantity * 4.00
elif code == 2:
    res = quantity * 4.50
elif code == 3:
    res = quantity * 5.00
elif code == 4:
    res = quantity * 2.00
elif code == 5:
    res = quantity * 1.50

print(f"Total: R$ {res:0.2f}")