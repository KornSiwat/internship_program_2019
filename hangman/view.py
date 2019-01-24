from model import Hangman
from os import system,listdir

def router(route):
    clear_screen()
    if route == 'main_menu':
        return main_menu()

def clear_screen():
    try:
        system('clear')
    except Exception:
        system('cls')

def print_choice(choice):
    for no,choice in enumerate(choice,1):
        print(f'{no}:{choice}')

def get_category_name():
        path = 'words/'
        name_list = listdir(path)
        print(name_list)

def main_menu():
    print(f"{'######### Hang Man #########':^30}")
    choice = ['start', 'how to play', 'score_board']
    print_choice(choice)

if __name__ == "__main__":
    get_category_name()