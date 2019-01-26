from model import ReadWordFile,Hangman,ScoreBoard
from os import system,listdir

def router(route):
    clear_screen()
    if route == 'main_menu':
        return main_menu()
    elif route == 'start':
        return category_menu()
    elif route == 'how to play':
        return how_to_play()

def clear_screen():
    try:
        system('clear')
    except Exception:
        system('cls')

def print_choice(choice):
    for no,key in enumerate(choice,1):
        print(f'{no}) {choice[key].title().replace("_"," ")}')

def get_category_name():
    path = 'words/'
    name_list = listdir(path)
    name_list.sort()
    return name_list

def main_menu():
    print(f"{'######### Hang Man #########':^30}")
    menu_choice = { 1:'start', 2:'how to play', 3:'score_board'}
    print_choice(menu_choice)
    return menu_choice

def category_menu():
    print(f"{'#### Choose Word Category ####':^30}")
    category_choice = dict()
    category_choice[0] = 0
    category_list = get_category_name()
    for no,name in enumerate(category_list):
        category_choice[no] = name
        print(f'{no}) {name}')
    print('0)Main Menu')
    choice = int(input("Your Choice: "))
    while choice not in category_choice:
        print("Invaild Choice")
        choice = int(input("Your Choice: "))
    if choice == 0:
        menu_choice = main_menu()
        return menu_choice
    else:
        game_play(category_choice[choice])
        menu_choice = main_menu()
        return menu_choice

def how_to_play():
    print(f"{'####### How to play #######':^30}")
    print('     Step 1: Go to Start')
    print('     Step 2: Choose a Word Category')
    print('     Step 3: Guess a word from hint. [One Character for One Round.]')
    print('You Will Be Given 7 Life. If you are out of life, you will be hangged to dead, and the game will be over.')
    print('After the game is over, you can submit the score to scoreboard.')
    print('Scoring:')
    print('     1 Point for each correct word guess')
    print('     10 Point for completing a word')
    menu_choice = {0: 'main_menu'}
    print_choice(menu_choice)
    return menu_choice

def game_play(category_name):
    file_read = ReadWordFile(category_name)
    word_list = file_read.read()
    
if __name__ == "__main__":
    print(get_category_name())