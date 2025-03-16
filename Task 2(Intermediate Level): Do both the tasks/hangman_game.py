
import random

def choose_word():
    return random.choice(['python', 'hangman', 'programming'])

def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / \
           -
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \|
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |      
           |      
           |      
           -
        """,
        """
           --------
           |      |
           |      
           |      
           |      
           |      
           -
        """
    ]
    return stages[6 - tries]

def play():
    word = choose_word()
    guessed = ['_'] * len(word)
    tries = 6

    while tries > 0 and '_' in guessed:
        print(display_hangman(tries))
        print(' '.join(guessed))
        guess = input("Guess a letter: ").lower()
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            tries -= 1
            print(f"Wrong! {tries} tries left.")

    print(display_hangman(tries))
    if '_' not in guessed:
        print(f"You guessed it! The word was '{word}'.")
    else:
        print(f"Out of tries! The word was '{word}'.")

if __name__ == "__main__":
    play()
