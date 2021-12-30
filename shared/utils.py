def enter_a_valid_number(message):
    while True:
        num = input(message)
        try:
            num = int(num)
            break
        except:
            print('\t>>>> Enter a valid number')
    return num