# A function to play the game hangman

# import methods from library
import random

# A dictionary in which possible wordlist are stored in a list
wordlist = ['avocado','battleship','candle','dovetail','elongate','fastidious','gyroscope','hijinks','indigo','jalapeno','kitty','lynx','manatee','notoriety','oplulent','pinstripe','querulous','rash','sanitary','twenty','unveil','vexatious','willowy','xylophone','yiddish','zipper']

# Defines empty strings and lists for first letter and evolving Incorrects
Letter = ''
Incorrects = ''
GuessList = []

# Initialises the counters
NumGuess = 0
counter = 0

# Picks a word from the dictionary
answer = wordlist[random.randint(0, len(wordlist)-1)]

# Populates guess with placeholders *
for element in answer:
    GuessList.append('*')

# Asks user to guess letters and populates a list of letters which have already been guessed:
while ''.join(GuessList) != answer and Letter != 'quit':
    NumGuess += 1
    Letter = input('(Guess) Enter a letter or guess the word (type \'quit\' to exit)'+''.join(GuessList)+' > ')

    # Block to end game if you reach 11 incorrect guesses
    if len(Incorrects) >= 11:
        print('Too bad!')
        Letter = 'quit'

    # Block for guessing the word outright
    elif Letter == answer:
        Letter = 'quit'

    # Block for guessing an incorrect word
    elif (len(Letter) == len(answer)) and (Letter != answer):
        print('Unlucky, the word is not ' + Letter.upper())
        Incorrects = Incorrects + '9'

    # Block for inputting a previous correct/incorrect guess
    elif (Letter in Incorrects) or (Letter in GuessList):
        print('you have already guessed the letter ' + Letter.upper())
        NumGuess -= 1

    # Handles new incorrect guesses
    elif not (Letter in answer):
        print('There are no ' + Letter.upper() + '\'s')
        Incorrects = Incorrects + Letter

    # Handles new correct guesses
    else:
        counter = 0
        for character in answer:
            if character == Letter:
                # insert guessed letter
                GuessList.insert(counter,Letter)
                # remove placeholder
                GuessList.pop(counter+1)
            counter += 1

if len(Incorrects) <= 10:
    print('Congratulations')

print('the word was '+ answer.upper())
print('You used '+ str(NumGuess) + ' guesses.')
print('You added '+ str(len(Incorrects)) + ' sections to the scaffold')
