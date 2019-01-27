from model import ReadWordFile,Hangman,ScoreBoard,ScoreFileRW
from os import system,listdir
import time

def router(route):
    clear_screen()
    if route == 'main_menu':
        intro()
        return main_menu()
    elif route == 'start':
        return category_menu()
    elif route == 'how to play':
        return how_to_play()
    elif route == 'scoreboard':
        return scoreboard_page()

def clear_screen():
    try:
        system('clear')
    except Exception:
        try:
            system('cls')
        except Exception:
            pass

def print_choice(choice):
    for key in choice:
        print(f'{key}) {choice[key].title().replace("_"," ")}')

def get_category_name():
    path = 'words/'
    name_list = []
    for file_name in listdir(path):
        name_list.append(return_first_line(path+file_name))
    name_list.sort()
    return name_list

def get_category_file_name():
    path = 'words/'
    name_list = listdir(path)
    return name_list

def return_first_line(file):
    with open( file, 'r') as file_open:
        return file_open.readline().strip()

def intro():
    intro_man = Hangman()
    while intro_man.is_dead() != True:
        intro_man.draw_next()
        intro_man.print_hangman()
        time.sleep(0.08)
        clear_screen()

def main_menu():
    print(f"{'######### Hang Man #########':^30}")
    menu_choice = { 1:'start', 2:'how to play', 3:'scoreboard'}
    print_choice(menu_choice)
    return menu_choice

def category_menu():
    path = 'words/'
    print(f"{'#### Choose Word Category ####':^30}")
    category_choice = dict()
    category_choice[0] = 0
    category_name_list = get_category_name()
    category_file_name = get_category_file_name()
    for no,name in enumerate(category_name_list,1):
        print(f"{no}) {name}")
    print('0)Main Menu')
    for no,name in enumerate(category_file_name,1):
        category_choice[no] = name
    choice = int(input("Your Choice: "))
    while choice not in category_choice:
        print("Invaild Choice")
        choice = int(input("Your Choice: "))
    if choice == 0:
        clear_screen()
        menu_choice = main_menu()
        return menu_choice
    else:
        game_play(path+category_choice[choice])
        clear_screen()
        menu_choice = main_menu()
        return menu_choice

def how_to_play():
    print(f"{'####### How to play #######':^30}")
    print('    Step 1: Go to Start')
    print('    Step 2: Choose a Word Category')
    print('    Step 3: Guess a word from hint. [One Character for One Round.]')
    print('You Will Be Given 7 Life. If you are out of life, you will be hangged to dead, and the game will be over.')
    print('After the game is over, you can submit the score to scoreboard.')
    print('Scoring:')
    print('    1 Point for each correct word guess')
    print('    10 Point for completing a word')
    menu_choice = {0: 'main_menu'}
    print_choice(menu_choice)
    return menu_choice

def game_play(category_name):
    file_read = ReadWordFile(category_name)
    word_list = file_read.read()
    player = ScoreBoard()
    hangman = Hangman()
    current_word = word_list.generate_word()
    while hangman.is_dead() != True:
        clear_screen()
        hangman.print_hangman()
        hangman.print_remaining_life()
        print(player)
        current_word.print_info()
        player_guess = input('Input a Character: ')
        result = current_word.guess(player_guess)
        if result == True:
            player.correct_guess()
            if current_word.complete() == True:
                print("Word Completed")
                print(current_word)
                time.sleep(2)
                player.complete_word()
                if word_list.won == True:
                    break
                current_word = word_list.generate_word()
        else:
            hangman.draw_next()
    if word_list.won == True:
        clear_screen()
        'Out of words. You Win!!'
    else:
        clear_screen()
        hangman.print_hangman()
        'Game Over'
    player.set_name(input("Your Name: "))
    save_score = ScoreFileRW('score.txt')
    save_score.write(player)
    
def scoreboard_page():
    print(f"{'##### ScoreBoard Top 10 #####':^30}")
    score_read = ScoreFileRW('score.txt')
    try:
        score_list = score_read.read()
        if len(score_list) == 0:
            print("No Score")
        else:
            score_list.sort(key=lambda x: x[1], reverse=True)
        for no,player_info in enumerate(score_list,1):
            if no > 10:
                break
            else:
                print(f'{no}) {player_info[0]} Score: {player_info[1]}')
    except FileNotFoundError:
        print("No Score")
    menu_choice = {0: 'main_menu'}
    print_choice(menu_choice)
    return menu_choice