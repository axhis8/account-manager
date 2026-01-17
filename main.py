import string
import random

MIN_PWD_LENGTH = 8
MAX_PWD_LENGTH = 16
SPECIALS = ["!", "@", "#", "$", "%", "&", "*"]
STARS = "****"

# {ID: [service, username, password]}
password_list = {1: ["Youtube", "Ashis", "123"],
                 2: ["Twitch", "Fish", "asdasd"],
                 3: ["Telegram", "Bananaslayer", "H)QCWJ)EC()"],
                 4: ["Instagram", "Moinsen", "SUS"],
                 5: ["Facebook", "ashislmc", "HEYHEY"],}

# ==================== UI ====================

def print_menu():
    print(f"\n{STARS} ACCOUNT MANAGER {STARS}\n")
    print("1 - Generate a new Password")
    print("2 - Show Accounts")
    print("3 - Save Account")
    print("4 - Delete Account")
    print("5 - Exit\n")

def generate_pwd_menu():
    input_length = input("How many characters should the Password contain? (length 8-16): ")
    input_specials = input("Should there be special characters? (y/n): ")

    needs_specials = check_user_input(input_specials)

    new_pwd = generate_pwd(input_length, needs_specials)
    if new_pwd == None:
        return
    
    print(f"\nYour Password is {new_pwd}\n")

    check_user_save = input("Do you want to save the password? (y/n): ")
    if check_user_input(check_user_save):
        save_account(new_pwd)

def show_accounts_menu():
    for k, v in password_list.items():
        print(f'\n{k}. {v[0]}')
        print(f'Username: {v[1]}')
        print(f'Password: {v[2]}')


# ==================== LOGIC ====================

def check_user_input(inp):
    return True if "y" in inp else False

def generate_pwd(length, use_special):
    try:
        length = int(length)
    except ValueError:
        print(f'\nGiven length "{length}" is not a Number!')
        return 
    
    if length < MIN_PWD_LENGTH:
        print(f'\nLength must be more than {MIN_PWD_LENGTH}.')
        return 
    elif length > MAX_PWD_LENGTH:
        print(f'\nLength must be less than {MAX_PWD_LENGTH}.')
        return 

    letters = list(string.ascii_letters)
    digits = list(string.digits)

    if use_special:
        chars = ''.join(letters) + ''.join(digits) + ''.join(SPECIALS)
        password = [random.choice(letters), random.choice(digits), random.choice(SPECIALS)]
    else: 
        chars = ''.join(letters) + ''.join(digits)
        password = [random.choice(letters), random.choice(digits)]

    for _ in range(length - len(password)):
        password.append(random.choice(chars))

    random.shuffle(password)
    return ''.join(password)

def save_account(pwd=None):
    service = input("\nService: ")
    username = input("Username: ")
    if pwd == None:
        pwd = input("Password: ")
    
    if service == "" or username == "" or pwd == "":
        print("\nError. Please retry & fill in missing data.")
        return

    pwd_id = len(password_list) + 1
    password_list[pwd_id] = [service, username, pwd]
    print("\nPassword saved!")

def delete_account():
    try:
        id = int(input("ID of the account you want to delete: "))
        if id in password_list:
            print(f'\nSuccessfully deleted {password_list[id][0]} account with the ID of {id}')
            del password_list[id]
        else: 
            print("\nThere is no account with this ID.")

    except ValueError:
        print(f'\nThis ID does not exist.')
    

# ==================== INIT ====================

while True:

    print_menu()

    user_option = input("Choice (1 - 5): ")
    match user_option:
        case "1":
            generate_pwd_menu()

        case "2":
            show_accounts_menu()

        case "3":
            save_account()
        
        case "4":
            delete_account()

        case "5":
            break
    
    input("\nEnter to continue ")