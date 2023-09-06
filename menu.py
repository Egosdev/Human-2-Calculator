import time
import random
import os
import sys
import keyboard

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
                                             /_/     /_/\_\                  Version {COLOR.BOLD}1.0{COLOR.ENDC}
"""
menu_info = f"""
    Created by {COLOR.UNDERLINE}Ege{COLOR.ENDC}.
    
    You can {COLOR.OKGREEN}practice{COLOR.ENDC} to improve your proficiency in the 
    four fundamental arithmetic operations and {COLOR.OKGREEN}speed up{COLOR.ENDC}.

    {COLOR.OKBLUE}[1]{COLOR.ENDC} Addition
    {COLOR.OKCYAN}--not ready {COLOR.ENDC}{COLOR.OKBLUE}[2]{COLOR.ENDC} Subtraction
    {COLOR.OKCYAN}--not ready {COLOR.ENDC}{COLOR.OKBLUE}[3]{COLOR.ENDC} Multiplication 
    {COLOR.OKCYAN}--not ready {COLOR.ENDC}{COLOR.OKBLUE}[4]{COLOR.ENDC} Division 
    
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
        prompt = input(f" {COLOR.HEADER}>|{COLOR.ENDC} Type {COLOR.OKGREEN}[1-4]{COLOR.ENDC} to {COLOR.OKGREEN}select quiz{COLOR.ENDC}, {COLOR.FAIL}[9] {COLOR.ENDC}to {COLOR.FAIL}exit{COLOR.ENDC}: ")
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
        os.system('cls')
        prompt = ""
        print("\n\n  [+] ADDITION QUIZ \n\n")
        print(f" Don't forget to {COLOR.OKBLUE}check the settings{COLOR.ENDC}, there are {COLOR.OKBLUE}different{COLOR.ENDC} modes.\n")
        print(f" {COLOR.FAIL}m{COLOR.ENDC} or {COLOR.FAIL}M{COLOR.ENDC} | {COLOR.FAIL}main menu{COLOR.ENDC}")
        print(f" {COLOR.OKGREEN}p{COLOR.ENDC} or {COLOR.OKGREEN}P{COLOR.ENDC} | {COLOR.OKGREEN}learning pathway{COLOR.ENDC} (0% progress)")
        print(f" {COLOR.WARNING}r{COLOR.ENDC} or {COLOR.WARNING}R{COLOR.ENDC} | {COLOR.WARNING}ranked{COLOR.ENDC}")
        print(f"    -> {COLOR.WARNING}s{COLOR.ENDC} or {COLOR.WARNING}S{COLOR.ENDC} | {COLOR.WARNING}ranked settings{COLOR.ENDC}\n")
        prompt = input(f" {COLOR.HEADER}>|{COLOR.ENDC} Choose an action: ")
        prompt = prompt.lower()
        if (prompt == "r"):
            for i in range(3):
                print(f"    {3-i}!")
                time.sleep(1)
            with open("addition.py", "r", encoding='utf-8') as addition_game:
                addition_game_code = addition_game.read()
                exec(addition_game_code)
            while(prompt != "y" or prompt != "n"):
                prompt = input(f" {COLOR.HEADER}>|{COLOR.ENDC} Do you wanna {COLOR.WARNING}play again?{COLOR.ENDC} (Y/N) ")
                if (prompt == "n"):
                    change_screen(0)
                    break
                elif (prompt == "y"):
                    os.system('cls')
                    break
        elif (prompt == "s"):
            os.system('cls')
            print("settings")
            input(" press enter to continue... ")
        elif (prompt == "p"):
            os.system('cls')
            print("pathway")
            input(" press enter to continue... ")
        elif (prompt == "m"):
            change_screen(0)