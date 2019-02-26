# Problem Set 2, hangman.py
# Name: Prasad Yeole
# Collaborators:
# Time spent: 2 days (18 Feb, 19 Feb) year=2019

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import copy

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
        if char not in letters_guessed:
            return False

    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    secretWordPrint = ''
    for char in secret_word:
        if char not in letters_guessed:
            secretWordPrint += '_ '
        else:
            secretWordPrint += char

    return secretWordPrint


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    abc = string.ascii_lowercase
    for i in range(len(letters_guessed)):
        abc = abc.replace(letters_guessed[i], "")

    return abc


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = []
    allGuess = []
    noGuess = 6
    noWarning = 3
    print(secret_word)
    while noGuess > 0:
        print("You have ", noGuess, " Guess Remaining")
        print("Avaliable Letter :  ", get_available_letters(allGuess))
        print('----------------------------------')
        chGuess = input("Enter the Character : ")

        if chGuess.isalpha():
            if chGuess not in letters_guessed:
                letters_guessed.append(chGuess)
                guessed_word = get_guessed_word(secret_word, letters_guessed)

                if chGuess in secret_word:
                    print('Good guess: ', chGuess)
                else:
                    if chGuess in 'aeiou':
                        noGuess -= 2
                    else:
                        noGuess -= 1
                    print('Oops! That letter is not in my word.')
            else:
                if noWarning > 0:
                    noWarning -= 1
                    print('Oops! You\'ve already guessed that letter. You now have ',
                          noWarning, ' warnings.\n')
                else:
                    noGuess -= 1
                    print(
                        'Oops! You\'ve already guessed that letter. You now have no warnings left so you lose one guess.\n')

        else:
            if noWarning > 0:
                noWarning -= 1
                print('Oops! That is not a valid letter. You have ',
                      noWarning, ' warnings left.')
            else:
                noGuess -= 1
                print(
                    'Oops! You\'ve already guessed that letter. You now have no warnings left so you lose one guess.')

        print('----------------------------------')
        print("Guess Word is : ", guessed_word)
        print('----------------------------------\n\n')

        if is_word_guessed(secret_word, letters_guessed):
            unique_letters = []
            for char in secret_word:
                if char not in unique_letters:
                    unique_letters.append(char)
            print("############ ~ C O N G R A T U L A T I O N ~ #############\n")
            print('# Congratulations, you won!')
            print('# Your total score for this game is ',
                  noGuess * len(unique_letters))
            break

        if noGuess <= 0:
            print('Sorry, you ran out of guesses. The word was ', secret_word)
            break


temp = []
sepWord = []


def swapList():
    for word in sepWord:
        temp.append(word)
    sepWord.clear()


def getHintWord(char, pos):
    #l = 0
    cnt = len(pos)
    f = 0
    for word in temp:
        #l += 1
        for i in pos:
            if word[i] == char:
                f += 1
        if cnt == f:
            sepWord.append(word)
        f = 0
    temp.clear()
    swapList()
    #print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@\nLoop itrate this much time : ",l,"\n@@@@@@@@@@@@@@@@@@@@@@@@@\n")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    for w in wordlist:
        if len(w) == len(secret_word):
            temp.append(w)

    letters_guessed = []
    allGuess = []
    noGuess = 6
    noWarning = 3
    pos = []

    while noGuess > 0:
        print("\tYou have ", noGuess, " Guess Remaining")
        print("\tAvaliable Letter :  ", get_available_letters(letters_guessed))
        print('\t------------------------------------------------')
        chGuess = input("\tEnter the Character : ")

        ##########################################################
        # to Know secret word only for admin purpose
        if chGuess == 'sw':                 # enter 'sw' instead of any char and then pswd
            pswd = input('\tenter the password : ')
            if pswd == 'root123':
                print('\tSecret Word is = ', secret_word)
            print('\t----------------------------------')
            continue
        elif chGuess == "":
            print('\n\t#----------------------------------------------#')
            print("\t# Please, Enter Character Don't leave it Blank #")
            print('\t#----------------------------------------------#\n')
            continue
        elif chGuess == '*':
            print('\tHint words are : ')
            print('\t', temp)
            print('\t-----------------------------------------------------------------------------------------------\n\n\n')
            continue
        ###########################################################

        if chGuess.isalpha():
            if chGuess not in letters_guessed:
                letters_guessed.append(chGuess)
                guessed_word = get_guessed_word(secret_word, letters_guessed)

                if chGuess in secret_word:
                    for i in range(len(secret_word)):
                        if chGuess == secret_word[i]:
                            pos.append(i)

                    print('\tGood guess: ', chGuess)
                else:
                    if chGuess in 'aeiou':
                        noGuess -= 2
                    else:
                        noGuess -= 1
                    print('\tOops! That letter is not in my word.')
            else:
                if noWarning > 0:
                    noWarning -= 1
                    print('\tOops! You\'ve already guessed that letter. You now have ',
                          noWarning, ' warnings.\n')
                else:
                    noGuess -= 1
                    print(
                        '\tOops! You\'ve already guessed that letter. You now have no warnings left so you lose one guess.\n')

        else:
            if noWarning > 0:
                noWarning -= 1
                print('\tWARNING : Oops! That is not a valid letter. You have ',
                      noWarning, ' warnings left.')
                continue
            else:
                noGuess -= 1
                print(
                    '\tOops! You\'ve already guessed that letter. You now have no warnings left so you lose one guess.')
                if not chGuess.isalpha == False:
                    continue

        print('\t----------------------------------')
        print("\tGuess Word is : ", guessed_word)
        print('\t----------------------------------\n')

        if len(pos) > 0:
            getHintWord(chGuess, pos)
            print("\tTotal Hint Word\'s are : ", len(temp))
            # print('\t',temp)
        pos = []

        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")

        if is_word_guessed(secret_word, letters_guessed):
            unique_letters = []
            for char in secret_word:
                if char not in unique_letters:
                    unique_letters.append(char)
            print("\t############ ~ C O N G R A T U L A T I O N ~ #############")
            print("\t#")
            print('\t# Congratulations, you won!')
            print('\t# Your total score for this game is ',
                  noGuess * len(unique_letters))
            break

        if noGuess <= 0:
            print(
                '\tSorry, you ran out of guesses. The word was [ ', secret_word, ' ]')
            break


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.
if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    print("\n\tYour word is", len(secret_word), " char long\n")
    print("\tYou have 3 warnings")
    print("\tYou have 6 guesses")
    # hangman(secret_word)
    hangman_with_hints(secret_word)
    print("\t# Secret Word is :  ", secret_word)
    print("\t#")
    print("\t##########################################################")

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
