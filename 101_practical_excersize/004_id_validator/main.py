# Main function for entering ID
def enter_id():
    condition = True
    while condition:
        try:
            user_id = input('Please enter ID: ')
            int(user_id)
            if len(user_id) != 11:
                raise UserWarning
        except UserWarning:
            if len(user_id) < 11:
                print('Code is too short')
            elif len(user_id) > 11:
                print('Code is too long')
        except:
            print('Code you entered is not numeric')
        else:
            condition = False
            user_menu(user_id)


# Let user choose what to do
def user_menu(idcode):
    user_choice = input('Please choose:\n1.Get data by ID code\n2.Check if ID is valid\n3.Change ID\n4.Exit\n-->')
    if user_choice == '1':
        # Create variables for each type of data from ID
        gender_num = idcode[0]
        by_num = idcode[1:3]
        bm_num = idcode[3:5]
        bd_num = idcode[5:7]
        birth_region = idcode[7:10]
        chk_num = idcode[10]

        # Get gender and birth century
        if gender_num == '1':
            cent_id = '18'
            gend_id = 'Male'
        elif gender_num == '2':
            cent_id = '18'
            gend_id = 'Female'
        elif gender_num == '3':
            cent_id = '19'
            gend_id = 'Male'
        elif gender_num == '4':
            cent_id = '19'
            gend_id = 'Female'
        elif gender_num == '5':
            cent_id = '20'
            gend_id = 'Male'
        elif gender_num == '6':
            cent_id = '20'
            gend_id = 'Female'

        # IF statement to check region of birth
        if int(birth_region) in range(1, 11):
            region = 'Kuressaare haigla'
        elif int(birth_region) in range(11, 20):
            region = 'Tartu Ülikooli Naistekliinik'
        elif int(birth_region) in range(21, 151):
            region = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
        elif int(birth_region) in range(151, 161):
            region = 'Keila haigla'
        elif int(birth_region) in range(161, 221):
            region = 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
        elif int(birth_region) in range(221, 271):
            region = 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
        elif int(birth_region) in range(271, 371):
            region = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
        elif int(birth_region) in range(371, 421):
            region = 'Narva haigla'
        elif int(birth_region) in range(421, 471):
            region = 'Pärnu haigla'
        elif int(birth_region) in range(471, 491):
            region = 'Haapsalu haigla'
        elif int(birth_region) in range(491, 521):
            region = 'Järvamaa haigla (Paide)'
        elif int(birth_region) in range(521, 571):
            region = 'Rakvere haigla, Tapa haigla'
        elif int(birth_region) in range(571, 601):
            region = 'Valga haigla'
        elif int(birth_region) in range(601, 651):
            region = 'Viljandi haigla'
        elif int(birth_region) in range(651, 701):
            region = 'Lõuna-Eesti haigla (Võru), Põlva haigla'
        else:
            region = 'Unknown'

        # Print results
        print('\n')
        print('ID: ' + idcode)
        print('Gender: ' + gend_id)
        print('Date of birth: ' + bd_num + '.' + bm_num + '.' + cent_id + by_num)
        print('Region: ' + region)
        print('ID check number: ' + chk_num + '\n')

        # Return to user menu
        user_menu(idcode)


    elif user_choice == '2':
        id_validator(idcode)

    elif user_choice == '3':
        enter_id()

    elif user_choice == '4':
        print('Good bye.')
        quit()
    else:
        print('Choice out of range')
        user_menu(idcode)


# Function to print data collected from ID
def get_data_by_id(idcode):

    # Create variables for each type of data from ID
    gender_num = idcode[0]
    by_num = idcode[1:3]
    bm_num = idcode[3:5]
    bd_num = idcode[5:7]
    birth_region = idcode[7:10]
    chk_num = idcode[10]

    # Get gender and birth century
    if gender_num == '1':
        cent_id = '18'
        gend_id = 'Male'
    elif gender_num == '2':
        cent_id = '18'
        gend_id = 'Female'
    elif gender_num == '3':
        cent_id = '19'
        gend_id = 'Male'
    elif gender_num == '4':
        cent_id = '19'
        gend_id = 'Female'
    elif gender_num == '5':
        cent_id = '20'
        gend_id = 'Male'
    elif gender_num == '6':
        cent_id = '20'
        gend_id = 'Female'

    # IF statement to check region of birth
    if int(birth_region) in range(1, 11):
        region = 'Kuressaare haigla'
    elif int(birth_region) in range(11, 20):
        region = 'Tartu Ülikooli Naistekliinik'
    elif int(birth_region) in range(21, 151):
        region = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
    elif int(birth_region) in range(151, 161):
        region = 'Keila haigla'
    elif int(birth_region) in range(161, 221):
        region = 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
    elif int(birth_region) in range(221, 271):
        region = 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
    elif int(birth_region) in range(271, 371):
        region = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
    elif int(birth_region) in range(371, 421):
        region = 'Narva haigla'
    elif int(birth_region) in range(421, 471):
        region = 'Pärnu haigla'
    elif int(birth_region) in range(471, 491):
        region = 'Haapsalu haigla'
    elif int(birth_region) in range(491, 521):
        region = 'Järvamaa haigla (Paide)'
    elif int(birth_region) in range(521, 571):
        region = 'Rakvere haigla, Tapa haigla'
    elif int(birth_region) in range(571, 601):
        region = 'Valga haigla'
    elif int(birth_region) in range(601, 651):
        region = 'Viljandi haigla'
    elif int(birth_region) in range(651, 701):
        region = 'Lõuna-Eesti haigla (Võru), Põlva haigla'
    else:
        region = 'Unknown'

    # Print results
    print('\n')
    print('ID: ' + idcode)
    print('Gender: ' + gend_id)
    print('Date of birth: ' + bd_num + '.' + bm_num + '.' + cent_id + by_num)
    print('Region: ' + region)
    print('ID check number: ' + chk_num + '\n')

    # Return to user menu
    user_menu(idcode)


# Function to validate ID
def id_validator(idcode):
    # Check numbers
    chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

    # For loop to check first row of numbers
    chk_result = 0
    for x in range(0, 10):
        chk_result += int(idcode[x]) * chk1[x]

    # For loop to check second row of numbers if first try failed
    if chk_result % 11 != int(idcode[-1]) and chk_result % 11 == 10:
        chk_result = 0
        for x in range(0, 10):
            chk_result += int(idcode[x]) * chk2[x]

    # Print validation result
    if chk_result % 11 == int(idcode[-1]):
        print('Your ID is valid')
    else:
        print('You ID is NOT valid')
    user_menu(idcode)


enter_id()
