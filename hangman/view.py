from model import *
from os import system

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

def main_menu():
    print(f"{'######### Hang Man #########':^30}")
    choice = ['start', 'how to play']
    print_choice(choice)