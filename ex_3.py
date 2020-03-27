n = int(input('Please enter a number from 0 to 9: '))
while (n >= 10) or (n < 0):
    number = int(input('Введите число от 0 до 9: '))
#print(n+(10*n+n)+(10 ** 2 * n+ 10 ** 1 * n + n ))
print(f'{(n+(10 * n+n) + ((10 ** 2) * n+ (10 ** 1) * n + n ))}')