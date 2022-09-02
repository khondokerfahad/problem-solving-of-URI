employee_num = int(input())
employee_worktime = int(input())
employee_recieve_amount_perhour = float(input())

res = employee_worktime * employee_recieve_amount_perhour

print(f"NUMBER = {employee_num}\nSALARY = U$ {res:.2f}")