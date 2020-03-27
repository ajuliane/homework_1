a = int(input('Please enter revenue: '))
b = int(input('Please enter costs: '))
if a-b>0:
    print(f'Congratulation! You work with profit {a-b}. Your profitability is {(a-b)/a}')
    c = int(input('Please enter number of employees: '))
    print(f'Profitability per employee is {(a-b)/c}')
else:
    print(f'You work with leisen {b - a}.')