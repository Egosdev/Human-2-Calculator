import random
import time
import os

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
    
#SETTINGS
QUESTIONS_COUNT = 10
NUMBER_OF_DIGITS = 2

class Status_Object:
  def __init__(self, question = "", seconds = 0, first_try = -1):
    self.question = question
    self.seconds = seconds
    self.first_try = first_try
    
status_array = []
current_question = 0

for i in range (QUESTIONS_COUNT):
    status_array.append(Status_Object())

def display_status_bar():
    os.system('cls')
    print("\n")
    print("   ", end = " ")
    for i in range (QUESTIONS_COUNT):
        if (status_array[i].first_try == -1):
            print("█", end = " ")
        elif(status_array[i].first_try == True):
            print(f"{COLOR.OKGREEN}█{COLOR.ENDC}", end = " ")
        else:
            print(f"{COLOR.WARNING}█{COLOR.ENDC}", end = " ")
    print(f" < [{current_question}/{QUESTIONS_COUNT}] Questions\n\n")

def result_statistics():
    display_status_bar()
    
    total_time = 0
    min_time = status_array[0].seconds
    max_time = 0
    worst_question_index = 0
    total_first_try = 0
    
    for i in status_array:
        total_time += i.seconds
        if (i.seconds < min_time):
            min_time = i.seconds
        if (i.seconds > max_time):
            max_time = i.seconds
            worst_question = i.question
        if (i.first_try == True):
            total_first_try += 1
            
    avg_time = round(total_time / QUESTIONS_COUNT, 2)
    total_time = round(total_time, 2)
    
    print(f"{COLOR.OKGREEN} █ GREEN{COLOR.ENDC} squares means solved on {COLOR.UNDERLINE}first try{COLOR.ENDC}")
    print(f"{COLOR.WARNING} █ YELLOW{COLOR.ENDC} squares means {COLOR.UNDERLINE}not{COLOR.ENDC} solved at once\n")
    print(f"   - -*- - {COLOR.OKBLUE}STATISTICS{COLOR.ENDC} - -*- -\n")
    print(f" {COLOR.OKBLUE} * Total time{COLOR.ENDC}                for {COLOR.UNDERLINE}{QUESTIONS_COUNT}{COLOR.ENDC} questions {COLOR.OKCYAN}{total_time} sec{COLOR.ENDC}")
    print(f" {COLOR.WARNING} * Best time{COLOR.ENDC}                 {COLOR.OKCYAN}{min_time} sec{COLOR.ENDC}")
    print(f" {COLOR.OKBLUE} * Worst time{COLOR.ENDC}                {COLOR.OKCYAN}{max_time} sec{COLOR.ENDC} with {COLOR.FAIL}{worst_question}{COLOR.ENDC} operation")
    print(f" {COLOR.WARNING} * Average time{COLOR.ENDC}              {COLOR.OKCYAN}{avg_time} sec{COLOR.ENDC}")
    print(f" {COLOR.OKBLUE} * Solved On The First Try{COLOR.ENDC}   {COLOR.OKCYAN}{total_first_try}{COLOR.ENDC} out of {COLOR.OKCYAN}{QUESTIONS_COUNT}{COLOR.ENDC}\n")
    
    d = str(input(f" If you wanna see details type {COLOR.OKCYAN}d{COLOR.ENDC} or {COLOR.OKCYAN}D{COLOR.ENDC} : "))
    if (d == "d" or d == "D"):
        result_statistics_details(avg_time)

def result_statistics_details(_avg_time):
    count = 1
    print(" ")
    for i in status_array:
        if (i.seconds > _avg_time):
            print(f"  {count}. Question: {COLOR.WARNING}{i.question}{COLOR.ENDC} {COLOR.FAIL}{i.seconds} sec{COLOR.ENDC}")
        else:
            print(f"  {count}. Question: {COLOR.WARNING}{i.question}{COLOR.ENDC} {COLOR.OKGREEN}{i.seconds} sec{COLOR.ENDC}")
        
        count += 1
    print(" ")
    
    
#Start game

for i in range (QUESTIONS_COUNT):
    current_question = i+1
    display_status_bar()
    rn_one = random.randint((10 ** (NUMBER_OF_DIGITS-1)), (10 ** (NUMBER_OF_DIGITS))-1)
    rn_two = random.randint((10 ** (NUMBER_OF_DIGITS-1)), (10 ** (NUMBER_OF_DIGITS))-1)
    rn_sum = rn_one + rn_two
    start_time = time.time()
    rn_input_info = f"{str(rn_one)} + {str(rn_two)}"
    status_array[i].question = rn_input_info
    while True:
        rn_user_input = input(f"  [{COLOR.OKBLUE}Q{i+1}{COLOR.ENDC}]  {rn_input_info} : ")
        try:
            rn_user_input = int(rn_user_input)
        except ValueError:
            print(f" {COLOR.FAIL}Oops!{COLOR.ENDC} You have to type an {COLOR.FAIL}INTEGER{COLOR.ENDC}")
            continue
        if rn_user_input == rn_sum:
            elapsed_time = round(time.time() - start_time, 2)
            print(f" {COLOR.OKGREEN}CORRECT!{COLOR.ENDC}", elapsed_time, "seconds")
            status_array[i].seconds = elapsed_time
            if (status_array[i].first_try == -1):
                status_array[i].first_try = True;
            input(f" {COLOR.HEADER}>|{COLOR.ENDC} Press {COLOR.WARNING}enter{COLOR.ENDC} to continue...")
            break
        else:
            print(f" {COLOR.FAIL}WRONG!{COLOR.ENDC}")
            status_array[i].first_try = False;
            
result_statistics()