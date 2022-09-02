time = int(input())

sec = time%60

time = int(time/60)

min = int(time%60)

time = int(time/60)

hr = int(time%60)

print(f"{hr}:{min}:{sec}")