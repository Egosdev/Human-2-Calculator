import time
import random
import os

os.system("")

class COLOR:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

menu_logo = f"""*
  _    _                            {COLOR.FAIL} ___ {COLOR.ENDC}  _____      _            _       _             
 | |  | |                           {COLOR.FAIL}|__ \{COLOR.ENDC} / ____|    | |          | |     | |            
 | |__| |_   _ _ __ ___   __ _ _ __ {COLOR.FAIL}   ) {COLOR.ENDC}| |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 |  __  | | | | '_ ` _ \ / _` | '_ \{COLOR.FAIL}  / /{COLOR.ENDC}| |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |  | | |_| | | | | | | (_| | | | |{COLOR.FAIL}/ /_{COLOR.ENDC}| |___| (_| | | (__| |_| | | (_| | || (_) | |   
 |_|  |_|\__,_|_| |_| |_|\__,_|_| |_|{COLOR.FAIL}____{COLOR.ENDC}|\_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                  __
                               _                 / /                      
                             _| |_   ______     / /  __  __               
                            |_   _| |______|   / /   \ \/ /               
                              |_|             / /     >  <                
                                             /_/     /_/\_\               
"""
menu_info = f"""
    Version {COLOR.BOLD}1.0{COLOR.ENDC}
    Created by {COLOR.UNDERLINE}Ege{COLOR.ENDC}
    
    You can {COLOR.OKGREEN}practice{COLOR.ENDC} to improve your proficiency in the 
    four fundamental arithmetic operations and {COLOR.OKGREEN}speed up{COLOR.ENDC}.

    {COLOR.OKBLUE}[1]{COLOR.ENDC} Addition
    {COLOR.OKBLUE}--[2]{COLOR.ENDC} Subtraction {COLOR.OKCYAN}**not ready{COLOR.ENDC}
    {COLOR.OKBLUE}--[3]{COLOR.ENDC} Multiplication {COLOR.OKCYAN}**not ready{COLOR.ENDC}
    {COLOR.OKBLUE}--[4]{COLOR.ENDC} Division {COLOR.OKCYAN}**not ready{COLOR.ENDC}
    
    {COLOR.OKBLUE}[9]{COLOR.ENDC} Exit the program
    """
    
DISPLAY_SCREEN = 0
    
def menu_input_check(_str):
    if len(_str) == 1 and _str.isdigit():
        single_digit_number = int(_str)
        return single_digit_number
    else:
        return False

def display_menu():
    print(menu_logo)
    print(menu_info)
    
def change_screen(i):
    os.system('cls')
    global DISPLAY_SCREEN
    DISPLAY_SCREEN = i
    if (i == 0):
        display_menu()
        
change_screen(0)

while True:
    if (DISPLAY_SCREEN == 0):
        prompt = input(f" {COLOR.HEADER}>|{COLOR.ENDC} Type {COLOR.OKGREEN}[1-4]{COLOR.ENDC} to {COLOR.OKGREEN}select game{COLOR.ENDC}, {COLOR.FAIL}[9] {COLOR.ENDC}to {COLOR.FAIL}exit{COLOR.ENDC}: ")
        if (menu_input_check(prompt)):
            n = menu_input_check(prompt)
            if (n == 1):
                change_screen(1)
            elif (n == 2):
                print("**2")
            elif (n == 3):
                print("**3")
            elif (n == 4):
                print("**4")
            elif (n == 9):
                exit()
        else:
            print(" ")
            print(f" {COLOR.FAIL}Oops!{COLOR.ENDC} Just follow the instructions. {COLOR.FAIL}TYPE AGAIN CORRECTLY...{COLOR.ENDC} ")
    if (DISPLAY_SCREEN == 1):
        print("\n\n  [+] ADDITION GAME \n\n")
        print(f" Now, you should {COLOR.OKBLUE}relax{COLOR.ENDC} a bit.")
        print(f" Try to be as {COLOR.OKBLUE}fast{COLOR.ENDC} as you can.\n")
        input(f" {COLOR.HEADER}>|{COLOR.ENDC} Are you feel {COLOR.OKGREEN}ready?{COLOR.ENDC} press {COLOR.OKGREEN}enter{COLOR.ENDC} to continue...\n")
        for i in range(3):
            print(f"    {3-i}!")
            time.sleep(1)
        with open("addition.py", "r", encoding='utf-8') as addition_game:
            addition_game_code = addition_game.read()
            exec(addition_game_code)
        prompt = ""
        while(prompt != "Y" or prompt != "y" or prompt != "N" or prompt != "n"):
            prompt = input(f" {COLOR.HEADER}>|{COLOR.ENDC} Do you wanna {COLOR.WARNING}play again?{COLOR.ENDC} (Y/N) ")
            if (prompt == "N" or prompt == "n"):
                change_screen(0)
                break
            elif (prompt == "Y" or prompt == "y"):
                os.system('cls')
                break