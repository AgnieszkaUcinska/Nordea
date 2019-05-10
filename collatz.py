def collatz(number):
    print(number)
    if number==1:
        return
    elif number % 2:
        return collatz(number * 3 + 1)
    else:
        return collatz (number // 2)


if __name__== '__main__':
    number=int(input('Give a number: '))
    print (f'Collatz sequence for number {number} is: ')
    collatz(number)


