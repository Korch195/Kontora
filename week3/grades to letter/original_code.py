OP = float(input())
MA = float(input())
DM = float(input())
T = float(input())
H = float(input())

percent_grade = ((OP + MA + DM + T + H) / 5)

if OP < 0 or OP > 100 or MA < 0 or MA > 100 or DM < 0 or DM > 100 or T < 0 or T > 100 or H < 0 or H > 100: 
    print('None')


elif percent_grade >= 90:
        letter_grade = 'A'
elif percent_grade >= 80:
        letter_grade = 'B'
elif percent_grade >= 75:
        letter_grade = 'C'
elif percent_grade >= 65:
        letter_grade = 'D'
elif percent_grade >= 60:
        letter_grade = 'E'
elif percent_grade >= 0:
        letter_grade = 'F'
else: None

print(f'Average grade = {percent_grade} -> {letter_grade}')