i = 0
a = float(input('Please enter start result: '))
b = float(input('Please enter an aim: '))
while  (a < b):
    print(f'{i+1}-й день: {a:.2f}')
    a = float(a * (1.1))
    i = i + 1
print(f'{i+1}-й день: {a:.2f}')