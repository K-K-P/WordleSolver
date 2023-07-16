"""This file implements few functionalities:
- imports the dictionary in txt and outputs the list pairs word - set(word)
- removes from the db the words that do not fit the pattern"""

WORD_LEN = 5


def init_db():
    words_db: list = []
    with open('.\\Words_Base\\db.txt', 'r') as file:
        for word in file:
            words_db.append((word.replace('\n', ''), set(word.replace('\n', ''))))
    return tuple(words_db)


def filter_db(any_place_set: set, guessed_sofar: list, db: tuple, rejected: set):
    temp_db: list = []
    if not any_place_set and ''.join(guessed_sofar) == '_____':
        return db
    for word_tuple in db:
        word = word_tuple[0]
        word_set = word_tuple[1]
        flag_set: bool = False
        flag_guessed: bool = False
        flag_not_rejected: bool = True
        if any_place_set.issubset(word_set):
            flag_set = True
        guessed_chars = [char for char in guessed_sofar if char != '_']
        guessed_qty = len(guessed_chars)
        char_covered = 0
        for i, char in enumerate(guessed_sofar):
            if char == word[i]:
                char_covered += 1
        if char_covered == guessed_qty:
            flag_guessed = True
        for char in word:
            if char in rejected:
                flag_not_rejected = False
        if flag_set and flag_guessed and flag_not_rejected:
            temp_db.append(word)
    temp_db: tuple = tuple(temp_db)
    return temp_db


if __name__ == '__main__':
    # Testing example
    initial_db = init_db()
    filtered_db = filter_db({'a', 'b'}, ['_', 'l', '_', 'z', '_'], initial_db, {'u'})
    print(filtered_db)