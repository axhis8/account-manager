import json
import keyring as kr
import random
import string
import os

# Path to file to this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Path for Json
JSON_PATH = os.path.join(BASE_DIR, "accounts.json")
MIN_PWD_LENGTH = 8
MAX_PWD_LENGTH = 64
SPECIALS = ["!", "@", "#", "$", "%", "&", "*"]
STARS = "****"

class AccountManager:

    def __init__(self):

        try:
            with open(JSON_PATH, "r") as file:
                data: dict = json.load(file)
                self.password_list = {int(k): v for k, v in data.items()}
        except FileNotFoundError:
            self.password_list = {} # {ID: [service, username]}
        except json.JSONDecodeError:
            print("\nJSON File is damaged, creating a new list.\n")
            self.password_list = {}

        # Get highest ID
        self.password_id = max(list(self.password_list.keys())) if self.password_list else 0


    # ==================== UI ====================

    def print_menu(self):
        print(f"\n{STARS} ACCOUNT MANAGER {STARS}\n")
        print("1 - Generate a new Password")
        print("2 - Show Accounts")
        print("3 - Save Account")
        print("4 - Delete Account")
        print("5 - Exit\n")

    def generate_pwd_menu(self):
        input_length = input("How many characters should the Password contain? (length 8-64): ")
        input_specials = input("Should there be special characters? (y/n): ")

        needs_specials = self.check_user_input(input_specials)

        new_pwd = self.generate_pwd(input_length, needs_specials)
        if new_pwd == None:
            return
        
        print(f"\nYour Password is {new_pwd}\n")

        check_user_save = input("Do you want to save the password? (y/n): ")
        if self.check_user_input(check_user_save):
            self.save_account(new_pwd)

    def show_accounts_menu(self):
        if self.password_list == {}:
            print("\nNo Passwords saved.\n")
            input("Enter to continue ")
            return
        
        for k, v in self.password_list.items():
            print(f'\nID: {k} - {v[0]}')
            print(f'Username: {v[1]}')
        
        id_input = input("\nType which ID to show Password (Enter to exit): ")
        if id_input == "": return

        try:
            id_input = int(id_input)
        except ValueError:
            print("This ID is not a Number.")
            return
        
        if id_input in self.password_list:

            gotten_service = self.password_list[id_input][0]
            gotten_username = self.password_list[id_input][1]
            gotten_pwd = self._get_password(gotten_service, gotten_username)

            if gotten_pwd == None:
                return

            print(f'\n{id_input}. {gotten_service}')
            print(f'Username: {gotten_username}')
            print(f'Password: {gotten_pwd}')
            input("\nEnter to continue ")
        
        else:
            print("\nError. This ID does not exist.")

    # ==================== WRAPPER ====================

    def _set_password(self, service, username, pwd):
        try:
            kr.set_password(service, username, pwd)
            self._save_pwd_in_json()
            print("\nPassword saved!")
        except Exception as e:
            print("\nError. Couldn't save Account.")

    def _get_password(self, service, username):
        try:
            return kr.get_password(service, username)
        except Exception as e:
            print("\nError. Couldn't retrieve Account.")
            return None

    def _del_password(self, service, username):
        try:
            kr.delete_password(service, username)
            return True
        except Exception as e:
            print("\nError. Couldn't delete Account.")
            return False
        
    def _save_pwd_in_json(self):
        try:
            with open(JSON_PATH, "w") as file:
                json.dump(self.password_list, file, indent=4)
        except Exception as e:
            print(f'Loading Error: {e}')


    # ==================== LOGIC ====================

    @staticmethod
    def check_user_input(inp):
        return True if "y" in inp else False

    @staticmethod
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

    def save_account(self, pwd=None):
        service = input("\nService: ")
        username = input("Username: ")
        if pwd == None:
            pwd = input("Password: ")
        
        if service == "" or username == "" or pwd == "":
            print("\nError. Please retry & fill in missing data.")
            return

        self.password_id += 1
        self.password_list[self.password_id] = [service, username]

        self._set_password(service, username, pwd)

    def delete_account(self):
        try:
            id = int(input("\nID of the account you want to delete: "))
            if id in self.password_list:

                del_service = self.password_list[id][0]
                del_username = self.password_list[id][1]

                print(f'\nService: {del_service}')
                print(f'Username: {del_username}')
                confirm = input("\nAre you sure you want to delete this Account? (y/n): ")
                if not self.check_user_input(confirm):
                    return

                if self._del_password(del_service, del_username):
                    print(f'\nSuccessfully deleted {self.password_list[id][0]} account with the ID of {id}')
                    del self.password_list[id]
                    self._save_pwd_in_json()

            else: 
                print("\nThere is no account with this ID.")

        except ValueError:
            print(f'\nThis ID does not exist.')
        
        input("\nEnter to continue ")