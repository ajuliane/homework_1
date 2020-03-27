a = int(input('Please enter the time in seconds: '))
b = a // 3600
#print(b)
c = (a - b * 3600) // 60
#print(c)
d = (a - b * 3600 - c * 60)
#print(d)
#print(b, ':', c, ':', d)
print(f'{b}:{c}:{d}')

