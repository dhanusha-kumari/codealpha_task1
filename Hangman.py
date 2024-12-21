import random

# List of words to guess
words = ['apple', 'banana', 'cherry', 'date', 'grape']

def get_random_word(word_list):
    """Returns a random word from the provided list."""
    return random.choice(word_list)

def display_board(missed_letters, correct_letters, secret_word):
    """Displays the current state of the game."""
    print('Missed letters:', ' '.join(missed_letters))
    blanks = '_' * len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
    print('Current word:', ' '.join(blanks))

def get_guess(already_guessed):
    """Prompts the player for a letter and checks for validity."""
    while True:
        guess = input('Guess a letter: ').lower()
        if len(guess) != 1 or guess in already_guessed or not guess.isalpha():
            print('Invalid input. Please enter a single letter that you have not guessed yet.')
        else:
            return guess

def play_again():
    """Asks the player if they want to play again."""
    return input('Do you want to play again? (yes or no): ').lower().startswith('y')

# Main game loop
print('H A N G M A N')
missed_letters = ''
correct_letters = ''
secret_word = get_random_word(words)
game_is_done = False

while True:
    display_board(missed_letters, correct_letters, secret_word)
    guess = get_guess(missed_letters + correct_letters)

    if guess in secret_word:
        correct_letters += guess
        # Check if the player has won
        if all(letter in correct_letters for letter in secret_word):
            print(f'Yes! The secret word is "{secret_word}"! You have won!')
            game_is_done = True
    else:
        missed_letters += guess
        # Check if the player has lost
        if len(missed_letters) == 6:  # Assuming 6 incorrect guesses allowed
            display_board(missed_letters, correct_letters, secret_word)
            print(f'You have run out of guesses! The word was "{secret_word}".')
            game_is_done = True

    if game_is_done:
        if play_again():
            missed_letters = ''
            correct_letters = ''
            secret_word = get_random_word(words)
            game_is_done = False
        else:
            break
