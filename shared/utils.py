def enter_a_valid_number(message):
    while True:
        num = input(message)
        try:
            num = int(num)
            break
        except:
            print('\t>>>> Enter a valid number')
    return num


def enter_a_valid_number_or_default(message):
    while True:
        num = input(f'{message}(press Enter for choosing default value) ')
        try:
            if num == '':
                return 'default'
            num = int(num)
            break
        except:
            print('\t>>>> Enter a valid number')
    return num
