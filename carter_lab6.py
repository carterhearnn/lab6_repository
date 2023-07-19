def encode(values): # encode function adds 3 to every value given to the program
    encoded_values = ''
    for pos, num in enumerate(values):
        num = int(num) + 3
        num = str(num)
        encoded_values += num

    return encoded_values


# method subtracts 3 from each digit in given encoded_values
def decode(encoded_values):
	decoded_password = ''
	for idx, num in enumerate(encoded_values):    # for-loop iterates over encoded_values
		num = int(num) - 3
		num = str(num)
		decoded_password += num

	return decoded_password      # returns original password given by user


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

        # if user_option equals '2', the encoded_values are decoded back to the original password
        elif user_choice == 2:
            decoded_password = decode(encoded_values)
            print(f'The encoded password is {encoded_values}, and the original password is {decoded_password}.')
            print()

        elif user_choice == 3: # ends program if option 3 is chosen
            menu_active = False


if __name__ == '__main__':
    main()
