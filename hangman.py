import linecache
import random
import time


# colors for console
red = "\u001B[31m"
yellow = '\u001B[33m'
green = '\u001B[32m'
white = '\u001B[39m'
blue = '\u001B[24m'


# resets vars for new round
def reset():
    global word, used, correct, fullWord, attempts, condition
    word = ''
    used = []
    correct = 0
    fullWord = []
    attempts = 12
    condition = 0


# start function
def start():
    global mode
    print('---< commands >---')
    print('enter any letter as your guess')
    print('enter !guess to guess the whole word')
    print('enter !used to see used letters')
    print('enter !save to save your stats')
    print('enter !end to give and end the game')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    reset()
    time.sleep(1)
    print(green + '!normal is for normal mode | lives: 12, word length any, guess wrong: -2 lives')
    print(red + '!hard is for hard mode | lives: 6, word length > 6, guess wrong: death' + white)
    mode = input('enter !normal or !hard: ')
    main()


def again():
    global mode, attempts, endCondition, autoSave
    option = input('enter !save to save your results\nenter !play to play again\nenter !stop to stop\n')
    if option == '!stop':
        exit()
    elif option == '!save':
        file = open('history', 'a')
        file.write('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
        file.write(f'{endCondition}\n')
        file.write(
            f'word: {word[:-1]}\nmode: {mode[1:]}\nlives left: {lives}\nwrong letters: {attempts - lives}\nused letters: {len(used)}\n')
        file.write(f'used letter list: {used}\n')
        again()
    elif option == '!play':
        reset()
        time.sleep(1)
        print(green + '!normal is for normal mode | lives: 12, word length any, guess wrong: -2 lives')
        print(red + '!hard is for hard mode | lives: 6, word length > 6, guess wrong: death' + white)
        mode = input('enter !normal or !hard: ')
        main()
    else:
        exit()


# stats for end of game
def stats():
    global mode, attempts, lives, endCondition
    if attempts < 0:
        attempts = 0
    lives = attempts
    if mode == '!hard':
        attempts = 6
    else:
        attempts = 12
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    # sets end condition of the game
    if condition == 0:
        endCondition = green + 'you won' + white
    elif condition == 1:
        endCondition = red + 'you lost | you ran out of lives' + white
    elif condition == 2:
        endCondition = red + 'you lost | you guessed the wrong word' + white
    elif condition == 3:
        endCondition = red + 'you lost | you gave up' + white
    else:
        endCondition = yellow + 'you lost | no lose information' + white
    print(endCondition)
    print(
        f'word: {word[:-1]}\nmode: {mode[1:]}\nlives left: {lives}\nwrong letters: {attempts - lives}\nused letters: {len(used)}')
    print(f'used letter list: {used}')
    time.sleep(1)
    print(blue + '\ncheck out my github: https://github.com/cqb13' + white)
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    again()


def main():
    global fullWord, word, correct, attempts, condition
    word = linecache.getline('words', random.randrange(0, 8749))
    if mode == '!hard':
        print(red + 'you are on hard mode' + white)
        attempts = 6
        while len(word) <= 6:
            word = linecache.getline('words', random.randrange(0, 8749))
    else:
        print(green + 'you are on normal mode' + white)
    wordlength = len(word)
    # creates the word visual
    while wordlength != 0:
        fullWord.append('_')
        wordlength -= 1
    fullWord.pop()
    print(fullWord)
    # takes enter key value from words file needs it removed
    print(f'word length: {len(word) - 1}')
    print(f'lives: ' + green + f'{attempts}' + white)

    while attempts > 0:
        option = input('enter a guess: ')

        if option == '!used':
            print(f'used letters: {used}')
        elif option == '!save':
            print(yellow + 'you can do that at the end of a round' + white)
        elif option == '!end':
            print(yellow + 'are you sure you want to give up?')
            print('enter y to give up\nenter any key to skip' + white)
            option = input('enter your choice: ')
            if option == 'y':
                condition = 3
                stats()
            else:
                print('skipped')
        # option to guess the full word
        elif option == '!guess':
            if mode == '!hard':
                print(yellow + 'if incorrect you will lose' + white)
            else:
                print(yellow + 'if incorrect you will lose 2 lives')
            print('enter y to give up\n enter any key to skip' + white)
            option = input('enter your choice: ')
            word = word[:-1]
            # confirm option
            if option == 'y':
                option = input('enter word: ')
                # checks if the word is right after guessing full word
                if option == word:
                    condition = 0
                    stats()
                # checks if you are on normal mode
                elif option != word and mode != '!hard':
                    print(red + 'that\'s not the right word | -2 attempts' + white)
                    attempts -= 2
                    print(f'lives: {attempts}')
                    if attempts < 0:
                        condition = 1
                        stats()
                else:
                    condition = 2
                    stats()
            else:
                print(yellow + 'skipped' + white)
        else:
            if len(option) > 1:  # checks that you only entered 1 letter
                print(yellow + 'enter !guess to guess the full word' + white)
            elif option.isalpha():  # only allows letters
                letterUsed = False  # I don't fucking know, it does something I think
                num = 0
                # checks if letter has been used before
                for _ in used:
                    if option == used[num]:
                        print(yellow + f'letter {option} has already been used')
                        print('enter !used to see all used letters' + white)
                        letterUsed = True
                    num += 1

                num = 0
                # adds letter to its spot in hidden word
                for _ in word:
                    if letterUsed is True:
                        pass
                    # setup for blank spots
                    elif option == word[num]:
                        temp = list(fullWord)
                        temp[num] = option
                        fullWord = ''.join(temp)
                        correct += 1
                    num += 1

                # checks if it should take away a life
                if option not in word and option not in used:
                    attempts -= 1

                print(fullWord)

                # adds letter to used list
                if letterUsed is True:
                    pass
                else:  # adds every letter to list
                    used.append(option)
                if fullWord == word[:-1]:  # checks if you won
                    condition = 0
                    stats()
                elif attempts <= 0:  # checks if you have too many wrong letters
                    condition = 1
                    stats()

                # health color
                if mode == '!normal':
                    if attempts >= 8:
                        print(f'lives: ' + green + f'{attempts}' + white)
                    elif 8 > attempts >= 4:
                        print(f'lives: ' + yellow + f'{attempts}' + white)
                    else:
                        print(f'lives: ' + red + f'{attempts}' + white)
                else:
                    if attempts >= 4:
                        print(f'lives: ' + green + f'{attempts}' + white)
                    elif 4 > attempts >= 2:
                        print(f'lives: ' + yellow + f'{attempts}' + white)
                    else:
                        print(f'lives: ' + red + f'{attempts}' + white)
                print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            else:
                print(yellow + 'you can only guess letters' + white)


print('---< welcome to hangman >---')
print('---<   made by: cqb13   >---\n')
time.sleep(1)
start()
