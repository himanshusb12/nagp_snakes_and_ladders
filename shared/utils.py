def enter_a_valid_number(message):
    """
    Prompts user to provide a valid positive integer.

    Parameters
    ----------
    message: str
        Message to be shown to the user

    Returns
    -------
    int
    """
    while True:
        num = input(message)
        try:
            num = int(num)
            if num < 0:
                print('\t>>>> Enter a positive integer')
                continue
            break
        except Exception:
            print('\t>>>> Enter a valid number')
    return num


def enter_a_valid_number_or_default(message):
    """
    Prompts user to provide a valid non zero positive integer or it's default value.

    Parameters
    ----------
    message: str
        Message to be shown to the user

    Returns
    -------
    int, str
    """
    while True:
        num = input(f'{message}(press Enter for choosing default value) ')
        try:
            if num == '':
                return 'default'
            num = int(num)
            if num < 1:
                print('\t>>>> Enter a positive non zero integer')
                continue
            break
        except Exception:
            print('\t>>>> Enter a valid number')
    return num
