import random
from colorama import Fore
import playsound

def main():

    print('\n',Fore.LIGHTBLUE_EX + '!! Welcome to Wordle !!' + Fore.RESET,'\n')

    WORD_LENGTH = choose_letters()
    MAX_ATTEMPTS = choose_attempts()
    Difficulty = choose_difficulty()

    word_set = load_word_set(WORD_LENGTH)
    easy_word_set = load_easy_word_set(WORD_LENGTH)
    if Difficulty == 1:
        secret = random.choice(list(easy_word_set))
    else:
        secret = random.choice(list(word_set))
    secret = secret.rstrip()

    out = []
    word_table = []

    print('For Demo',Fore.YELLOW +secret + Fore.RESET)#test

    print(Fore.GREEN + ' Game Started' + Fore.RESET)
    empty_box(WORD_LENGTH,MAX_ATTEMPTS)

    game_input(secret,word_set,WORD_LENGTH,1,MAX_ATTEMPTS,out,word_table)

    if play_again():
        main()
    else:
        print(Fore.YELLOW + ' Game Over' + Fore.RESET)

def is_a_word(word:str,word_set,WORD_LENGTH):
    if word in word_set and len(word) == WORD_LENGTH:
        return True
    else:
        return False

def input_a_word(secret):
    word = input()
    word = word.upper().rstrip()
    #cheatmode
    while word == 'CHEATMODE':
        i = int(input(Fore.YELLOW + 'Input A Number ' + Fore.RESET))
        if i > len(secret) or i < 0:
            print(Fore.RED + 'You Must Be Joking' + Fore.RESET)
        else:
            print(Fore.RED + secret[i-1] + Fore.RESET)
            word = input()
            word = word.upper().rstrip()
    return word

def load_word_set(letters: int):
    if letters == 4:
        path = r'C:\Users\u1040\OneDrive\桌面\Work\Project1\hard_words\words_4letter.txt'
    elif letters == 5:
        path = r'C:\Users\u1040\OneDrive\桌面\Work\Project1\hard_words\words_5letter.txt'
    else:
        path = r'C:\Users\u1040\OneDrive\桌面\Work\Project1\hard_words\words_6letter.txt'
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set

def load_easy_word_set(letters: int):
    if letters == 4:
        path = r'C:\Users\u1040\OneDrive\桌面\Work\Project1\easy_words\easy_4letter.txt'
    elif letters == 5:
        path = r'C:\Users\u1040\OneDrive\桌面\Work\Project1\easy_words\easy_5letter.txt'
    else:
        path = r'C:\Users\u1040\OneDrive\桌面\Work\Project1\easy_words\easy_6letter.txt'
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set

def correct_or_not(secret:str,word:str,WORD_LENGTH):
    ans = []
    for i in range(WORD_LENGTH - 1,-1,-1):
        if secret.count(word[i]) >= 1 and word.count(word[i]) == 1:
            if word[i] == secret[i]:
                ans.extend('G')
            else:
                ans.extend('Y')
        elif secret.count(word[i]) == 1 and word.count(word[i]) > 1:
            if word[i] == secret[i]:
                ans.extend('G')
            else:
                k = 0
                for j in range(WORD_LENGTH):
                    if word[j] == secret[j] and word[j] == word[i]:
                        k += 1

                if k > 0:
                    ans.extend('W')
                else:
                    if word[:i+1].count(word[i]) == 1:
                        ans.extend('Y')
                    else:
                        ans.extend('W')
        elif secret.count(word[i]) > 1 and word.count(word[i]) > 1:
            if secret.count(word[i]) >= word.count(word[i]):
                if word[i] == secret[i]:
                    ans.extend('G')
                elif word[i] in secret:
                    ans.extend('Y')
                else:
                    ans.extend('W')
            else:
                if word[i] == secret[i]:
                    ans.extend('G')
                elif word[:i + 1].count(word[i]) > secret.count(word[i]):
                    ans.extend('W')
                else:
                    ans.extend('Y') 
        else:
            ans.extend('W')
    ans.reverse()
    return ans
def print_out(secret,word,word_set,WORD_LENGTH,out:list(),word_table,parameter,MAX_ATTEMPTS):
    if is_a_word(word,word_set,WORD_LENGTH):
        correctness = correct_or_not(secret,word,WORD_LENGTH)
        out.append(correctness)

        print('┌','─' * (2 * WORD_LENGTH + 1),'┐',sep = '')

        for i in range(parameter):
            for j in range(WORD_LENGTH):
                if j == 0:
                    print('│ ',end = '')
                if out[i][j] == 'W':
                    print(word_table[i][j],end = ' ')
                elif out[i][j] == 'Y':
                    print(Fore.YELLOW + word_table[i][j] + Fore.RESET,end = ' ')
                else:
                    print(Fore.GREEN + word_table[i][j] + Fore.RESET,end = ' ')
            else:
                print('│')
        
        for i in range(MAX_ATTEMPTS - parameter):
            for j in range(WORD_LENGTH):
                if j == 0:
                    print('│ ',end = '')
                print('_ ',end = '')
            else:
                print('│')

        print('└','─' * (2 * WORD_LENGTH + 1),'┘',sep = '')

        if WORD_LENGTH == 4:
            allgreen = ['G','G','G','G']
        elif WORD_LENGTH == 5:
            allgreen = ['G','G','G','G','G']
        else:
            allgreen = ['G','G','G','G','G','G']

        if correctness == allgreen:
            return 2
        else:
            return 1
    else:
        print(Fore.RED + 'Wrong Input' + Fore.RESET)
        return 0

