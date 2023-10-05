import time
import random
import os
import sys
import ctypes
import addition
import yaml

def main():
    print()
    #TODO

os.system("")
def set_font():
    LF_FACESIZE = 32
    STD_OUTPUT_HANDLE = -11

    class COORD(ctypes.Structure):
        _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

    class CONSOLE_FONT_INFOEX(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_ulong),
                    ("nFont", ctypes.c_ulong),
                    ("dwFontSize", COORD),
                    ("FontFamily", ctypes.c_uint),
                    ("FontWeight", ctypes.c_uint),
                    ("FaceName", ctypes.c_wchar * LF_FACESIZE)]
        
    font = CONSOLE_FONT_INFOEX()
    font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
    font.nFont = 12
    font.dwFontSize.X = 32
    font.dwFontSize.Y = 32
    font.FontFamily = 54
    font.FontWeight = 400
    handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    ctypes.windll.kernel32.SetCurrentConsoleFontEx(
            handle, ctypes.c_long(False), ctypes.pointer(font))

set_font()

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

def display_settings(settings):
    if (settings['addition_settings']['is_digit_interval']):
        number_of_digits_settings_text = "Interval "
        how_many_digits_settings_text = f"{settings['addition_settings']['number_of_digits'][0]}...{settings['addition_settings']['number_of_digits'][1]}"
        if (settings['addition_settings']['is_digit_different']):
            number_of_digits_settings_text += "-different "
            example_digits_settings_text = "(** + ***), (**** + *) etc."
        else:
            number_of_digits_settings_text += "-same      "
            example_digits_settings_text = "(** + **), (*** + ***) etc."
    else:
        number_of_digits_settings_text = "Single Value        "
        how_many_digits_settings_text = f"{settings['addition_settings']['number_of_digits'][0]}"
        example_digits_settings_text = "("+(settings['addition_settings']['number_of_digits'][0] * "*") + " + " + (settings['addition_settings']['number_of_digits'][0] * "*")+")"
    if (settings['addition_settings']['memorize_mode']):
        memorize_mode_settings_text = "on "
    else:
        memorize_mode_settings_text = "off"
    if (settings['addition_settings']['cumulative_mode']):
        cumulative_mode_settings_text = "on "
    else:
        cumulative_mode_settings_text = "off"
    os.system('cls')
    print("\n\n  + ADDITION SETTINGS \n\n")
    print(f" {COLOR.OKBLUE}[1]{COLOR.ENDC} Number of questions per run: {COLOR.WARNING}{settings['addition_settings']['questions_count']}{COLOR.ENDC}       (1...20)")
    print(f" {COLOR.OKBLUE}[2]{COLOR.ENDC} Number of digits: {COLOR.WARNING}{number_of_digits_settings_text}{COLOR.ENDC}(single/interval) -[same/different]")
    print(f"     {COLOR.WARNING}{how_many_digits_settings_text} digits{COLOR.ENDC} e.g. {example_digits_settings_text}")
    print(f" {COLOR.OKBLUE}[3]{COLOR.ENDC} Memorize Mode: {COLOR.WARNING}{memorize_mode_settings_text}{COLOR.ENDC}                    (on/off)")
    if (settings['addition_settings']['memorize_mode']):
        print(f"     {COLOR.WARNING}{settings['addition_settings']['memorize_seconds']} sec{COLOR.ENDC}")
    print(f" {COLOR.OKBLUE}[4]{COLOR.ENDC} Cumulative Mode: {COLOR.WARNING}{cumulative_mode_settings_text}{COLOR.ENDC}                  (on/off)")
