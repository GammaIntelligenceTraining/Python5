def enter_id():
    while True:
        try:
            user_input = input('Please enter your ID: ')
            int(user_input)
            if len(user_input) != 11:
                raise UserWarning
        except ValueError:
            print('Code you entered is not numeric!')
            continue

        except UserWarning:
            if len(user_input) > 11:
                print('Code you entered is too long')
            elif len(user_input) < 11:
                print('Code you enter is too short')
            continue
        else:
            print(f'Your id is {user_input}')
            print(f'Yout id is {len(user_input)} digits long.')
            return main(user_input)


def validate_id(id_code):
    chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

    result = 0
    counter = 0
    for num in chk1:
        result = result + int(id_code[counter]) * num
        counter += 1
    if result % 11 == int(id_code[-1]):
        print(id_code, "Your id code is valid.")
    else:
        result = 0
        counter = 0
        for num in chk2:
            result = result + int(id_code[counter]) * num
            counter += 1
        if result % 11 == int(id_code[-1]):
            print(id_code, "Your id code is valid")
        else:
            print(id_code, "Your id code is NOT valid")


def get_data_by_id(id_code):
    cent_id = id_code[0]
    if cent_id == '1' or cent_id == '2':
        b_cent = '18'
    elif cent_id == '3' or cent_id == '4':
        b_cent = '19'
    elif cent_id == '5' or cent_id == '6':
        b_cent = '20'

    if cent_id == '1' or cent_id == '3' or cent_id == '5':
        gender = 'Male'
    elif cent_id == '2' or cent_id == '4' or cent_id == '6':
        gender = 'Female'

    by = id_code[1:3]
    bm = id_code[3:5]
    bd = id_code[5:7]
    region = int(id_code[7:10])

    if region in range(1, 11):
        birth_place = 'Kuressaare haigla'
    elif region in range(11, 20):
        birth_place = 'Tartu Ülikooli Naistekliinik'

    print(f'Your id is {id_code}')
    print(f'You were born in {bd}.{bm}.{b_cent + by}')



def main(id_code):
    condition = True
    while condition:
        print(id_code)
        user_choice = input('Please choose:\n'
                            '1. Get ID data\n'
                            '2. Validate\n'
                            '3. Change ID\n'
                            '4. Exit\n'
                            '--> ')
        if user_choice == '1':
            get_data_by_id(id_code)
        elif user_choice == '2':
            validate_id(id_code)
        elif user_choice == '3':
            enter_id()
        elif user_choice == '4':
            condition = False
        else:
            print('Choice is out of range.')


enter_id()