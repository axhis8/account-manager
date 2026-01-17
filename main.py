from accountmanager import AccountManager

manager = AccountManager()

if __name__ == '__main__':
    while True:

            manager.print_menu()

            user_option = input("Choice (1 - 5): ")
            match user_option:
                case "1":
                    manager.generate_pwd_menu()

                case "2":
                    manager.show_accounts_menu()

                case "3":
                    manager.save_account()
                
                case "4":
                    manager.delete_account()

                case "5":
                    break
            
            input("\nEnter to continue ")