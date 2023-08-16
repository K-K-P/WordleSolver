"""UPDATE:
Using the words' percentage frequency according to
https://sjp.pwn.pl/poradnia/haslo/frekwencja-liter-w-polskich-tekstach;7072.html
to propose the user the most "probable" word"""

"""Preparing the data:"""

with open(r'.\Words_Base\words_percentage.txt', 'r', encoding='UTF-8') as percentage:
    with open(r'.\Words_Base\word_percentage.txt', 'w') as percentage_db:
        for line in percentage:
            percentage_db.write(line.strip('\n'))
            percentage_db.write(';')
