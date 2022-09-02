seller_name = str(input())
seller_salary = float(input())
total_sale = float(input())

res = seller_salary + ((total_sale*15)/100)

print(f"TOTAL = R$ {res:.2f}")