def odds (number):
    if number == 0:
        result = 'Error'
    elif number % 2 > 0:
        result = 'odd'
    else:
        result = 'even'
    return result




if __name__ == '__main__':
    user_number = int (input('Enter a number: '))
    print (f'This number is {odds(user_number)}')
    odds (user_number)
