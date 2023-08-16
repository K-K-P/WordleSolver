"""
Tool used for preparing word database.
Tool takes the polish words database in and outputs database containing only 5 - characters long words
"""

WORD_LENGTH: int = 5

with open(r'.\Words_Base\slowa.txt', 'r', encoding='UTF-8') as input:
    with open(r'.\Words_Base\db.txt', 'w') as db:
        for word in input:
            word = word.strip()
            if len(word) == WORD_LENGTH and type(word) == str:
                db.write(word + '\n')





