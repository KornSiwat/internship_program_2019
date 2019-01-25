from view import router

def start():
    route = 'main_menu'
    menu_choice = router(route)
    while True:
        choice = int(input("Your Choice: "))
        while choice not in menu_choice:
            print("Input is not valid")
            choice = int(input("Your Choice: "))
        menu_choice = router(menu_choice[choice])