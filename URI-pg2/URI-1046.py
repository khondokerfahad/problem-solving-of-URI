a , b  = map(int , input().split())

if b>a:
    time = b-a
else:
    time = b+24-a

print(f"O JOGO DUROU {time} HORA(S)")