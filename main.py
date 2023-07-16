"""This tool is aimed to provide help in solving Wordle / Literalnie game"""

import control
import load_db

COUNTER: int = 6


def main():
    db = load_db.init_db()
    guess: list = ['_', '_', '_', '_', '_']
    any_place_set: set = set()
    countdown: int = COUNTER
    rejected_all = set()
    while countdown > 0:
        print(f'All rejected: {rejected_all}')
        print(f'You have {countdown} attempts left')
        guess_word = control.guessing()
        if not guess_word:
            continue
        print(f'Word that you\'ve provided: {guess_word[0].upper()}\n')
        any_place_set.update(guess_word[3])
        for i, char in enumerate(guess_word[1]):
            if char != '_':
                guess[i] = char

        countdown -= guess_word[2]
        rejected = guess_word[4]
        print(rejected)
        rejected_all.update(rejected.difference(set(guess)).difference(any_place_set))
        print('What we have so far:', ''.join(guess), 'and letters to be placed randomly: ',
              ''.join(any_place_set), sep=' ')
        word_suggestions = load_db.filter_db(any_place_set, guess, db, rejected_all)
        print('Here are the suggestions of the words you might want to use in your next try:')
        print('\n'.join(word_suggestions))
    print('Sorry, this was Your last attempt. Please, try again')


main()
