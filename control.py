"""This file is aimed to provide input and validation functionalities"""

INDEXES: tuple = (1, 2, 3, 4, 5)  # benchmark for checking if the word's length is correct


def input_word() -> str:
    """Task of the function is to take in an input of a guess word and return its lower representation"""
    word: str = input('Place the word here, please or [Q]uit to escape\n')
    return word.lower()


def guessing():
    user_input = input_word()
    if user_input == 'q':
        quit()
    guess_word = Word(user_input)
    found_letter: bool = True
    if len(user_input) != 5:
        print('Length of the word not equal to 5')
        return False
    while found_letter:
        letter_found = input('Have you guessed any letter right? Y\\N?\n')
        if letter_found.lower() == 'y':
            while True:
                pos_or_any = input('Was it the right index or random? [I]ndex / [R]andom?\n')
                if pos_or_any.lower() == 'r':
                    any_index = int(input('Please provide the index of the letter that you\'ve guessed\n'))
                    if any_index not in INDEXES:
                        print('The index is not in a range or given incorrectly. Please try again')
                        continue
                    guess_word.any_place(any_index)
                    is_random = input('Are there any other letters to be placed? Y\\N\n')
                    if is_random.lower() == 'y':
                        continue
                    else:
                        break
                if pos_or_any.lower() not in ('r', 'i'):
                    print('[R]andom or [I]ndex?')
                    continue
                # Providing the number of the letter guessed on the right place of the word:
                try:
                    found_index = int(input('Please provide the index of the letter that you\'ve guessed\n'))
                except ValueError:
                    print('Given value is not a number! Please try again\n')
                    continue
                if found_index not in INDEXES:
                    print('The index is not in a range or given incorrectly. Please try again')
                    continue
                guess_word.place_correct(found_index)
                break
        if letter_found.lower() == 'n':
            found_letter: bool = False
        guess_word.update_rejected()
    guess_word.return_correct()
    return guess_word.correct_joined, guess_word.correct, 1, guess_word.any_place_set, guess_word.rejected


class Word:
    """Create a class representation of each word input
    Instance is returning attributes necessary for right implementation
    of word search logic implemented in main.py file"""
    def __init__(self, word: str):
        self.word = word.lower()
        self.correct: list = ['_', '_', '_', '_', '_']  # Create a blank list placeholder for placing the correct letter
        self.list_word: tuple = tuple(self.word)  # Create an immutable tuple for further chars extracting
        self.correct_joined: str = ''
        self.any_place_set: set = set()
        self.rejected: set = set()

    def place_correct(self, index: int):
        self.correct[index - 1] = self.list_word[index - 1]  # index-1 to provide natural user's feeling \
        # (start with 1 when list index is 0)

    def return_correct(self):
        self.correct_joined = ''.join(self.correct)

    def any_place(self, index: int):
        self.any_place_set.add(self.list_word[index - 1])

    def update_rejected(self):
        diff = set(self.list_word).difference(set(self.correct)).difference(self.any_place_set)
        print(f'Litery do odrzucenia: {diff}')
        self.rejected.update(diff)

