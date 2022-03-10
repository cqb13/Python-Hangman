import linecache
import random
import time

# base
word = ''
used = []
correct = 0
fullWord = []
# stats
attempts = 12


def info():
    print('---< commands >---')
    print('enter any letter as your guess')
    print('enter !guess to guess the whole word')
    print('enter !used at any time during the game to see the letters you already used')
    print('\n')


def stats():  # stats for end of game
    wrongLetter()
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print(f'word: {word[:-1]}\nlives left: {attempts}\nwrong letters: {wrongGuess}\nused letters: {len(used)}')
    time.sleep(1)
    print('\ncheck out my github: https://github.com/cqb13')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    time.sleep(20)
    exit()


def wrongLetter():  # finds the amount of wrong letter I think
    global wrongGuess
    num = 0
    wrongGuess = (len(used))
    for i in used:
        if used[num] in word:
            wrongGuess -= 1
        else:
            pass
        num += 1


def options():
    global fullWord, word, correct, attempts
    word = linecache.getline('words', random.randrange(0, 8749))
    wordlength = len(word)
    while wordlength != 0:  # creates the word visual
        fullWord.append('_')
        wordlength -= 1
    fullWord.pop()  # fix's weird glitch with word visual
    print(fullWord)
    print(f'word length: {len(word) - 1}')  # idk whats wrong with this, but it needs to be like this
    print(f'lives: {attempts}')

    while attempts > 0:
        option = input('enter a guess')

        if option == '!used':
            print(f'used letters: {used}')
        elif option == '!guess':  # option to guess the full word
            print('if you get the word wrong you will lose.\npress y to continue '
                  'or x to skip')
            option = input('y to continue, or any key to skip')
            word = word[:-1]  # something wrong with word, idk anymore
            if option == 'y':  # makes sure that you actually want to do it
                option = input('enter word')
                if option == word:  # checks if the word is right
                    print('you won')
                    stats()
                else:
                    print('you lost')
                    stats()
            else:
                print('skipped')
        else:
            if len(option) > 1:  # checks that you only entered 1 letter
                print('enter !full to guess the word')
            else:
                letterUsed = False  # I don't fucking know, it does something I think
                num = 0
                for i in used:  # checks if letter has been used before
                    if option == used[num]:
                        print(f'letter {option} has already been used')
                        print('enter !used to see all used letters')
                        letterUsed = True
                        pass
                    else:
                        pass
                    num += 1

                num = 0
                for i in word:  # adds letter to its spot in hidden word
                    if letterUsed is True:
                        pass
                    elif option == word[num]:  # weird word symbol thing
                        temp = list(fullWord)
                        temp[num] = option
                        fullWord = ''.join(temp)
                        correct += 1
                    else:
                        pass
                    num += 1

                if option not in word and option not in used:  # checks if it should take away a life
                    attempts -= 1
                else:
                    pass

                print(fullWord)

                if letterUsed is True:  # adds letter to used list
                    pass
                else:  # adds every letter to list
                    used.append(option)
                if correct == len(word) - 1:  # checks if you won
                    print('you won')
                    stats()
                elif attempts <= 0:  # checks if you have too many wrong letters
                    print('you lost')
                    stats()
                else:
                    pass

                print(f'lives: {attempts}')
                print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')


print('---< welcome to hangman >---')
print('---<   made by: cqb13   >---')
print('\n')
time.sleep(1)
info()
time.sleep(1)
options()
