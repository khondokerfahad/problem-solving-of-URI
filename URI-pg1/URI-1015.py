import math
#input = list(map(float , input().split(" ")))

x1 , y1 = list(map(float , input().split(" ")))
x2 , y2 = list(map(float , input().split(" ")))

res = ((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))

dis = math.sqrt(res)

print(f"{dis:.4f}")