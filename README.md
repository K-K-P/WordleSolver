# WordleSolver
The application that helps in solving Literalnie / Wordle puzzles

This particular version of the application helps the user to solve Literalnie's (PL version of Wordle) puzzles.
The aim here is to provide the user the words that would fit the constraints that are being imposed with every guess:

eg. first guess: "bluza" - we did the first try in the "Literalnie" app and got one letter, "z" right - not only we guessed the letter, we also got the position correctly. 
Now, "WordleSolver" will filter the database and provide the user the words which have "z" letter on the right spot (i.e. 4th) and do not contain letters b, l, u, a.
Another guess: procedure continues with another letters to be or not to be included in search filter. 

prepare_data.py - this file provides the script useful for filtering the whole polish dictionary and providing only 5 - letters long words
<br>
control.py - whole control and interface layer is focused here. Creating instance for each word looked through, inputting the word and whole "guessing" procesure is implemented here
<br>
load_db.py - this file contaings the code for initializing the database for a session and for filtering the database
<br>
main.py - main file for starting the app, implementing all the logic into one script
<br>
db.txt - text file with 5 - letter long words

At this point, app doesn't solve the whole puzzle for the user. It is planned to develop the probability matrix (taking into account the frequency of presence of the each word's particular letter).
When tested, app turned out to be a decent help - worst case scenario, I managed to guess the word at 5th attempt - it's all up to luck and user's gut. 
