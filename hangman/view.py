from model import Hangman
from os import system,listdir

def router(route):
    clear_screen()
    if route == 'main_menu':
        return main_menu()
    elif route == 'start':
        return category_menu()

def clear_screen():
    try:
        system('clear')
    except Exception:
        system('cls')

def print_choice(choice):
    for no,key in enumerate(choice,1):
        print(f'{no}:{choice[key].title().replace("_"," ")}')

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
    

if __name__ == "__main__":
    print(get_category_name())