days = int(input())

year = int(days/365)

days %= 365

month = int(days/30)

days %= 30

print(f"{year} ano(s)\n{month} mes(s)\n{days} dia(s)")