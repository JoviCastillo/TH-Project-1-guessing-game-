import random

highscore = []


def not_in_range(guess_it):
    """This is to check that the numbers inputted by the user are in range,
    and will let the user know. If the numbers are in range then it passes.
    """
    if guess_it < 1:
        print('I am not thinking of negative numbers!')
    elif guess_it > 10:
        print('That number is way bigger than 10!')
    else:
        pass


def new_game(tries):
    """After the user has guessed the number correctly, the game
    will ask the player if they would like to play again. Yes will start
    the game again. No will exit the game. Highscore will be displayed
    by the lowest amount of tries recorded.
    """
    play_again = input('Would you like to play again? (Yes/No) ')
    if play_again.upper() == 'YES':
        highscore.append(tries)
        highscore.sort
        print('The highscore is {}.'.format(highscore[0]))
        start_game()
    elif play_again.upper() == 'NO':
        exit()
    else:
        play_again = input('Please let me know by typing yes or no: ')


def start_game():  # title screen of the game
    """This is the start of the game which include the title screen and
    is the main function that runs all the other functions as well.
    """
    print('-' * 40)
    print('Welcome to the Number Guessing Game!!!')
    print('-' * 40)
    print('I am thinking of a number between 1-10.')
    random_number = random.randint(1, 10)
    tries = 0
    while True:
        try:
            guess_it = int(input('Can you guess it?: '))
        except ValueError:
            print('I said number, not gibberish!')
        else:
            while guess_it != random_number:
                not_in_range(guess_it)
                tries += 1
                if guess_it > random_number:
                    print('That is too high!')
                elif guess_it < random_number:
                    print('That is too low')
                break
            else:
                print('You guessed it right! Your number was {}.'.format(random_number))
                print('It took you {} tries.'.format(tries))
                break
    new_game(tries)


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
