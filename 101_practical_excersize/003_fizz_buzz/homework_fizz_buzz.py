'''
0-100
Если число делится на 3 без остатка - написать Fizz
Если число делится на 5 без остатка - написать Buzz
Если число делится на 3 и на 5 без остатка - написать FizzBuzz
'''

for number in range(0, 101):
    if number % 5 == 0 and number % 3 == 0:
        print(f'Fizz {number}')
    elif number % 3 == 0:
        print(number, 'Fizz')
    elif number % 5 ==0:
        print(number, 'Buzz')
