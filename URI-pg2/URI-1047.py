h1 , m1 , h2 , m2 = map(int , input().split())

total_time = ((h2*60)+m2) - ((h1*60)+m1)

if total_time <= 0:
    total_time+=(24*60)

print(f"O JOGO DUROU {total_time//60} HORA(S) E {total_time%60} MINUTO(S)")