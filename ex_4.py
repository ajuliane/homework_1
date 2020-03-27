max=0
n = int(input('Please enter a number: '))
while  (n >0):
    if (n % 10) > max:
        max = n % 10
    n=n // 10
print(f'max is {max}')