def encode(values): # encode function adds 3 to every value given to the program
    encoded_values = ''
    for pos, num in enumerate(values):
        num = int(num) + 3
        num = str(num)
        encoded_values += num

    return encoded_values


def main():
    menu_active = True # creates while loop for options 1 and 2, easily terminated with option 3
    while menu_active:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print('')
        user_choice = int(input('Please enter an option: '))
        if user_choice == 1:
            values = input('Please enter your password to encode: ')
            encoded_values = encode(values)
            print('Your password has been encoded and stored!') # encodes password with +3 to every digit
            print()
        elif user_choice == 2:
            pass
        elif user_choice == 3: # ends program if option 3 is chosen
            menu_active = False


if __name__ == '__main__':
    main()
