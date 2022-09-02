input = input().split(" ")

a , b , c , d = input

if( (b>c) and (d>a) and ((c+d)>(a+b)) and c>0 and d>0 ):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")