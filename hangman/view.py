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

def draw_rope():
    print(f"{'  ||  ':^30}")

def draw_head():
    print(f"{'####':^30}")
    print(f"{'#  #':^30}")
    print(f"{'####':^30}")

def draw_left_arm():
    print(f"{'######        ':^30}")

def draw_right_arm():
    print(f"{'######  ######':>22}")

def print_choice(choice):
    for no,choice in enumerate(choice,1):
        print(f'{no}:{choice}')

def main_menu():
    print(f"{'######### Hang Man #########':^30}")
    draw_rope()
    draw_head()
    draw_left_arm()
    draw_right_arm()
    choice = ['start', 'how to play']
    print_choice(choice)