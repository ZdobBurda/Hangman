import random

def hangman():
    words = ['python', 'hangman', 'game', 'programming', 'computer']
    word = random.choice(words)
    guesses = ''
    turns = 6

    while turns > 0:
        failed = 0

        for char in word:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_', end=' ')
                failed += 1

        if failed == 0:
            print('\nCongratulations! You won!')
            break

        guess = input('\nGuess a character: ')
        guesses += guess

        if guess not in word:
            turns -= 1
            print('Wrong guess. Turns left:', turns)

        if turns == 0:
            print('You lost. The word was:', word)

# Example usage
hangman()


























