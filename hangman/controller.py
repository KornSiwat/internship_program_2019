from view import router

def start():
    route = 'main_menu'
    while True:
        menu_choice = router(route)
        choice = input()
        while choice not in menu_choice:
            print("Input is not valid")
            choice = input()