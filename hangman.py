import linecache
import random
import time


def reset():  # resets vars for new round
    global word, used, correct, fullWord, attempts, condition
    word = ''
    used = []
    correct = 0
    fullWord = []
    attempts = 12
    condition = 0


def start():  # start function
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
    print('!normal is for normal mode | lives: 12, word length any, guess wrong: -2 lives')
    print('!hard is for hard mode | lives: 6, word length > 6, guess wrong: death')
    mode = input('enter !normal or !hard: ')
    main()


def again():
    global mode, attempts, endCondition, autoSave
    option = input('enter !save to save your results\nenter !play to play again\nenter !stop to stop\n')
    if option == '!stop':
        exit()
    elif option == '!save':  # needs auto save (function maybe)
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
        print('!normal is for normal mode | lives: 12, word length any, guess wrong: -2 lives')
        print('!hard is for hard mode | lives: 6, word length > 6, guess wrong: death')
        mode = input('enter !normal or !hard: ')
        main()
    else:
        exit()


def stats():  # stats for end of game
    global mode, attempts, lives, endCondition
    if attempts < 0:
        attempts = 0
    lives = attempts
    if mode == '!hard':
        attempts = 6
    else:
        attempts = 12
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    if condition == 0:  # sets end condition of the game
        endCondition = 'you won'
    elif condition == 1:
        endCondition = 'you lost | you ran out of lives'
    elif condition == 2:
        endCondition = 'you lost | you guessed the wrong word'
    elif condition == 3:
        endCondition = 'you lost | you gave up'
    else:
        endCondition = 'you lost | no lose information'
    print(endCondition)
    print(
        f'word: {word[:-1]}\nmode: {mode[1:]}\nlives left: {lives}\nwrong letters: {attempts - lives}\nused letters: {len(used)}')
    print(f'used letter list: {used}')
    time.sleep(1)
    print('\ncheck out my github: https://github.com/cqb13')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    again()


def main():
    global fullWord, word, correct, attempts, condition
    word = linecache.getline('words', random.randrange(0, 8749))
    if mode == '!hard':
        print('you are on hard mode')
        attempts = 6
        while len(word) <= 6:
            word = linecache.getline('words', random.randrange(0, 8749))
    else:
        print('you are on normal mode')
    wordlength = len(word)
    while wordlength != 0:  # creates the word visual
        fullWord.append('_')
        wordlength -= 1
    fullWord.pop()  # fix's weird glitch with word visual
    print(fullWord)
    print(f'word length: {len(word) - 1}')  # idk whats wrong with this, but it needs to be like this
    print(f'lives: {attempts}')

    while attempts > 0:
        option = input('enter a guess: ')

        if option == '!used':
            print(f'used letters: {used}')
        elif option == '!save':
            print('you can do that at the end of a round')
        elif option == '!end':
            print('are you sure you want to give up?')
            print('enter y to give up\nenter any key to skip')
            option = input('enter your choice: ')
            if option == 'y':
                condition = 3
                stats()
            else:
                print('skipped')
        elif option == '!guess':  # option to guess the full word
            if mode == '!hard':
                print('if incorrect you will lose')
            else:
                print('if incorrect you will lose 2 lives')
            print('enter y to give up\n enter any key to skip')
            option = input('enter your choice: ')
            word = word[:-1]  # something wrong with word, idk anymore
            if option == 'y':  # makes sure that you actually want to do it
                option = input('enter word: ')
                if option == word:  # checks if the word is right
                    condition = 0
                    stats()
                elif option != word and mode != '!hard':  # checks if you are on normal mode
                    print('that\'s not the right word | -2 attempts')
                    attempts -= 2
                    print(f'lives: {attempts}')
                    if attempts < 0:
                        condition = 1
                        stats()
                else:
                    condition = 2
                    stats()
            else:
                print('skipped')
        else:
            if len(option) > 1:  # checks that you only entered 1 letter
                print('enter !guess to guess the full word')
            else:
                letterUsed = False  # I don't fucking know, it does something I think
                num = 0
                for _ in used:  # checks if letter has been used before
                    if option == used[num]:
                        print(f'letter {option} has already been used')
                        print('enter !used to see all used letters')
                        letterUsed = True
                    num += 1

                num = 0
                for _ in word:  # adds letter to its spot in hidden word
                    if letterUsed is True:
                        pass
                    elif option == word[num]:  # weird word symbol thing
                        temp = list(fullWord)
                        temp[num] = option
                        fullWord = ''.join(temp)
                        correct += 1
                    num += 1

                if option not in word and option not in used:  # checks if it should take away a life
                    attempts -= 1

                print(fullWord)

                if letterUsed is True:  # adds letter to used list
                    pass
                else:  # adds every letter to list
                    used.append(option)
                if fullWord == word[:-1]:  # checks if you won
                    condition = 0
                    stats()
                elif attempts <= 0:  # checks if you have too many wrong letters
                    condition = 1
                    stats()

                print(f'lives: {attempts}')
                print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')


print('---< welcome to hangman >---')
print('---<   made by: cqb13   >---\n')
time.sleep(1)
start()

# make auto save that works
