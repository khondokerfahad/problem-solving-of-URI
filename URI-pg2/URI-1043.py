a,b,c = map(float,input().split())

if (a+b)>c and (a+c)>b and (b+c)>a:
    perimeter = (a+b+c)
    print(f"Perimetro = {perimeter:0.1f}")
else:
    area = 0.5*(a+b)*c
    print(f"Area = {area:0.1f}")