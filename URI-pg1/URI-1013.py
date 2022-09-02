import math
input = list(map(int, input().split(" ")))

a, b, c = input

mxab = (a+b+abs(a-b))/2

max = (mxab + c + abs(mxab-c))/2

print(f"{int(max)} eh o maior")