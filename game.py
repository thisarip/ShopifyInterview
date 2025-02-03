# val dictionary = Set("able", "bell", "boss", "cast", "cash", "knot", "note", "near", "over", "salt", "wood")
# Implement a word guessing game, such that when initialized with a dictionary and a target word, the user can enter guesses, 
# and the system indicates whether the guess is correct or not, and provide hints to help the user guess.

# The dictionary is a series of valid words, all four letters.
# The target word is randomly selected from the dictionary
# The user can enter up to 5 guesses, and after each guess the system provides a hint, or indicates the target word has been guessed.
# Each guess must be a valid word in a specific dictionary, otherwise the submitted word is rejected immediately. In this case no hints are provided and this invalid submission does not count toward a turn. A list of words pulled from an English dictionary is available for reference (see sample_dictionary.txt, also available in this public gist).
# A hint has the following structure:
# a number 1 indicates the position contains a correct character in the correct position
# a number 0 indicates the position contains a correct character but in an incorrect position
# a hyphen - indicates the position contains an incorrect character
import random

class Game:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def run_game(self):
        word = random.choice(self.dictionary)

        for _ in range(5):
            guess = input("Please guess a word: ")
            while guess not in self.dictionary:
                print("This word is not in the dictionary")
                guess = input("Please guess a word: ")

            if guess == word:
                print("Yay! You guessed the word!")
                break

            hint = ''
            for i in range(len(guess)):
                guessed_char = guess[i]
                correct_char = word[i]
                if guessed_char == correct_char:
                    hint += '1'
                elif guessed_char not in word:
                    hint += '-'
                else:
                    char_index = word.index(guessed_char)
                    if word[char_index] == guess[char_index]:
                        hint += '-'
                    else:
                        hint += '0'
            print(hint)

        print("The word was " + word)

game = Game(["able", "bell", "boss", "cast", "cash", "knot", "note", "near", "over", "salt", "wood"])
game.run_game()