def game_input(secret,word_set,WORD_LENGTH,parameter:int,MAX_ATTEMPTS:int,out,word_table):
    if parameter > MAX_ATTEMPTS:
        print(Fore.RED + ' !! You Are Failed !!' + Fore.RESET)
        print(' The Answer is',Fore.YELLOW + secret + Fore.RESET,'\n')
        sound_control('WthYouDoing')
    else:
        word = input_a_word(secret)
        word_table.append(word)
        tmp = print_out(secret,word,word_set,WORD_LENGTH,out,word_table,parameter,MAX_ATTEMPTS)
        if tmp == 1:
            tmp = ['ohohoh','trueorfalse']
            if parameter > 1:
                tmp.append('noagain')
                tmp.append('dieagain')
            if parameter == MAX_ATTEMPTS:
                tmp = tmp[:0]
                tmp.append('NoInput')
            sound_control(random.choice(tmp))
            parameter += 1
            game_input(secret,word_set,WORD_LENGTH,parameter,MAX_ATTEMPTS,out,word_table)
        elif tmp == 0:
            sound_control('WthYouDoing')
            word_table = word_table[0:-1]
            game_input(secret,word_set,WORD_LENGTH,parameter,MAX_ATTEMPTS,out,word_table)
        else:
            print(Fore.GREEN + '!! You Won !!' + Fore.RESET)
            sound_control('bingo')

def choose_letters():
    print(Fore.LIGHTGREEN_EX + ' Choose The Letters You Want' + Fore.RESET)
    letters = int(input())
    while letters > 6 or letters < 4:
        print(Fore.RED + ' Letters Must Be 4/5/6' + Fore.RESET)
        letters = int(input())
    return letters

def choose_attempts():
    print(Fore.LIGHTMAGENTA_EX + ' Choose The Max Attempts You Want' + Fore.RESET)
    attempts = int(input())
    while attempts < 1:
        print(Fore.RED + ' Attempts Must Larger Than 1' + Fore.RESET)
        attempts = int(input())
    return attempts

def choose_difficulty():
    print(Fore.LIGHTYELLOW_EX + ' Choose The Difficulty (easy/hard)' + Fore.RESET)
    difficulty = input()
    difficulty = difficulty.lower()
    diff = ['easy','hard']
    while difficulty not in diff:
        print(Fore.RED + ' Choose The Difficulty Again' + Fore.RESET)
        difficulty = input()
        difficulty = difficulty.lower()
    if difficulty == 'easy':
        return 1
    else:
        return 3

def empty_box(WORD_LENGTH,MAX_ATTEMPTS):
    print('┌','─' * (2 * WORD_LENGTH + 1),'┐',sep = '')
    for i in range(MAX_ATTEMPTS):
        for j in range(WORD_LENGTH):
            if j == 0:
                print('│ ',end = '')
            print('_ ', end = '')
        else:
            print('│')
    print('└','─' * (2 * WORD_LENGTH + 1),'┘',sep = '')

def play_again():
    print(Fore.LIGHTYELLOW_EX + ' Play Again ? (yes/no)' + Fore.RESET)
    play = input()
    play = play.lower()
    if play == 'yes':
        return True
    else:
        return False

def sound_control(string:str):
    if string == 'bingo':
        path = r'C:\Users\u1040\OneDrive\桌面\Work\Project1\audio\bingo.wav'
    elif string == 'comfortable':
        path = r'C:\Users\u1040\OneDrive\桌面\Work\Project1\audio\comfortable.wav'
    elif string == 'dieagain':
        path = r'C:\Users\u1040\OneDrive\桌面\Work\Project1\audio\dieagain.wav'
    elif string == 'noagain':
        path = r'C:\Users\u1040\OneDrive\桌面\Work\Project1\audio\noagain.wav'
    elif string == 'ohohoh':
        path = r'C:\Users\u1040\OneDrive\桌面\Work\Project1\audio\ohohoh.wav'
    elif string == 'trueorfalse':
        path = r'C:\Users\u1040\OneDrive\桌面\Work\Project1\audio\trueorfalse.wav'
    elif string == 'WthYouDoing':
        path = r'C:\Users\u1040\OneDrive\桌面\Work\Project1\audio\WthYouDoing.wav'
    try:
        playsound.playsound(path)
    except:
        pass

if __name__ == '__main__':
    main()