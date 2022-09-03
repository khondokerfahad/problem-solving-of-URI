employee_salary = float(input())

if 0<=employee_salary and employee_salary<=400.01:
    res = (employee_salary*15)/100
    percent = 15
    total = employee_salary+res
elif 400.01<=employee_salary and employee_salary<=800.00:
    res = (employee_salary*12)/100
    percent = 12
    total = employee_salary+res
elif 800.01<=employee_salary and employee_salary<=1200.00:
    res = (employee_salary*10)/100
    percent = 10
    total = employee_salary+res
elif 1200.01<=employee_salary and employee_salary<=2000.00:
    res = (employee_salary*7)/100
    percent = 7
    total = employee_salary+res
elif employee_salary>2000.00:
    res = (employee_salary*4)/100
    percent = 4
    total = employee_salary+res

print(f"Novo salario: {total:0.2f}\nReajuste ganho: {res:0.2f}\nEm percentual: {percent} %")