"""
CSSE1001 Assignment 1
Semester 2, 2017
"""

# Import statements go here
import random

# Fill these in with your details
__author__ = ""
__email__ = ""
__date__ = ""

# Some useful constants

# Each step of the game
STEPS = (
    # position, length
    (0, 2),
    (0, 3),
    (1, 3),
    (2, 3),
    (3, 3),
    (2, 4),
    (1, 4),
    (0, 4),
    (0, 5),
    (1, 5),
    (0, 6),
)

# Score values for correctly guessing a letter
RIGHT_POSITION_VALUE = 100
WRONG_POSITION_VALUE = 20


# Write your code here (i.e. functions)

def load_words(filename, length):
    """
    Returns a list of all words contained in filename that have the given length.
    """
    words_needed = []
    with open(filename) as file:
        all_words = [L.rstrip('\n') for L in file]
        for word in all_words:
            if len(word) == length:
                words_needed.append(word)
    return words_needed


def compute_score(guess, position, word):
    """
    Computes the score for a given guess, as outlined in 1. Introduction.
    """
    score = 0
    word_set = set(word)
    # First, determine whether the words in each location are correct
    for index in range(len(guess)):
        if guess[index] == word[position + index]:
            score = score + RIGHT_POSITION_VALUE
            word_set.remove(word[position + index])
    # Then calculate the wrong position score
    for index in range(len(guess)):
        if guess[index] in word_set:
            score = score + WRONG_POSITION_VALUE
    return score


def prompt_guess(position, length):
    """
    Repeatedly prompts the user to make a guess at a given position. Returns the first guess with correct length.
    """
    type_ahead = "Now guess %d letters corresponding to letters %d to %d of the unknown word: "
    input_letters = input(type_ahead % (length, position + 1, position + length))
    # Check that the length of the input is correct
    while len(input_letters) != length:
        print("Invalid guess '%s'. Should be %d characters long." % (input_letters, length))
        print()
        input_letters = input(type_ahead % (length, position + 1, position + length))
    return input_letters


def print_guess(guess, position):
    """
     Obtain the representation of an underlined word
    """
    print_word = "_" * position + guess + "_" * (6 - position - len(guess))
    return print_word


def main():
    """
    Handles top-level interaction with user.
    """
    # Write the code for your main function here

    all_words_of_6_letters = load_words("words.txt", 6)
    # Choose a 6 letter word at random
    word = all_words_of_6_letters[random.randint(0, len(all_words_of_6_letters) - 1)]

    print("Welcome to the brain teasing zig-zag word game.\n")
    user_name = input("What is your name? ")
    print("\nHi %s! We have selected a %d letter word for you to guess.\n" % (user_name, 6))
    print("Let the game begin!\n")

    total_score = 0  # Final score
    # Start cycle step
    for (position, length) in STEPS:
        guess = prompt_guess(position, length)
        this_time_guess_score = compute_score(guess, position, word)
        print("Your guess and score were: %s : %d\n" % (print_guess(guess, position), this_time_guess_score))
        total_score = total_score + this_time_guess_score

    # Determine if the last one was successful
    if this_time_guess_score == 600:
        print("Congratulations! You correctly guessed the word '%s'.\n" % word)
    else:
        print("\nYou did not manage to guess the correct word. It was '%s'. Better luck next time." % word)
    print("Your total score was %d." % total_score)


if __name__ == "__main__":
    main()
