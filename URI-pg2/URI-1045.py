a,b,c = map(float,input().split())

list = [a,b,c]

list.sort()

if(list[0]>=(list[1]+list[2])):
    print("NAO FORMA TRIANGULO")
elif(list[0]*list[0] == (list[1]*list[1]+list[2]*list[2])):
     print("TRIANGULO RETANGULO")
elif(list[0] * list[0] > (list[1]*list[1]+list[2]*list[2])):
    print("TRIANGULO OBTUSANGULO")
elif(list[0] * list[0] < (list[1]*list[1]+list[2]*list[2])):
    print("TRIANGULO ACUTANGULO")
if(list[0] == list[1] and list[1] == list[2]):
        print("TRIANGULO EQUILATERO")
elif(list[0] == list[1] or list[1] == list[2]):
        print("TRIANGULO ISOSCELES")