main()
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
        print("\n\n  + ADDITION QUIZ \n\n")
        print(f" Don't forget to {COLOR.OKBLUE}check the settings{COLOR.ENDC}, there are {COLOR.OKBLUE}different{COLOR.ENDC} modes.\n")
        print(f" {COLOR.FAIL}m{COLOR.ENDC} or {COLOR.FAIL}M{COLOR.ENDC} | {COLOR.FAIL}main menu{COLOR.ENDC}")
        print(f" {COLOR.OKGREEN}p{COLOR.ENDC} or {COLOR.OKGREEN}P{COLOR.ENDC} | {COLOR.OKGREEN}learning pathway{COLOR.ENDC} (0% progress)")
        print(f" {COLOR.WARNING}r{COLOR.ENDC} or {COLOR.WARNING}R{COLOR.ENDC} | {COLOR.WARNING}ranked{COLOR.ENDC} >> {COLOR.WARNING}s{COLOR.ENDC} or {COLOR.WARNING}S{COLOR.ENDC} {COLOR.WARNING}ranked settings{COLOR.ENDC}\n")
        prompt = input(f" {COLOR.HEADER}>|{COLOR.ENDC} Choose an action: ").lower()
        if (prompt == "r"):
            for i in range(3):
                print(f"    {3-i}!")
                time.sleep(1)
            addition.start_game()
            while (prompt != "y" or prompt != "n"):
                prompt = input(f" {COLOR.HEADER}>|{COLOR.ENDC} Do you wanna {COLOR.WARNING}play again?{COLOR.ENDC} (Y/N) ").lower()
                if (prompt == "n"):
                    change_screen(0)
                    break
                elif (prompt == "y"):
                    os.system('cls')
                    break
        elif (prompt == "s"):
            with open('config.yaml') as file:
                settings = yaml.safe_load(file)
            while (prompt != "b"):
                display_settings(settings)
                prompt = input(f"\n {COLOR.HEADER}>|{COLOR.ENDC} {COLOR.FAIL}b{COLOR.ENDC} or {COLOR.FAIL}B{COLOR.ENDC} to {COLOR.FAIL}back{COLOR.ENDC}, {COLOR.OKGREEN}[1-4]{COLOR.ENDC} to {COLOR.OKGREEN}select an action{COLOR.ENDC} for more info and adjustments: ").lower()
                if (prompt == "1"):
                    _input = -1
                    while (_input > 20 or _input < 1):
                        try:
                            _input = input(f"\n Number of Questions\n **Current number of questions per run: {COLOR.WARNING}{settings['addition_settings']['questions_count']}{COLOR.ENDC}\n > To specify how many consecutive questions will be asked,\n please {COLOR.WARNING}enter{COLOR.ENDC} a number {COLOR.WARNING}between 1 and 20{COLOR.ENDC}: ")
                            if (_input == 'b' or _input == 'B'): break
                            _input = int(_input)
                            if (_input >= 1 and _input <= 20):
                                settings['addition_settings']['questions_count'] = _input
                                break
                            else:
                                os.system('cls')
                                print(f"\n\n{COLOR.FAIL} Oops!{COLOR.ENDC} The number you entered should be {COLOR.FAIL}between 1 and 20{COLOR.ENDC}!\n")
                        except ValueError:
                            #os.system('cls')
                            break
                            print(f"\n\n{COLOR.FAIL} Oops!{COLOR.ENDC} You should enter an {COLOR.FAIL}INTEGER{COLOR.ENDC}!\n")
                elif (prompt == "2"):
                    _input = ""
                    while (_input != "single" or _input != "interval -same" or _input != "interval -different"):
                        _input = input(f"\n Number of Digits\n If you want numbers with distinct digits to be generated within a range,\n  type: {COLOR.WARNING}interval -different{COLOR.ENDC} e.g. (123 + 6),(78 + 5453)...\n\n If you want numbers to be generated within a range, but you want the digits to be the same,\n  type: {COLOR.WARNING}interval -same{COLOR.ENDC} e.g. (12 + 39),(325 + 112)...\n\n If you want only numbers with the exact number of digits you desire to be generated,\n  type: {COLOR.WARNING}single{COLOR.ENDC} e.g. (51 + 77)\n\n > Choose an action: ").lower()
                        if (_input == "single"):
                            _input = -1
                            while (_input > 10 or _input < 1):
                                try:
                                    _input = int(input(f"\n Number of Digits\n > How many digits should the numbers be?\n please {COLOR.WARNING}enter{COLOR.ENDC} a number of digits {COLOR.WARNING}between 1 and 10{COLOR.ENDC}: "))
                                    if (_input >= 1 and _input <= 10):
                                        settings['addition_settings']['number_of_digits'][0] = _input
                                        break
                                    else:
                                        print(f"{COLOR.FAIL}Oops!{COLOR.ENDC} The number of digits you entered should be {COLOR.FAIL}between 1 and 10{COLOR.ENDC}!")
                                except ValueError:
                                    print(f"{COLOR.FAIL}Oops!{COLOR.ENDC} You should enter an {COLOR.FAIL}INTEGER{COLOR.ENDC}!")
                            break
                        if (_input == "interval -same"):
                            input(" > interval -same")
                            break
                        if (_input == "interval -different"):
                            input(" > interval -different")
                            break
                        os.system('cls')
                        print("\n\n  + ADDITION SETTINGS \n\n")
                        print(f" {COLOR.OKBLUE}[1]{COLOR.ENDC} Number of questions per run: {COLOR.WARNING}{settings['addition_settings']['questions_count']}{COLOR.ENDC}       (1...20)")
                        print(f" {COLOR.OKBLUE}[2]{COLOR.ENDC} Number of digits: {COLOR.WARNING}{number_of_digits_settings_text}{COLOR.ENDC}(single/interval) -[same/different]")
                        print(f"     {COLOR.WARNING}{how_many_digits_settings_text} digits{COLOR.ENDC} e.g. {example_digits_settings_text}")
                        print(f" {COLOR.OKBLUE}[3]{COLOR.ENDC} Memorize Mode: {COLOR.WARNING}{memorize_mode_settings_text}{COLOR.ENDC}                    (on/off)")
                        if (settings['addition_settings']['memorize_mode']):
                            print(f"     {COLOR.WARNING}{settings['addition_settings']['memorize_seconds']} sec{COLOR.ENDC}")
                        print(f" {COLOR.OKBLUE}[4]{COLOR.ENDC} Cumulative Mode: {COLOR.WARNING}{cumulative_mode_settings_text}{COLOR.ENDC}                  (on/off)")
                elif (prompt == "3"):
                    input(" > 3")
                elif (prompt == "4"):
                    input(" > 4")   
                with open('config.yaml', 'w') as file:
                    yaml.dump(settings, file)
        elif (prompt == "p"):
            os.system('cls')
            print("pathway")
            input(" press enter to continue... ")
        elif (prompt == "m"):
            change_screen(0)