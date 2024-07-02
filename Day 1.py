'''
a = input('Введите число')
b = input('Введите число')
c = input('Введите число')
s = a+b+c
print (s)
'''
'''
a = int(input('Введите число:'))
if a%2==0:
    print('Even number')
else:
    print('Odd number')
'''
'''
a = int(input('Введите число:'))
if a%7==0:
    print('Number is multiple 7')
else:
    print('Number is not multiple 7')
'''
'''
a = int(input('Введите число:'))
b = int(input('Введите число:'))
choose = input('Выведите операцию:1=сумма, 2=произведение, 3=деление, 4=среднеарифметическое')
if choose=='1':
    print ('Сумма чисел: ', a+b)
if choose=='2':
    print('Произведение чисел:', a*b)
if choose=='3':
    print('Деление чисел:', a/b)
if choose=='4':
    print('Среднеарифметическое чисел:', (a+b)/2)
'''
'''
a = int(input('Введите число:'))
b = int(input('Введите число:'))
while a<=b:
    if a%2==1:
        print('Нечетное число:', a)
    a+=1
'''
a = int(input('Введите число:'))
b = int(input('Введите число:'))
c = 0
'''
while a<=b:
    if a%7==0:
        print('Число кратно 7', a)
while a<=b:
    print('Убывающей порядок:', b)
    a-=1
'''
while a<=b:
    if a%5==0:    
        c+=1
    a+=1
print('Количество чисел кратным 5', c)
    
       
        