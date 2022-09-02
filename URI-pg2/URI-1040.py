a,b,c,d = map(float,input().split())

val = (a*2+b*3+c*4+d*1)/10

print(f"Media: {val:.1f}")

if val>=7.0:
    print("Aluno aprovado.")
elif val<5.0:
    print("Aluno reprovado.")
elif val>=5.0 and val<7.0:
    print("Aluno em exame.")
    exam_case = float(input())
    print(f"Nota do exame: {exam_case:.1f}")
    exam_case = (val+exam_case)/2
    if exam_case>=5.0:
        print("Aluno aprovado.")
        print(f"Media final: {exam_case:.1f}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {exam_case:.1f}")