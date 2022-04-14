import random 

num_digits = 3
max_guess = 5

def main():
    print(f'''I am thinking of a {num_digits} digit number. 
    It has no repeated digits.Try to guess what the number is:
    when I say:     That means:
        Juice            One digit is correct but in the wrong position.
        Guido           One digit is correct but and in the right position.
        Bagels          No digit is correct.
    Example: If the secret number was 248 and your guess was 843, the clues would be Fermi Pico.''')

    while True: # main game loop
        #this stores the secret number or winning num
        secret_num = get_secret_num()
        print('I thave thought up a number.')
        print(f'You have {max_guess}')

        num_guess = 1
        while num_guess <= max_guess:
            guess = ''
            #loop continues until they enter a valid guess
            while len(guess) != num_digits or not guess.isdecimal():
                print(f'Guess {num_guess}: ')
                guess = input('> ')
                
                # Asking if you want you play again
        print('Do you want to play again? (press y or n)')
        if not input('> ').lower():
            break
    print('Thanks for playing!')


def get_secret_num():
    numbers = list('0123456789') #create a list of digits 0 to 9
    random.shuffle(numbers)     #shuffle numbers in a random order

    #get the first digits in the list for the secret number:
    secret_num = ''
    for i in range(num_digits):
        secret_num += str(numbers[i])
    return secret_num


def get_clue(guess,secret_num):
    if guess == secret_num:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            #a correct digit is in the correct place
            clues.append('Juice')
        elif guess[i] in secret_num:
            #a corect digit is in the incorrect place
            clues.append('Guido')
    if len(clues) == 0:
        return 'Bagels' #there are not correct digit at all
    else:
        #sort the clues into alphabethical order so thier order
        #does not give information away
        clues.sort()
        #make a single string from the list of clues
        return ' '.join(clues)


#if the program is run (instead of imported), run the game:
#if __name__ == '__main__':
#   main()
main()