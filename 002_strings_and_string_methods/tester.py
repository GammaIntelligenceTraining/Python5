id_code = input('Please enter ID: ')
if id_code.isdigit():
    print('All digits')
if len(id_code) == 11 or len(id_code) > 10:
    if id_code[0] != '3' and id_code[0] != '4':
        print(id_code[0])
        print('Your id code is wrong')
    else:
        print('Your ID code is: ' + id_code)
elif len(id_code) > 10:
    print('Your ID is too long')
else:
    print('Your ID is too short')