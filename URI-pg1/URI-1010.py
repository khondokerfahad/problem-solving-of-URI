product1_input = input().split(" ")
product2_input = input().split(" ")

product1_code, product1_unit, product1_price = product1_input

product2_code, product2_unit, product2_price = product2_input

res = (int(product1_unit)*float(product1_price)) + (int(product2_unit)*float(product2_price))

print(f"VALO A PAGAR: R$ {res:.2f}")